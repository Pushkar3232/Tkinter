import tkinter as tk
from tkinter import messagebox
import csv
import os

FILE_NAME = "expenses.csv"

# Save expense to CSV
def save_expense():
    amount = amount_entry.get().strip()
    category = category_entry.get().strip()
    note = note_entry.get().strip()

    if not amount or not category:
        messagebox.showerror("Error", "Please fill amount and category!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, note])

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)
    load_expenses()

# Load expenses from CSV
def load_expenses():
    expenses_list.delete(0, tk.END)
    total = 0
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    expenses_list.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")
                    total += float(row[0])
    total_label.config(text=f"Total: ₹{total}")

# Delete selected expense
def delete_expense():
    selected = expenses_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select an expense to delete!")
        return

    index = selected[0]
    expenses = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    expenses.pop(index)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

    load_expenses()

# Tkinter UI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("350x450")

# Input fields
tk.Label(root, text="Amount (₹):").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Note:").pack()
note_entry = tk.Entry(root)
note_entry.pack()

tk.Button(root, text="Add Expense", command=save_expense, bg="lightgreen").pack(pady=5)

# Expense list
expenses_list = tk.Listbox(root, width=40, height=10)
expenses_list.pack(pady=10)

# Buttons
tk.Button(root, text="Delete Selected", command=delete_expense, bg="tomato").pack(pady=5)

# Total label
total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

load_expenses()

root.mainloop()
