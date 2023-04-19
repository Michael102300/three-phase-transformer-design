import tkinter as tk
import ttkbootstrap as ttk

from app.layout.layout import Window

if __name__ == "__main__":
    window = ttk.Window('Light')
    window.title('')
    window.minsize(400, 600)
    window.geometry('800x600')
    app = Window(window)
    app.mainloop()
