import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import re

class AnalizadorLexicoApp:
    def __init__(self, root):
        # Código del constructor aqui
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2c2c2c", fieldbackground="#2c2c2c", foreground="white", rowheight=25)
        style.configure("Treeview.Heading", background="#3c3c3c", foreground="white", font=("Arial", 12, "bold"))
