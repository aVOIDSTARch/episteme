import argparse
import json

import requests

BASE = "http://127.0.0.1:8100/api/v1/framework"


def list_tree(path: str):
    resp = requests.get(f"{BASE}/tree", params={"path": path})
    resp.raise_for_status()
    return resp.json()


def get_file(path: str):
    resp = requests.get(f"{BASE}/file", params={"path": path})
    resp.raise_for_status()
    return resp.json()


def search(q: str):
    resp = requests.get(f"{BASE}/search", params={"query": q})
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Episteme knowledge CLI")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("tree")
    p1.add_argument("--path", default="")

    p2 = sub.add_parser("file")
    p2.add_argument("path", help="Relative path under episteme-framework")

    p3 = sub.add_parser("search")
    p3.add_argument("query")

    args = parser.parse_args()
    if args.cmd == "tree":
        print(json.dumps(list_tree(args.path), indent=2))
    elif args.cmd == "file":
        print(json.dumps(get_file(args.path), indent=2))
    elif args.cmd == "search":
        print(json.dumps(search(args.query), indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
