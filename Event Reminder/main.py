import tkinter as tk
from tkinter import ttk, messagebox
import json, os

FILE = "events.json"

def load_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_data():
    json.dump(events, open(FILE, "w"))

def add_event():
    name = name_var.get().strip()
    date = date_var.get().strip()
    if name and date:
        events.append({"name": name, "date": date})
        save_data()
        refresh()
        name_var.set("")
        date_var.set("")
    else:
        messagebox.showwarning("Input", "Enter event name and date.")

def delete_event():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        events.pop(idx)
        save_data()
        refresh()

def refresh():
    tree.delete(*tree.get_children())
    for i, e in enumerate(events):
        tree.insert("", "end", iid=i, values=(e["name"], e["date"]))

root = tk.Tk()
root.title("Event Reminder")
root.geometry("400x400")

name_var, date_var = tk.StringVar(), tk.StringVar()
events = load_data()

tk.Label(root, text="Event Name:").pack()
tk.Entry(root, textvariable=name_var).pack()
tk.Label(root, text="Event Date (YYYY-MM-DD):").pack()
tk.Entry(root, textvariable=date_var).pack()

tk.Button(root, text="Add Event", command=add_event).pack(pady=5)

tree = ttk.Treeview(root, columns=("Event", "Date"), show="headings")
tree.heading("Event", text="Event Name")
tree.heading("Date", text="Date")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Button(root, text="Delete Event", command=delete_event).pack(pady=5)

refresh()
root.mainloop()
