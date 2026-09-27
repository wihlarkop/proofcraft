#!/usr/bin/env python3
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def frontmatter(text: str):
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    block = text[4:end]
    data = {}
    current = None
    for line in block.splitlines():
        if not line.startswith(" ") and ":" in line:
            k, v = line.split(":", 1)
            current = k.strip(); data[current] = v.strip()
        elif current == "description" and line.startswith("  "):
            data[current] = (data[current] + " " + line.strip()).strip()
    return data


def validate_skill(skill: Path):
    errors=[]
    text=(skill/'SKILL.md').read_text(encoding='utf-8')
    try: fm=frontmatter(text)
    except ValueError as e: return [str(e)]
    name=fm.get('name','')
    desc=fm.get('description','').replace('>-','').strip()
    if name != skill.name: errors.append(f"name {name!r} does not match directory")
    if not NAME_RE.match(name): errors.append("invalid skill name")
    if not desc: errors.append("description is empty")
    if len(desc)>1024: errors.append("description exceeds 1024 chars")
    if len(text.splitlines())>500: errors.append("SKILL.md exceeds 500 lines")
    for match in LINK_RE.finditer(text):
        target=match.group(1).split('#',1)[0]
        if not target or '://' in target or target.startswith('mailto:'): continue
        p=(skill/target).resolve()
        if not p.exists(): errors.append(f"broken local link: {target}")
    return errors


def main():
    if not SKILLS.exists(): raise SystemExit("skills/ missing; run scripts/build.py")
    failures=[]
    generated = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for skill in generated:
        errs=validate_skill(skill)
        eval_path = skill / "evals" / "evals.json"
        if not eval_path.exists():
            errs.append("missing evals/evals.json")
        else:
            try:
                data=json.loads(eval_path.read_text(encoding="utf-8"))
                cases=data.get("evals", [])
                if len(cases) < 5: errs.append("fewer than 5 eval cases")
                if data.get("skill_name") != skill.name: errs.append("eval skill_name mismatch")
            except Exception as e:
                errs.append(f"invalid eval JSON: {e}")
        if errs: failures.append((skill.name,errs))

    try:
        suite=json.loads((ROOT/"suite.yaml").read_text(encoding="utf-8"))
        implemented=set(suite.get("implemented", []))
        actual={p.name for p in generated}
        if implemented != actual:
            failures.append(("suite.yaml", [f"implemented list {sorted(implemented)} != generated skills {sorted(actual)}"]))
    except Exception as e:
        failures.append(("suite.yaml", [f"invalid JSON-compatible YAML: {e}"]))

    if failures:
        for name,errs in failures:
            for e in errs: print(f"ERROR {name}: {e}")
        raise SystemExit(1)
    print(f"Validated {len(generated)} generated skills, eval sets, and suite manifest")

if __name__=='__main__': main()
