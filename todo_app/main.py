import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json, os

# JSON file path
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

# Add task
def add_task():
    task_text = entry.get().strip()
    if task_text:
        task = {"task": task_text, "done": False}
        tasks.append(task)
        update_list()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty", "Enter a task.")

# Toggle done/pending
def toggle_status():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_list()
        save_tasks()

# Delete selected
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_list()
        save_tasks()
    else:
        messagebox.showinfo("Select Task", "No task selected.")

# Edit selected
def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        current = tasks[index]["task"]
        new_text = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=current)
        if new_text:
            tasks[index]["task"] = new_text.strip()
            update_list()
            save_tasks()

# Clear all tasks
def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        tasks.clear()
        update_list()
        save_tasks()

# Refresh Listbox
def update_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "🔲"
        listbox.insert(tk.END, f"{status} {task['task']}")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.resizable(False, False)

# Task input
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)
entry = tk.Entry(entry_frame, width=30, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)
tk.Button(entry_frame, text="Add", command=add_task).pack(side=tk.LEFT)

# Listbox with scrollbar
list_frame = tk.Frame(root)
list_frame.pack()
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=40, height=15, font=("Arial", 12), yscrollcommand=scrollbar.set)
listbox.pack()
scrollbar.config(command=listbox.yview)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Toggle Done", width=15, command=toggle_status).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Edit Task", width=15, command=edit_task).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Delete Task", width=15, command=delete_task).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Clear All", width=15, command=clear_all).grid(row=1, column=1, padx=5, pady=5)

# Load and show tasks
tasks = load_tasks()
update_list()

root.mainloop()
