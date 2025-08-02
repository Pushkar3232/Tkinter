import tkinter as tk
import random

score = 0
time_left = 30

def move_button():
    if time_left > 0:
        x = random.randint(20, 250)
        y = random.randint(60, 450)
        tap_btn.place(x=x, y=y)

def tap():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    move_button()

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time: {time_left}")
        root.after(1000, countdown)
    else:
        tap_btn.place_forget()
        timer_label.config(text="Time's up!")
        messagebox.showinfo("Game Over", f"Your Score: {score}")

# GUI Setup
root = tk.Tk()
root.title("Tap Game")
root.geometry("300x500")
root.resizable(False, False)

from tkinter import messagebox

title = tk.Label(root, text="Tap the Button!", font=("Arial", 18, "bold"))
title.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

timer_label = tk.Label(root, text="Time: 30", font=("Arial", 14))
timer_label.pack()

tap_btn = tk.Button(root, text="TAP ME!", font=("Arial", 14, "bold"), bg="orange", command=tap)
tap_btn.place(x=100, y=200)

# Start countdown
root.after(1000, countdown)

root.mainloop()
