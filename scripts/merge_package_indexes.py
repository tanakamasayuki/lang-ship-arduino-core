#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


PACKAGE_URL = "https://github.com/tanakamasayuki/lang-ship-arduino-core"


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

    merged_package = {
        "name": "lang-ship",
        "maintainer": "tanakamasayuki",
        "websiteURL": PACKAGE_URL,
        "email": "",
        "help": {
            "online": PACKAGE_URL,
        },
        "platforms": [],
        "tools": [],
    }

    for index_path in args.indexes:
        for package in load_index(index_path)["packages"]:
            platforms = package.get("platforms", [])
            if not isinstance(platforms, list):
                raise ValueError(f"{index_path} contains a package without a platforms array")
            merged_package["platforms"].extend(platforms)

    merged = {"packages": [merged_package]}
    args.output.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
