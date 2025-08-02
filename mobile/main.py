import tkinter as tk
from tkinter import messagebox
import os

# Function to save note
def save_note():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        with open("my_note.txt", "w", encoding="utf-8") as file:
            file.write(content)
        messagebox.showinfo("Saved", "Note saved successfully!")
    else:
        messagebox.showwarning("Empty", "Note is empty!")

# Function to load note
def load_note():
    if os.path.exists("my_note.txt"):
        with open("my_note.txt", "r", encoding="utf-8") as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)
    else:
        messagebox.showerror("Not Found", "No saved note found!")

# GUI setup
root = tk.Tk()
root.title("My Notes")
root.geometry("300x500")  # Good size for Pydroid app
root.configure(bg="#f0f0f0")

# Heading
title = tk.Label(root, text="Notes App", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Text input area
text_area = tk.Text(root, font=("Arial", 14), wrap="word", height=20, padx=10, pady=10)
text_area.pack(padx=10, pady=10, fill="both", expand=True)

# Save button
save_btn = tk.Button(root, text="Save", font=("Arial", 14), command=save_note, bg="#4CAF50", fg="white")
save_btn.pack(pady=5, ipadx=10, ipady=5)

# Load button
load_btn = tk.Button(root, text="Load", font=("Arial", 14), command=load_note, bg="#2196F3", fg="white")
load_btn.pack(pady=5, ipadx=10, ipady=5)

# Start app
root.mainloop()
