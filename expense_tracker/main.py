import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json, os

FILE = "expenses.json"

# Load expenses
def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save expenses
def save_expenses():
    with open(FILE, "w") as f:
        json.dump(expenses, f)

# Add expense
def add_expense():
    amt = amount_var.get().strip()
    cat = category_var.get()
    note = note_var.get().strip()

    if amt.isdigit() and cat:
        expense = {"amount": int(amt), "category": cat, "note": note}
        expenses.append(expense)
        save_expenses()
        update_table()
        update_total()
        amount_var.set("")
        note_var.set("")
    else:
        messagebox.showwarning("Invalid", "Enter valid amount and category.")

# Delete selected expense
def delete_expense():
    selected = tree.selection()
    if selected:
        idx = tree.index(selected)
        expenses.pop(idx)
        save_expenses()
        update_table()
        update_total()

# Edit selected expense
def edit_expense():
    selected = tree.selection()
    if selected:
        idx = tree.index(selected)
        exp = expenses[idx]

        new_amt = simpledialog.askstring("Amount", "Enter new amount:", initialvalue=str(exp["amount"]))
        new_cat = simpledialog.askstring("Category", "Enter new category:", initialvalue=exp["category"])
        new_note = simpledialog.askstring("Note", "Edit note:", initialvalue=exp["note"])

        if new_amt.isdigit() and new_cat:
            expenses[idx] = {"amount": int(new_amt), "category": new_cat, "note": new_note or ""}
            save_expenses()
            update_table()
            update_total()

# Update table
def update_table():
    tree.delete(*tree.get_children())
    for exp in expenses:
        tree.insert("", tk.END, values=(exp["amount"], exp["category"], exp["note"]))

# Update total
def update_total():
    total = sum(exp["amount"] for exp in expenses)
    total_label.config(text=f"Total: ₹ {total}")

# GUI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")
root.resizable(False, False)

# Input form
form = tk.Frame(root)
form.pack(pady=10)

amount_var = tk.StringVar()
category_var = tk.StringVar()
note_var = tk.StringVar()

tk.Label(form, text="Amount:").grid(row=0, column=0)
tk.Entry(form, textvariable=amount_var).grid(row=0, column=1)

tk.Label(form, text="Category:").grid(row=1, column=0)
cat_menu = ttk.Combobox(form, textvariable=category_var, values=["Food", "Travel", "Bills", "Other"])
cat_menu.grid(row=1, column=1)

tk.Label(form, text="Note:").grid(row=2, column=0)
tk.Entry(form, textvariable=note_var).grid(row=2, column=1)

tk.Button(form, text="Add Expense", command=add_expense).grid(row=3, columnspan=2, pady=5)

# Expense table
tree = ttk.Treeview(root, columns=("Amount", "Category", "Note"), show="headings")
tree.heading("Amount", text="Amount")
tree.heading("Category", text="Category")
tree.heading("Note", text="Note")
tree.pack(pady=10, fill=tk.X, padx=10)

# Buttons
btns = tk.Frame(root)
btns.pack()
tk.Button(btns, text="Edit", width=15, command=edit_expense).grid(row=0, column=0, padx=5)
tk.Button(btns, text="Delete", width=15, command=delete_expense).grid(row=0, column=1, padx=5)

# Total label
total_label = tk.Label(root, text="Total: ₹ 0", font=("Arial", 14))
total_label.pack(pady=10)

# Load and show
expenses = load_expenses()
update_table()
update_total()

root.mainloop()
