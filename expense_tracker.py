import csv
import os
from datetime import datetime

FILE = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE) or os.stat(FILE).st_size == 0:
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Category", "Amount", "Date"])


def add_expense(name, category, amount):
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, category, amount, date])


def get_all_expenses():
    expenses = []

    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        pass

    return expenses


def get_total_expense():
    return sum(float(row[2]) for row in get_all_expenses())


def get_category_summary():
    summary = {}

    for row in get_all_expenses():
        category = row[1]
        amount = float(row[2])

        summary[category] = summary.get(category, 0) + amount

    return summary


def get_monthly_summary():
    summary = {}

    for row in get_all_expenses():
        month = row[3][:7]
        amount = float(row[2])

        summary[month] = summary.get(month, 0) + amount

    return summary


def clear_all_expenses():
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Category", "Amount", "Date"])


def delete_last_expense():
    rows = get_all_expenses()

    if not rows:
        return

    rows.pop()

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Category", "Amount", "Date"])
        writer.writerows(rows)