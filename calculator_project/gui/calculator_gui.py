import tkinter as tk
from logic.calculator_logic import evaluate_expression

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        self._create_buttons()

    def _create_buttons(self):
        button_texts = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "C", "+"),
            ("=",)
        ]

        for i, row in enumerate(button_texts):
            for j, char in enumerate(row):
                button = tk.Button(self.root, text=char, padx=20, pady=20, font=("Arial", 14),
                                   command=lambda ch=char: self._on_button_click(ch))
                button.grid(row=i + 1, column=j, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def _on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            self.expression = str(evaluate_expression(self.expression))
        else:
            self.expression += str(char)
        self._update_display()

    def _update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
