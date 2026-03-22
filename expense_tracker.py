import csv

file = "expenses.csv"

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            total = 0

            for row in reader:
                print(row[0], "-", row[1])
                total += float(row[1])

            print("Total Expense:", total)

    except:
        print("No expenses recorded yet.")

while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        break