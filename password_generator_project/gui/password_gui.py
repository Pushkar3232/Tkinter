import tkinter as tk
from tkinter import messagebox
import pyperclip
from logic.password_logic import generate_password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.length_var = tk.IntVar(value=12)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=False)
        self.password_var = tk.StringVar()

        self._build_gui()

    def _build_gui(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
        tk.Spinbox(frame, from_=4, to=64, textvariable=self.length_var, width=5).grid(row=0, column=1, sticky="w")

        tk.Checkbutton(frame, text="Include Uppercase (A-Z)", variable=self.use_upper).grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(frame, text="Include Lowercase (a-z)", variable=self.use_lower).grid(row=2, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(frame, text="Include Digits (0-9)", variable=self.use_digits).grid(row=3, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(frame, text="Include Symbols (!@#$)", variable=self.use_symbols).grid(row=4, column=0, columnspan=2, sticky="w")

        tk.Button(frame, text="Generate Password", command=self._generate).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Entry(frame, textvariable=self.password_var, font=("Courier", 12), width=30, justify='center').grid(row=6, column=0, columnspan=2, pady=5)

        tk.Button(frame, text="Copy to Clipboard", command=self._copy).grid(row=7, column=0, columnspan=2, pady=5)

    def _generate(self):
        password = generate_password(
            length=self.length_var.get(),
            use_upper=self.use_upper.get(),
            use_lower=self.use_lower.get(),
            use_digits=self.use_digits.get(),
            use_symbols=self.use_symbols.get()
        )
        self.password_var.set(password)

    def _copy(self):
        pwd = self.password_var.get()
        if pwd:
            pyperclip.copy(pwd)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
