import tkinter as tk
from gui.password_gui import PasswordGeneratorApp

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
