"""
In-Class Exercise: Transaction Log Reader
------------------------------------------
Goal: Read a file of TeleBirr transactions, summarise them by customer
using a dictionary, and handle a missing file gracefully.

Fill in each TODO below. Run the script to test your work:
    python transaction_report.py

When it works, it should:
  1. Read transactions.txt line by line (name,amount per line).
  2. Build a dict mapping each customer to their total spend.
  3. Print each customer and total, sorted highest first.
  4. Wrap the file read in try/except for a missing file.
  5. Write the summary to report.txt.
"""

INPUT_FILE = "transactions.txt"
OUTPUT_FILE = "report.txt"


def read_transactions(filename):
    """
    Read the transactions file and return a dict mapping
    customer name -> total amount spent.

    Each line in the file looks like:
        Abebe,250.00

    TODO 1: Open the file and read it line by line.
    TODO 2: For each line, split it into name and amount.
             (Hint: use line.strip().split(","))
    TODO 3: Convert the amount to a float.
    TODO 4: Add the amount to that customer's running total in a dict.
             (Hint: totals[name] = totals.get(name, 0) + amount)
    TODO 5: Wrap the file-opening code in a try/except block that
             catches FileNotFoundError and prints a friendly message,
             then returns an empty dict instead of crashing.
    """
    totals = {}

    # TODO: implement this function
    pass

    return totals


def print_summary(totals):
    """
    Print each customer and their total, sorted highest total first.

    TODO 6: Sort the dictionary items by amount, descending.
             (Hint: sorted(totals.items(), key=..., reverse=True))
    TODO 7: Print each customer and their total, formatted to 2 decimal
             places, e.g.:
                 Selam: 580.00
                 Abebe: 335.25
    """
    # TODO: implement this function
    pass


def write_report(totals, filename):
    """
    Write the same summary (sorted highest first) to a report file.

    TODO 8: Open the output file for writing.
    TODO 9: Write one line per customer in the same format as the
             printed summary.
    """
    # TODO: implement this function
    pass


def main():
    totals = read_transactions(INPUT_FILE)
    print_summary(totals)
    write_report(totals, OUTPUT_FILE)


if __name__ == "__main__":
    main()
