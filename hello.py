"""Greet a name given on the command line (defaults to "World")."""

import sys


def main(argv: list[str]) -> int:
    args = argv[1:]
    if len(args) > 1:
        print(
            "Error: please give just one name. Put names with spaces "
            'in quotes, e.g. python hello.py "Ada Lovelace"',
            file=sys.stderr,
        )
        return 1

    name = args[0].strip() if args else "World"
    if not name:
        print("Error: the name cannot be empty.", file=sys.stderr)
        return 1

    print(f"Hello, {name}!")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
