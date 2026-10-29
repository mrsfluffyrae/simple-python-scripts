"""Print the bill, tip and grand total for a bill and a tip rate."""

import sys
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

CENT = Decimal("0.01")
USAGE = (
    "Usage: python tips.py BILL TIP_PERCENT "
    "(example: python tips.py 45.50 15)"
)


def parse_number(text: str, label: str) -> Decimal:
    """Convert text to a finite number, or raise a clear ValueError."""
    try:
        value = Decimal(text)
    except InvalidOperation:
        raise ValueError(
            f"the {label} must be a number, but got '{text}'."
        ) from None
    if not value.is_finite():
        raise ValueError(
            f"the {label} must be a normal number, but got '{text}'."
        )
    return value


def money(value: Decimal) -> str:
    """Round half up to the cent and format with two decimal places."""
    return f"{value.quantize(CENT, rounding=ROUND_HALF_UP):.2f}"


def main(argv: list[str]) -> int:
    args = argv[1:]
    if len(args) != 2:
        print(
            f"Error: expected 2 arguments, but got {len(args)}.",
            file=sys.stderr,
        )
        print(USAGE, file=sys.stderr)
        return 1

    try:
        bill = parse_number(args[0], "bill")
        tip_percent = parse_number(args[1], "tip rate")
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 1

    if bill <= 0:
        print("Error: the bill must be greater than zero.", file=sys.stderr)
        return 1
    if tip_percent < 0:
        print("Error: the tip rate cannot be negative.", file=sys.stderr)
        return 1

    tip = (bill * tip_percent / 100).quantize(CENT, rounding=ROUND_HALF_UP)
    grand_total = bill + tip

    print(f"Bill:        {money(bill):>10}")
    tip_label = f"Tip ({tip_percent.normalize():f}%):"
    print(f"{tip_label:<13}{money(tip):>10}")
    print(f"Grand total: {money(grand_total):>10}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
