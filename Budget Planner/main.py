import tkinter as tk
from tkinter import ttk, messagebox
import json, os

FILE = "budget.json"

def load_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_data():
    json.dump(budget, open(FILE, "w"))

def add_entry():
    desc = desc_var.get().strip()
    amount = amount_var.get().strip()
    entry_type = type_var.get()

    if desc and amount.replace('.', '', 1).isdigit():
        budget.append({"desc": desc, "amount": float(amount), "type": entry_type})
        save_data()
        refresh()
        update_balance()
        desc_var.set("")
        amount_var.set("")
    else:
        messagebox.showwarning("Input", "Enter valid description and amount.")

def delete_entry():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        budget.pop(idx)
        save_data()
        refresh()
        update_balance()

def refresh():
    tree.delete(*tree.get_children())
    for i, b in enumerate(budget):
        tree.insert("", "end", iid=i, values=(b["desc"], b["amount"], b["type"]))

def update_balance():
    income = sum(b["amount"] for b in budget if b["type"] == "Income")
    expense = sum(b["amount"] for b in budget if b["type"] == "Expense")
    balance = income - expense
    balance_label.config(text=f"Balance: ₹{balance:.2f}")

root = tk.Tk()
root.title("Budget Planner")
root.geometry("500x500")

desc_var, amount_var = tk.StringVar(), tk.StringVar()
type_var = tk.StringVar(value="Income")
budget = load_data()

tk.Label(root, text="Description:").pack()
tk.Entry(root, textvariable=desc_var).pack()
tk.Label(root, text="Amount:").pack()
tk.Entry(root, textvariable=amount_var).pack()

frame = tk.Frame(root)
frame.pack(pady=5)
tk.Radiobutton(frame, text="Income", variable=type_var, value="Income").pack(side=tk.LEFT)
tk.Radiobutton(frame, text="Expense", variable=type_var, value="Expense").pack(side=tk.LEFT)

tk.Button(root, text="Add Entry", command=add_entry).pack(pady=5)

tree = ttk.Treeview(root, columns=("Description", "Amount", "Type"), show="headings")
for col in ("Description", "Amount", "Type"):
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Button(root, text="Delete Entry", command=delete_entry).pack(pady=5)

balance_label = tk.Label(root, text="Balance: ₹0.00", font=("Arial", 14))
balance_label.pack(pady=10)

refresh()
update_balance()
root.mainloop()
