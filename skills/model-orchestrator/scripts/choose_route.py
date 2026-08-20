#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from orchestrator_core import choose_route, dump, load_json

parser=argparse.ArgumentParser()
parser.add_argument("classification")
parser.add_argument("--config",required=True)
parser.add_argument("--output",required=True)
args=parser.parse_args()
artifact=choose_route(load_json(args.classification),load_json(args.config))
Path(args.output).write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
dump(artifact)

