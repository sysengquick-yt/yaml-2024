#!/usr/bin/env python3

import sys
import json
from ruamel.yaml import YAML


def _main():
    filename = "s02.yaml"

    if len(sys.argv) == 2:
        filename = sys.argv[1]

    yaml = YAML()

    try:
        with open(filename, "r") as f:
            docs = list(yaml.load_all(f))
    except IOError as e:
        print(e)
        sys.exit(1)

    for doc in docs:
        print(json.dumps(doc, indent=2, default=str))


if __name__ == "__main__":
    _main()
