import tkinter as tk
from tkinter import messagebox, ttk
import json, os
from datetime import date

FILE = "moods.json"

# Load data
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save data
def save_data():
    with open(FILE, "w") as f:
        json.dump(moods, f)

# Submit mood
def submit_mood():
    mood = mood_var.get()
    note = note_entry.get("1.0", tk.END).strip()
    today = str(date.today())

    if mood:
        moods[today] = {"mood": mood, "note": note}
        save_data()
        update_history()
        messagebox.showinfo("Saved", f"Mood for {today} saved!")
    else:
        messagebox.showwarning("Select Mood", "Please select your mood.")

# Show mood history
def update_history():
    history_list.delete(*history_list.get_children())
    for d, m in sorted(moods.items(), reverse=True):
        history_list.insert("", tk.END, values=(d, m["mood"], m["note"]))

# GUI
root = tk.Tk()
root.title("Daily Mood Tracker")
root.geometry("500x500")
root.resizable(False, False)

mood_var = tk.StringVar()
moods = load_data()

# Mood selection
tk.Label(root, text="How are you feeling today?", font=("Arial", 12)).pack(pady=5)

mood_frame = tk.Frame(root)
mood_frame.pack(pady=5)

for m in ["😊 Happy", "😐 Okay", "😢 Sad", "😡 Angry", "😴 Tired"]:
    tk.Radiobutton(mood_frame, text=m, variable=mood_var, value=m).pack(anchor="w")

# Note
tk.Label(root, text="Optional Note:").pack()
note_entry = tk.Text(root, height=3, width=50)
note_entry.pack(pady=5)

# Submit
tk.Button(root, text="Submit Mood", command=submit_mood).pack(pady=10)

# Mood History
tk.Label(root, text="Mood History", font=("Arial", 12, "bold")).pack(pady=5)
history_list = ttk.Treeview(root, columns=("Date", "Mood", "Note"), show="headings")
history_list.heading("Date", text="Date")
history_list.heading("Mood", text="Mood")
history_list.heading("Note", text="Note")
history_list.pack(fill=tk.BOTH, expand=True, padx=10)

update_history()

root.mainloop()
