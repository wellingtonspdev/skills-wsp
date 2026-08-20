#!/usr/bin/env python3
import argparse
from pathlib import Path
from orchestrator_core import classify, dump, load_json

parser=argparse.ArgumentParser()
parser.add_argument("task")
parser.add_argument("--output", required=True)
args=parser.parse_args()
artifact=classify(load_json(args.task))
Path(args.output).write_text(__import__("json").dumps(artifact,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
dump(artifact)

