

import os
import sys


def main() -> int:
    name = os.environ.get("WORKBENCH_NAME", "World").strip()
    if not name:
        print(
            "Error: WORKBENCH_NAME is set but empty. "
            "Give it a name or unset it to greet the world.",
            file=sys.stderr,
        )
        return 1

    print(f"Hello, {name}!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
