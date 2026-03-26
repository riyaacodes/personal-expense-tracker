import matplotlib.pyplot as plt
from expense_tracker import get_category_summary


def show_category_graph():
    categories = get_category_summary()

    if not categories:
        print("No data to display.")
        return

    plt.figure()
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()


def show_insights():
    categories = get_category_summary()

    if not categories:
        return "No data available."

    total = sum(categories.values())
    max_cat = max(categories, key=categories.get)

    insight = f"Top spending category: {max_cat}\n"
    insight += f"Spent ₹{categories[max_cat]} on {max_cat}\n"

    for cat, amt in categories.items():
        percent = (amt / total) * 100
        insight += f"{cat}: {percent:.1f}%\n"

    return insight