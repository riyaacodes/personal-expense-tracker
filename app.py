import tkinter as tk
from tkinter import messagebox

from expense_tracker import (
    initialize_file,
    add_expense,
    get_all_expenses,
    get_total_expense,
    clear_all_expenses,
    delete_last_expense,
)
from graph import show_category_graph, show_insights
from config import BUDGET


initialize_file()


def add_placeholder(entry, text):
    entry.insert(0, text)

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, tk.END)

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, text)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def toggle_other_category(selected):
    if selected == "Other":
        other_category_entry.pack()
        other_category_entry.delete(0, tk.END)
        add_placeholder(other_category_entry, "e.g. Gym / Movies")
    else:
        other_category_entry.pack_forget()


def add_expense_ui():
    name = name_entry.get()
    amount = amount_entry.get()
    
    if category_var.get() == "Other":
        category = other_category_entry.get()
        if not category or category == "e.g. Gym / Movies":
            messagebox.showerror("Error", "Please enter custom category!")
            return
    else:
        category = category_var.get()

    if not name or not category or not amount:
        messagebox.showerror("Error", "All fields required!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be number!")
        return

    add_expense(name, category, amount)
    messagebox.showinfo("Success", "Expense Added!")

    name_entry.delete(0, tk.END)
    add_placeholder(name_entry, "e.g. Pizza")
    amount_entry.delete(0, tk.END)
    add_placeholder(amount_entry, "e.g. 250")


def view_expenses_ui():
    display.delete("1.0", tk.END)

    expenses = get_all_expenses()

    for row in expenses:
        display.insert(tk.END, f"{row[0]} | {row[1]} | ₹{row[2]} | {row[3]}\n")

    total = get_total_expense()
    display.insert(tk.END, f"\nTotal: ₹{total}\n")

    if total > BUDGET:
        display.insert(tk.END, " Budget Exceeded!\n")


def show_insights_ui():
    insights = show_insights()
    display.delete("1.0", tk.END)
    display.insert(tk.END, insights)


def clear_expenses_ui():
    confirm = messagebox.askyesno("Confirm", "Delete all expenses?")
    
    if confirm:
        clear_all_expenses()
        display.delete("1.0", tk.END)
        messagebox.showinfo("Success", "All expenses cleared!")


def delete_last_expense_ui():
    confirm = messagebox.askyesno("Confirm", "Delete last expense entry?")
    
    if confirm:
        delete_last_expense()
        messagebox.showinfo("Success", "Last expense deleted!")


# UI
root = tk.Tk()
root.title("Smart Expense Tracker")
root.geometry("450x500")


# -------- ROW 1 --------
frame1 = tk.Frame(root)
frame1.pack(pady=10)

tk.Label(frame1, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(frame1)
name_entry.grid(row=1, column=0, padx=10)
add_placeholder(name_entry, "e.g. Pizza")

tk.Label(frame1, text="Category").grid(row=0, column=1)

category_var = tk.StringVar()
category_var.set("Food")

category_options = ["Food", "Travel", "Shopping", "Entertainment", "Bills", "Health", "Other"]

category_menu = tk.OptionMenu(frame1, category_var, *category_options, command=toggle_other_category)
category_menu.grid(row=1, column=1, padx=10)

for widget in frame1.winfo_children():
    widget.grid_configure(pady=5)


# -------- ROW 2 --------
frame2 = tk.Frame(root)
frame2.pack(pady=10)

tk.Label(frame2, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(frame2)
amount_entry.grid(row=1, column=0, padx=10)
add_placeholder(amount_entry, "e.g. 250")

tk.Button(frame2, text="Add Expense", command=add_expense_ui)\
    .grid(row=1, column=1, padx=10)

for widget in frame2.winfo_children():
    widget.grid_configure(pady=5)


# -------- ROW 3 --------
frame3 = tk.Frame(root)
frame3.pack(pady=10)

tk.Button(frame3, text="View Expenses", command=view_expenses_ui)\
    .grid(row=0, column=0, padx=10)

tk.Button(frame3, text="Show Graph", command=show_category_graph)\
    .grid(row=0, column=1, padx=10)


# -------- ROW 4 --------
frame4 = tk.Frame(root)
frame4.pack(pady=10)

tk.Button(frame4, text="Show Insights", command=show_insights_ui)\
    .grid(row=0, column=0, padx=10)

tk.Button(frame4, text="Delete Last", command=delete_last_expense_ui)\
    .grid(row=0, column=1, padx=10)


# -------- ROW 5 --------
frame5 = tk.Frame(root)
frame5.pack(pady=10)

tk.Button(frame5, text="Clear All Data", command=clear_expenses_ui)\
    .grid(row=0, column=0, columnspan=2, padx=10)


# -------- DISPLAY --------
display = tk.Text(root, height=15, width=50)
display.pack(pady=10)

# Entry for custom category (hidden initially)
other_category_entry = tk.Entry(root)


root.mainloop()