import tkinter as tk
from tkinter import ttk, messagebox
import json, os

FILE = "habits.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data():
    with open(FILE, "w") as f:
        json.dump(habits, f)

def add_habit():
    habit = habit_var.get().strip()
    if habit:
        habits.append({"habit": habit, "status": "Not Done"})
        save_data()
        refresh_table()
        habit_var.set("")
    else:
        messagebox.showwarning("Input", "Enter habit name.")

def mark_done():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        habits[idx]["status"] = "✅ Done"
        save_data()
        refresh_table()
    else:
        messagebox.showwarning("Select", "Select a habit to mark done.")

def delete_habit():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        habits.pop(idx)
        save_data()
        refresh_table()

def refresh_table():
    tree.delete(*tree.get_children())
    for i, h in enumerate(habits):
        tree.insert("", "end", iid=i, values=(h["habit"], h["status"]))

root = tk.Tk()
root.title("Habit Tracker")
root.geometry("400x400")

habit_var = tk.StringVar()
habits = load_data()

tk.Label(root, text="Enter Habit:").pack()
tk.Entry(root, textvariable=habit_var).pack(pady=5)
tk.Button(root, text="Add Habit", command=add_habit).pack(pady=5)

tree = ttk.Treeview(root, columns=("Habit", "Status"), show="headings")
tree.heading("Habit", text="Habit")
tree.heading("Status", text="Status")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=3)
tk.Button(root, text="Delete Habit", command=delete_habit).pack(pady=3)

refresh_table()
root.mainloop()
