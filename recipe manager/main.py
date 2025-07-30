import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json, os

FILE = "recipes.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_data():
    with open(FILE, "w") as f:
        json.dump(recipes, f)

def add_recipe():
    name = name_var.get().strip()
    ingredients = ingredients_box.get("1.0", tk.END).strip()
    steps = steps_box.get("1.0", tk.END).strip()

    if name and ingredients and steps:
        recipes.append({"name": name, "ingredients": ingredients, "steps": steps})
        save_data()
        refresh_list()
        clear_fields()
    else:
        messagebox.showwarning("Input", "Fill all fields.")

def show_recipe(event):
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        r = recipes[idx]
        name_var.set(r["name"])
        ingredients_box.delete("1.0", tk.END)
        steps_box.delete("1.0", tk.END)
        ingredients_box.insert(tk.END, r["ingredients"])
        steps_box.insert(tk.END, r["steps"])

def delete_recipe():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        recipes.pop(idx)
        save_data()
        refresh_list()
        clear_fields()

def clear_fields():
    name_var.set("")
    ingredients_box.delete("1.0", tk.END)
    steps_box.delete("1.0", tk.END)

def refresh_list():
    tree.delete(*tree.get_children())
    for i, r in enumerate(recipes):
        tree.insert("", "end", iid=i, values=(r["name"],))

root = tk.Tk()
root.title("Recipe Manager")
root.geometry("500x500")

name_var = tk.StringVar()
recipes = load_data()

tk.Label(root, text="Recipe Name:").pack()
tk.Entry(root, textvariable=name_var, width=50).pack(pady=2)

tk.Label(root, text="Ingredients:").pack()
ingredients_box = tk.Text(root, height=5, width=50)
ingredients_box.pack(pady=2)

tk.Label(root, text="Steps:").pack()
steps_box = tk.Text(root, height=5, width=50)
steps_box.pack(pady=2)

tk.Button(root, text="Add / Update Recipe", command=add_recipe).pack(pady=4)

tree = ttk.Treeview(root, columns=("Name",), show="headings")
tree.heading("Name", text="Recipe Name")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", show_recipe)

tk.Button(root, text="Delete Recipe", command=delete_recipe).pack(pady=4)

refresh_list()
root.mainloop()
