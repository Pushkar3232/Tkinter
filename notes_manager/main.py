import tkinter as tk
from tkinter import messagebox, ttk
import json, os

FILE = "notes.json"

# Load notes
def load_notes():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save notes
def save_notes():
    with open(FILE, "w") as f:
        json.dump(notes, f)

# Add or Update note
def save_note():
    title = title_var.get().strip()
    content = content_box.get("1.0", tk.END).strip()

    if title and content:
        for note in notes:
            if note["title"] == title:
                note["content"] = content
                break
        else:
            notes.append({"title": title, "content": content})
        save_notes()
        update_list()
        clear_fields()
    else:
        messagebox.showwarning("Input", "Both title and content required.")

# Show selected note
def show_note(event):
    selected = tree.selection()
    if selected:
        index = int(selected[0])
        title_var.set(notes[index]["title"])
        content_box.delete("1.0", tk.END)
        content_box.insert(tk.END, notes[index]["content"])

# Delete note
def delete_note():
    selected = tree.selection()
    if selected:
        index = int(selected[0])
        notes.pop(index)
        save_notes()
        update_list()
        clear_fields()

# Clear input fields
def clear_fields():
    title_var.set("")
    content_box.delete("1.0", tk.END)

# Update note list
def update_list():
    tree.delete(*tree.get_children())
    for i, note in enumerate(notes):
        tree.insert("", "end", iid=i, values=(note["title"],))

# GUI setup
root = tk.Tk()
root.title("Notes Manager")
root.geometry("500x500")

title_var = tk.StringVar()
notes = load_notes()

tk.Label(root, text="Note Title:").pack()
tk.Entry(root, textvariable=title_var, width=50).pack(pady=2)

tk.Label(root, text="Note Content:").pack()
content_box = tk.Text(root, height=5, width=50)
content_box.pack(pady=2)

tk.Button(root, text="Save / Update Note", command=save_note).pack(pady=4)

tree = ttk.Treeview(root, columns=("Title",), show="headings", height=10)
tree.heading("Title", text="Saved Notes")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", show_note)

tk.Button(root, text="Delete Note", command=delete_note).pack(pady=4)

update_list()
root.mainloop()
