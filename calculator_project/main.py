import tkinter as tk
from gui.calculator_gui import Calculator

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
