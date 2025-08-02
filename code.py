import tkinter as tk
from tkinter import ttk
import time

def progress_bar():
    root = tk.Tk()
    root.title("Update Progress")
    root.geometry("400x120")
    root.resizable(False, False)

    label = tk.Label(root, text="We are performing an internal update...", font=("Arial", 12))
    label.pack(pady=20)

    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=10)

    progress["maximum"] = 100

    def step():
        for i in range(101):
            progress["value"] = i
            root.update_idletasks()
            time.sleep(0.03)
        root.destroy()

    root.after(100, step)
    root.mainloop()

if __name__ == "__main__":
    progress_bar()
