#!/usr/bin/env python3
from __future__ import annotations
import filecmp, tempfile
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build import build


def compare(a: Path,b: Path,rel=Path('.')):
    da=a/rel; db=b/rel
    names=set([p.name for p in da.iterdir()] if da.exists() else []) | set([p.name for p in db.iterdir()] if db.exists() else [])
    diffs=[]
    for name in sorted(names):
        pa=da/name; pb=db/name; r=rel/name
        if not pa.exists() or not pb.exists(): diffs.append(str(r)); continue
        if pa.is_dir()!=pb.is_dir(): diffs.append(str(r)); continue
        if pa.is_dir(): diffs.extend(compare(a,b,r))
        elif not filecmp.cmp(pa,pb,shallow=False): diffs.append(str(r))
    return diffs


def main():
    with tempfile.TemporaryDirectory() as td:
        tmp=Path(td)/'skills'
        build(tmp)
        current=ROOT/'skills'
        diffs=compare(tmp,current)
        if diffs:
            print('Generated tree is stale. Run: python scripts/build.py')
            for d in diffs[:50]: print(' -',d)
            raise SystemExit(1)
    print('Generated tree matches canonical sources')

if __name__=='__main__': main()
