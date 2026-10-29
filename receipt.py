"""Print an itemised receipt from fixed values."""

import sys
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")

# (description, quantity, unit price)
ITEMS = [
    ("Paperback novel", 1, Decimal("9.99")),
    ("Hardback notebook", 2, Decimal("3.50")),
    ("Bookmark", 3, Decimal("0.75")),
]


def money(value: Decimal) -> str:
    """Format an amount with exactly two decimal places."""
    return f"{value.quantize(CENT, rounding=ROUND_HALF_UP):.2f}"


def main() -> int:
    print("THE CORNER BOOKSHOP")
    print("=" * 40)
    total = Decimal("0")
    for description, quantity, unit_price in ITEMS:
        line_total = quantity * unit_price
        total += line_total
        label = f"{description} x{quantity} @ {money(unit_price)}"
        print(f"{label:<30}{money(line_total):>10}")
    print("-" * 40)
    print(f"{'TOTAL':<30}{money(total):>10}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
