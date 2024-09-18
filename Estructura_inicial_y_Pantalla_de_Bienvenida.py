import tkinter as tk

class PantallaBienvenida:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico - LF&A")
        self.root.geometry("900x500")
        self.root.config(bg="#2c2c2c")

        self.lbl_titulo1 = tk.Label(root, text="Lenguajes Formales y Autómatas", font=("Arial", 35, "italic", "bold"), bg="#2c2c2c", fg="white")
        self.lbl_titulo1.pack(pady=50)

        self.lbl_titulo = tk.Label(root, text="Proyecto #1 - Analizador Léxico", font=("Arial", 15, "bold"), bg="#2c2c2c", fg="white")
        self.lbl_titulo.pack(pady=50)

        self.lbl_creadores = tk.Label(root, text="Creado por:\nMiguel Salguero - 1626923\nJulio Cáceres - 1549223", font=("Arial", 12), bg="#2c2c2c", fg="white")
        self.lbl_creadores.pack(pady=20)

        self.btn_continuar = tk.Button(root, text="Iniciar", command=self.cargar_aplicacion, bg="#4CAF50", fg="white", font=("Arial", 15), width=20)
        self.btn_continuar.pack(pady=20)

    def cargar_aplicacion(self):
        self.root.destroy()
        root = tk.Tk()
        app = AnalizadorLexicoApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaBienvenida(root)
    root.mainloop()
