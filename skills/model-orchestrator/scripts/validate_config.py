#!/usr/bin/env python3
import argparse
from orchestrator_core import dump, load_json, validate_config
p=argparse.ArgumentParser(); p.add_argument("--config",required=True); a=p.parse_args()
dump(validate_config(load_json(a.config),a.config))

