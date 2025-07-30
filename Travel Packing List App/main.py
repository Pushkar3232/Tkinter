import tkinter as tk
from tkinter import ttk, messagebox
import json, os

FILE = "packing.json"

def load_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_data():
    json.dump(items, open(FILE, "w"))

def add_item():
    item = item_var.get().strip()
    if item:
        items.append({"item": item, "status": "Not Packed"})
        save_data()
        refresh()
        item_var.set("")
    else:
        messagebox.showwarning("Input", "Enter an item name.")

def mark_packed():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        items[idx]["status"] = "✅ Packed"
        save_data()
        refresh()

def delete_item():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        items.pop(idx)
        save_data()
        refresh()

def refresh():
    tree.delete(*tree.get_children())
    for i, it in enumerate(items):
        tree.insert("", "end", iid=i, values=(it["item"], it["status"]))

root = tk.Tk()
root.title("Travel Packing List")
root.geometry("400x400")

item_var = tk.StringVar()
items = load_data()

tk.Label(root, text="Enter Item:").pack()
tk.Entry(root, textvariable=item_var).pack(pady=5)
tk.Button(root, text="Add Item", command=add_item).pack(pady=5)

tree = ttk.Treeview(root, columns=("Item", "Status"), show="headings")
tree.heading("Item", text="Item")
tree.heading("Status", text="Status")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Button(root, text="Mark as Packed", command=mark_packed).pack(pady=3)
tk.Button(root, text="Delete Item", command=delete_item).pack(pady=3)

refresh()
root.mainloop()
