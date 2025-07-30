import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json, os

FILE = "books.json"

# Load books
def load_books():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save books
def save_books():
    with open(FILE, "w") as f:
        json.dump(books, f)

# Add book
def add_book():
    title = title_var.get().strip()
    author = author_var.get().strip()
    isbn = isbn_var.get().strip()

    if title and author and isbn:
        books.append({"title": title, "author": author, "isbn": isbn})
        save_books()
        update_table()
        clear_fields()
    else:
        messagebox.showwarning("Required", "Fill all fields.")

# Clear input
def clear_fields():
    title_var.set("")
    author_var.set("")
    isbn_var.set("")

# Edit book
def edit_book():
    selected = tree.selection()
    if selected:
        idx = tree.index(selected)
        book = books[idx]

        new_title = simpledialog.askstring("Edit Title", "Title:", initialvalue=book["title"])
        new_author = simpledialog.askstring("Edit Author", "Author:", initialvalue=book["author"])
        new_isbn = simpledialog.askstring("Edit ISBN", "ISBN:", initialvalue=book["isbn"])

        if new_title and new_author and new_isbn:
            books[idx] = {"title": new_title, "author": new_author, "isbn": new_isbn}
            save_books()
            update_table()

# Delete book
def delete_book():
    selected = tree.selection()
    if selected:
        idx = tree.index(selected)
        books.pop(idx)
        save_books()
        update_table()

# Update table
def update_table():
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert("", tk.END, values=(book["title"], book["author"], book["isbn"]))

# GUI
root = tk.Tk()
root.title("Book Library")
root.geometry("500x500")
root.resizable(False, False)

# Input form
form = tk.Frame(root)
form.pack(pady=10)

title_var = tk.StringVar()
author_var = tk.StringVar()
isbn_var = tk.StringVar()

tk.Label(form, text="Title:").grid(row=0, column=0)
tk.Entry(form, textvariable=title_var).grid(row=0, column=1)

tk.Label(form, text="Author:").grid(row=1, column=0)
tk.Entry(form, textvariable=author_var).grid(row=1, column=1)

tk.Label(form, text="ISBN:").grid(row=2, column=0)
tk.Entry(form, textvariable=isbn_var).grid(row=2, column=1)

tk.Button(form, text="Add Book", command=add_book).grid(row=3, columnspan=2, pady=5)

# Book table
tree = ttk.Treeview(root, columns=("Title", "Author", "ISBN"), show="headings")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("ISBN", text="ISBN")
tree.pack(pady=10, fill=tk.X, padx=10)

# Action buttons
btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="Edit", width=15, command=edit_book).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", width=15, command=delete_book).grid(row=0, column=1, padx=5)

# Load data
books = load_books()
update_table()

root.mainloop()
