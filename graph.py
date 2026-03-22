import csv
import matplotlib.pyplot as plt

file = "expenses.csv"

categories = {}
with open(file, "r") as f:
    reader = csv.reader(f)

    for row in reader:
        category = row[1]
        amount = float(row[2])

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

plt.bar(categories.keys(), categories.values())
plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.show()