from argparse import ArgumentParser
import os


def initialize(subparsers):
    subparser: ArgumentParser = subparsers.add_parser(
        "init", help="initialize sfit for filename")
    subparser.add_argument("filename", help="name of file to be tracked")
    subparser.set_defaults(func=main)


class Commit:
    # Stores commit metadata and points to the corresponding snapshot
    def __init__(self, message):
        self.name = None
        self.type = "Text"


def main(args):
    # Create .sfit folder
    try:
        os.makedirs(".sfit")
    except OSError as e:
        print("sfit already initialized")
        return

    # Create config file
    config = os.path.join(".sfit", "config")
    with open(config, "w") as f:
        f.write(args.filename)

    # Create .sfit folders
    folders = ["refs", "objects"]
    for folder in folders:
        os.makedirs(os.path.join(".sfit", folder))

    # Create refs file
    os.makedirs(os.path.join(".sfit", "refs", "heads"), exist_ok=True)
    os.makedirs(os.path.join(".sfit", "refs", "tags"), exist_ok=True)


if __name__ == "__main__":
    print("invalid usage")
