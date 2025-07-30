import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json, os

FILE = "students.json"

# Load data
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_data():
    with open(FILE, "w") as f:
        json.dump(students, f)

# Add student
def add_student():
    roll = roll_var.get().strip()
    name = name_var.get().strip()
    marks = marks_var.get().strip()

    if roll and name and marks.isdigit():
        # check for duplicate roll no
        if any(s["roll"] == roll for s in students):
            messagebox.showwarning("Duplicate", "Roll number already exists.")
            return
        students.append({"roll": roll, "name": name, "marks": int(marks)})
        save_data()
        refresh_table()
        roll_var.set("")
        name_var.set("")
        marks_var.set("")
    else:
        messagebox.showwarning("Invalid", "Fill all fields correctly.")

# Edit selected student
def edit_student():
    selected = tree.selection()
    if selected:
        idx = tree.index(selected)
        s = students[idx]

        new_name = simpledialog.askstring("Edit Name", "Name:", initialvalue=s["name"])
        new_marks = simpledialog.askstring("Edit Marks", "Marks:", initialvalue=str(s["marks"]))

        if new_name and new_marks.isdigit():
            students[idx]["name"] = new_name
            students[idx]["marks"] = int(new_marks)
            save_data()
            refresh_table()

# Delete student
def delete_student():
    selected = tree.selection()
    if selected:
        idx = tree.index(selected)
        students.pop(idx)
        save_data()
        refresh_table()

# Refresh table
def refresh_table():
    tree.delete(*tree.get_children())
    for s in students:
        tree.insert("", tk.END, values=(s["roll"], s["name"], s["marks"]))

# GUI
root = tk.Tk()
root.title("Student Management")
root.geometry("500x500")
root.resizable(False, False)

# Form
form = tk.Frame(root)
form.pack(pady=10)

roll_var = tk.StringVar()
name_var = tk.StringVar()
marks_var = tk.StringVar()

tk.Label(form, text="Roll No:").grid(row=0, column=0)
tk.Entry(form, textvariable=roll_var).grid(row=0, column=1)

tk.Label(form, text="Name:").grid(row=1, column=0)
tk.Entry(form, textvariable=name_var).grid(row=1, column=1)

tk.Label(form, text="Marks:").grid(row=2, column=0)
tk.Entry(form, textvariable=marks_var).grid(row=2, column=1)

tk.Button(form, text="Add Student", command=add_student).grid(row=3, columnspan=2, pady=5)

# Table
tree = ttk.Treeview(root, columns=("Roll", "Name", "Marks"), show="headings")
tree.heading("Roll", text="Roll No")
tree.heading("Name", text="Name")
tree.heading("Marks", text="Marks")
tree.pack(pady=10, fill=tk.X, padx=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="Edit", width=15, command=edit_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", width=15, command=delete_student).grid(row=0, column=1, padx=5)

# Load and show
students = load_data()
refresh_table()

root.mainloop()
