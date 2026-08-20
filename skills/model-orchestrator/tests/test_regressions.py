import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'scripts'))
REQUIRED={"model","provider","agent","attempts","changed_files","commands","input_tokens","output_tokens","total_cost","duration_seconds","failures","fallback","objective_verdict","executor","reviewer"}

def calc(rows):
    missing=[]
    for r in rows:
        absent=sorted(REQUIRED-set(r)); assert isinstance(absent,list) and all(isinstance(x,str) for x in absent); missing.extend(absent)
    return sorted(set(missing))
def row():
    return {k: [] if k in ('changed_files','commands','failures') else (0 if k in ('input_tokens','output_tokens','total_cost','duration_seconds','attempts') else ('accepted' if k=='objective_verdict' else 'x')) for k in REQUIRED}
def main():
    assert calc([row()])==[]
    x=row(); del x['reviewer']; assert calc([x])==['reviewer']
    x=row(); del x['reviewer']; del x['executor']; assert calc([x])==['executor','reviewer']
    x=row(); x['changed_files']=[['nested']]; assert calc([x])==[]
    print('regressions: PASS')
if __name__=='__main__': main()

