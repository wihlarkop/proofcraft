#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_SKILLS = ROOT / "src" / "skills"
SHARED = ROOT / "src" / "shared"


def load_json_yaml(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def build(output: Path):
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    for skill_dir in sorted(p for p in SRC_SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").exists()):
        dest = output / skill_dir.name
        dest.mkdir(parents=True)
        for child in skill_dir.iterdir():
            if child.name in {"build.yaml", "SKILL.md"}:
                continue
            target = dest / child.name
            if child.is_dir():
                shutil.copytree(child, target)
            else:
                shutil.copy2(child, target)
        manifest_path = skill_dir / "build.yaml"
        manifest = load_json_yaml(manifest_path) if manifest_path.exists() else {"shared": []}
        for rel in manifest.get("shared", []):
            src = SHARED / rel
            if not src.exists():
                raise SystemExit(f"Missing shared reference for {skill_dir.name}: {rel}")
            target = dest / "references" / "_shared" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, target)

        # Make every distributable skill self-contained and ensure the copied
        # shared methodology is explicitly reachable through progressive disclosure.
        skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8").rstrip()
        refs = []
        local_refs = skill_dir / "references"
        if local_refs.exists():
            for ref in sorted(p for p in local_refs.rglob("*.md") if p.is_file()):
                rel = ref.relative_to(skill_dir).as_posix()
                refs.append((rel, ref.stem.replace("-", " ")))
        for rel in manifest.get("shared", []):
            refs.append((f"references/_shared/{rel}", Path(rel).stem.replace("-", " ")))
        if refs:
            lines = ["", "## Reference Guide", "", "Load only the references needed for the current task:", ""]
            for rel, label in refs:
                lines.append(f"- [{label}]({rel})")
            skill_text += "\n".join(lines)
        (dest / "SKILL.md").write_text(skill_text + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=ROOT / "skills")
    args = ap.parse_args()
    build(args.output.resolve())
    print(f"Built skills into {args.output.resolve()}")

if __name__ == "__main__":
    main()
