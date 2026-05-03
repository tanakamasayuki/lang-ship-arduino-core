#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_index(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data.get("packages"), list):
        raise ValueError(f"{path} does not contain a packages array")
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("indexes", nargs="+", type=Path)
    args = parser.parse_args()

    merged = {"packages": []}
    for index_path in args.indexes:
        merged["packages"].extend(load_index(index_path)["packages"])

    args.output.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
