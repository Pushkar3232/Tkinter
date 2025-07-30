import tkinter as tk
from tkinter import ttk, messagebox
import json, os

FILE = "workouts.json"

def load_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_data():
    json.dump(workouts, open(FILE, "w"))

def add_workout():
    name = name_var.get().strip()
    sets = sets_var.get().strip()
    reps = reps_var.get().strip()

    if name and sets.isdigit() and reps.isdigit():
        workouts.append({"name": name, "sets": int(sets), "reps": int(reps)})
        save_data()
        refresh()
        name_var.set("")
        sets_var.set("")
        reps_var.set("")
    else:
        messagebox.showwarning("Input", "Enter valid exercise, sets and reps.")

def delete_workout():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        workouts.pop(idx)
        save_data()
        refresh()

def refresh():
    tree.delete(*tree.get_children())
    for i, w in enumerate(workouts):
        tree.insert("", "end", iid=i, values=(w["name"], w["sets"], w["reps"]))

root = tk.Tk()
root.title("Workout Tracker")
root.geometry("400x400")

name_var, sets_var, reps_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
workouts = load_data()

tk.Label(root, text="Exercise Name:").pack()
tk.Entry(root, textvariable=name_var).pack()
tk.Label(root, text="Sets:").pack()
tk.Entry(root, textvariable=sets_var).pack()
tk.Label(root, text="Reps:").pack()
tk.Entry(root, textvariable=reps_var).pack()

tk.Button(root, text="Add Workout", command=add_workout).pack(pady=5)

tree = ttk.Treeview(root, columns=("Exercise", "Sets", "Reps"), show="headings")
tree.heading("Exercise", text="Exercise")
tree.heading("Sets", text="Sets")
tree.heading("Reps", text="Reps")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Button(root, text="Delete Workout", command=delete_workout).pack(pady=5)

refresh()
root.mainloop()
