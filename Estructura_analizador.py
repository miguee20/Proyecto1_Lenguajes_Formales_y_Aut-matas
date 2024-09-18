import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class AnalizadorLexicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Analizador Léxico")
        self.root.geometry("900x500")
        self.root.config(bg="#2c2c2c")

        left_frame = tk.Frame(self.root, bg="#2c2c2c")
        left_frame.pack(side="left", padx=10, pady=10)

        right_frame = tk.Frame(self.root, bg="#2c2c2c")
        right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.lbl_titulo = tk.Label(left_frame, text="Simulador de Analizador Léxico", font=("Arial", 16, "bold"), bg="#2c2c2c", fg="#ffffff")
        self.lbl_titulo.pack(pady=10)

        self.btn_abrir = tk.Button(left_frame, text="Abrir archivo", command=self.abrir_archivo, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        self.btn_abrir.pack(pady=5)

        self.btn_guardar = tk.Button(left_frame, text="Guardar archivo", command=self.guardar_archivo, bg="#FF9800", fg="white", font=("Arial", 12), width=20)
        self.btn_guardar.pack(pady=5)

        self.btn_analizar = tk.Button(left_frame, text="Analizar", command=self.analizar, bg="#2196F3", fg="white", font=("Arial", 12), width=20)
        self.btn_analizar.pack(pady=5)

        self.btn_limpiar = tk.Button(left_frame, text="Limpiar texto", command=self.limpiar_texto, bg="#E91E63", fg="white", font=("Arial", 12), width=20)
        self.btn_limpiar.pack(pady=5)

        self.textbox = tk.Text(left_frame, height=20, width=40, bg="#3c3c3c", fg="#ffffff", font=("Arial", 10), relief=tk.GROOVE, bd=2)
        self.textbox.pack(pady=10)

        self.tree = ttk.Treeview(right_frame, columns=("Token", "Tipo", "Cantidad"), show="headings", height=20)
        self.tree.heading("Token", text="Token")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.column("Token", anchor="center", width=200)
        self.tree.column("Tipo", anchor="center", width=150)
        self.tree.column("Cantidad", anchor="center", width=100)
        self.tree.pack(fill="both", expand=True)
