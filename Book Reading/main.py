import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json, os

FILE = "reading.json"

def load_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_data():
    json.dump(books, open(FILE, "w"))

def add_book():
    title = title_var.get().strip()
    page = page_var.get().strip()
    if title and page.isdigit():
        books.append({"title": title, "page": int(page)})
        save_data()
        refresh()
        title_var.set("")
        page_var.set("")
    else:
        messagebox.showwarning("Input", "Enter valid title and page.")

def update_progress():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        new_page = simpledialog.askstring("Update Page", "Enter new page number:")
        if new_page and new_page.isdigit():
            books[idx]["page"] = int(new_page)
            save_data()
            refresh()

def delete_book():
    selected = tree.selection()
    if selected:
        idx = int(selected[0])
        books.pop(idx)
        save_data()
        refresh()

def refresh():
    tree.delete(*tree.get_children())
    for i, b in enumerate(books):
        tree.insert("", "end", iid=i, values=(b["title"], b["page"]))

root = tk.Tk()
root.title("Book Reading Tracker")
root.geometry("400x400")

title_var, page_var = tk.StringVar(), tk.StringVar()
books = load_data()

tk.Label(root, text="Book Title:").pack()
tk.Entry(root, textvariable=title_var).pack()
tk.Label(root, text="Current Page:").pack()
tk.Entry(root, textvariable=page_var).pack()

tk.Button(root, text="Add Book", command=add_book).pack(pady=5)

tree = ttk.Treeview(root, columns=("Title", "Page"), show="headings")
tree.heading("Title", text="Book Title")
tree.heading("Page", text="Current Page")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="Update Progress", command=update_progress).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_book).grid(row=0, column=1, padx=5)

refresh()
root.mainloop()
