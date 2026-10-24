# Workbench: first Python scripts for the bookshop

Four small command-line scripts. Python 3.11 or newer, standard library only, no third-party packages.

| Script | What it does |
| --- | --- |
| `hello.py` | Greets a name given as an argument (default `World`) |
| `receipt.py` | Prints a three-line itemised receipt from fixed values |
| `tips.py` | Prints bill, tip and grand total for a bill and tip rate |
| `greet_env.py` | Stretch goal: greets the name in the `WORKBENCH_NAME` environment variable |

## 1. Set up the virtual environment

Run these from inside the `workbench` folder.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Your prompt now starts with `(.venv)`. The scripts need no packages, so there is nothing to `pip install`. To leave the environment, run `deactivate`. On Windows the activate command is `.venv\Scripts\activate`.

Check the version with `python --version` (3.11 or newer).

## 2. Run the scripts

With the environment active, `python` is the command to use.

### hello.py

```bash
python hello.py            # Hello, World!
python hello.py Rae        # Hello, Rae!
python hello.py "Ada Lovelace"
```

Names with spaces need quotes. With no argument the script greets `World`.

### receipt.py

```bash
python receipt.py
```

```
THE CORNER BOOKSHOP
========================================
Paperback novel x1 @ 9.99           9.99
Hardback notebook x2 @ 3.50         7.00
Bookmark x3 @ 0.75                  2.25
----------------------------------------
TOTAL                              19.24
```

### tips.py

```bash
python tips.py BILL TIP_PERCENT
python tips.py 45.50 15
```

The tip rate is a **percentage**: `15` means 15%, not `0.15`.

```
Bill:             45.50
Tip (15%):         6.83
Grand total:      52.33
```

Check: 15% of 45.50 is 6.825, which rounds half up to 6.83, so the grand total is 52.33.

### greet_env.py (stretch goal)

```bash
python greet_env.py                      # Hello, World!
WORKBENCH_NAME=Rae python greet_env.py   # Hello, Rae!
```

## 3. Errors and exit codes

Bad input prints a short message to standard error, with no traceback, and exits with code `1`. Success exits with `0`. Check the code in your shell with `echo $?`.

| Command | Message | Exit |
| --- | --- | --- |
| `python hello.py a b` | Please give just one name... | 1 |
| `python tips.py` | Expected 2 arguments, but got 0. | 1 |
| `python tips.py abc 15` | The bill must be a number, but got 'abc'. | 1 |
| `python tips.py 45.50 fifteen` | The tip rate must be a number, but got 'fifteen'. | 1 |
| `python tips.py 45.50 -5` | The tip rate cannot be negative. | 1 |
| `python tips.py -10 15` | The bill must be greater than zero. | 1 |
| `WORKBENCH_NAME=" " python greet_env.py` | WORKBENCH_NAME is set but empty. | 1 |

## 4. Design notes

- `tips.py` and `receipt.py` use `decimal.Decimal` (standard library) instead of floats. Plain `round(6.825, 2)` can give `6.82` because 6.825 cannot be stored exactly as a float. `Decimal` with round-half-up gives the 6.83 a customer expects.
- `tips.py` rejects `nan` and `inf`, which Python would otherwise accept as numbers.
- Each script keeps its logic in `main()` and ends with `sys.exit(main(...))`, so the exit code is explicit.

## 5. Style check

The code was checked against PEP 8 with `pycodestyle` (a development-time check only, not needed to run the scripts):

```bash
pip install pycodestyle
pycodestyle *.py
```
# simple-python-scripts
