#Miguel Salguero
#Julio Caceres
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import re

# Diccionario con los tokens en base a la tabla
tokens = {
    'Palabras Reservadas': ['entero', 'decimal', 'booleano', 'cadena', 'si', 'sino', 'mientras', 'hacer', 'verdadero', 'falso'],
    'Operadores': ['+', '-', '*', '/', '%', '=', '==', '<', '>', '>=', '<='],
    'Signos': ['(', ')', '{', '}', '"', ';'],
    'Numeros': r'\d+',
    'Identificadores': r'[a-zA-Z_][a-zA-Z0-9_]*'
}

# Clase principal del analizador
class AnalizadorLexicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Analizador Léxico")
        self.root.geometry("900x500")
        self.root.config(bg="#2c2c2c")

        # Frame para organizar el área de texto y botones a la izquierda
        left_frame = tk.Frame(self.root, bg="#2c2c2c")
        left_frame.pack(side="left", padx=10, pady=10)

        # Frame para la tabla a la derecha
        right_frame = tk.Frame(self.root, bg="#2c2c2c")
        right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        # Etiqueta de título
        self.lbl_titulo = tk.Label(left_frame, text="Simulador de Analizador Léxico", font=("Arial", 16, "bold"), bg="#2c2c2c", fg="#ffffff")
        self.lbl_titulo.pack(pady=10)

        # Botón para abrir archivo
        self.btn_abrir = tk.Button(left_frame, text="Abrir archivo", command=self.abrir_archivo, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        self.btn_abrir.pack(pady=5)

        # Botón para guardar archivo
        self.btn_guardar = tk.Button(left_frame, text="Guardar archivo", command=self.guardar_archivo, bg="#FF9800", fg="white", font=("Arial", 12), width=20)
        self.btn_guardar.pack(pady=5)

        # Botón para analizar
        self.btn_analizar = tk.Button(left_frame, text="Analizar", command=self.analizar, bg="#2196F3", fg="white", font=("Arial", 12), width=20)
        self.btn_analizar.pack(pady=5)

        # Botón para limpiar el texto
        self.btn_limpiar = tk.Button(left_frame, text="Limpiar texto", command=self.limpiar_texto, bg="#E91E63", fg="white", font=("Arial", 12), width=20)
        self.btn_limpiar.pack(pady=5)

        # Caja de texto para mostrar el contenido del archivo
        self.textbox = tk.Text(left_frame, height=20, width=40, bg="#3c3c3c", fg="#ffffff", font=("Arial", 10), relief=tk.GROOVE, bd=2)
        self.textbox.pack(pady=10)

        # Treeview para mostrar los resultados en formato de tabla (tabla del lado derecho)
        self.tree = ttk.Treeview(right_frame, columns=("Token", "Tipo", "Cantidad"), show="headings", height=20)
        self.tree.heading("Token", text="Token")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.column("Token", anchor="center", width=200)
        self.tree.column("Tipo", anchor="center", width=150)
        self.tree.column("Cantidad", anchor="center", width=100)
        self.tree.pack(fill="both", expand=True)

        # Estilo para Treeview (fondo oscuro y texto claro)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2c2c2c", fieldbackground="#2c2c2c", foreground="white", rowheight=25)
        style.configure("Treeview.Heading", background="#3c3c3c", foreground="white", font=("Arial", 12, "bold"))

    # Funcion para abrir archivos txt
    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, 'r') as file:
                contenido = file.read()
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, contenido)

    # Funcion para guardar el contenido editado en un archivo de texto
    def guardar_archivo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, 'w') as file:
                contenido = self.textbox.get(1.0, tk.END)
                file.write(contenido)
            messagebox.showinfo("Guardado", "El archivo ha sido guardado correctamente")

    def limpiar_texto(self):
        # Limpiar el contenido del textbox
        self.textbox.delete(1.0, tk.END)

    def analizar(self):
        contenido = self.textbox.get(1.0, tk.END).strip()
        lineas = contenido.split('\n')

        errores = []
        tokens_encontrados = {}

        # Limpiar la tabla antes de mostrar nuevos resultados
        for item in self.tree.get_children():
            self.tree.delete(item)

        operadores_compuestos = ['==', '<=', '>=']
        for operador in operadores_compuestos:
            count = contenido.count(operador)
            if count > 0:
                tokens_encontrados[operador] = count
                contenido = contenido.replace(operador, "")  

        operadores_simples = ['+', '-', '*', '/', '%', '=', '<', '>']
        for operador in operadores_simples:
            count = contenido.count(operador)
            if count > 0:
                tokens_encontrados[operador] = count

        for signo in tokens['Signos']:
            count = contenido.count(signo)
            if count > 0:
                tokens_encontrados[signo] = count
                contenido = contenido.replace(signo, '') 

        for tipo, patron in tokens.items():
            if isinstance(patron, list):
                for token in patron:
                    pattern = r'\b' + re.escape(token) + r'\b'
                    encontrados = re.findall(pattern, contenido)
                    if encontrados:
                        tokens_encontrados[token] = len(encontrados)
                        contenido = re.sub(pattern, '', contenido)  
            else:
                encontrados = re.findall(patron, contenido)
                for encontrado in encontrados:
                    tokens_encontrados[encontrado] = tokens_encontrados.get(encontrado, 0) + 1

        self.mostrar_resultados(tokens_encontrados)

    def mostrar_resultados(self, tokens_encontrados):
        # Insertar cada token en la tabla
        for token, cantidad in tokens_encontrados.items():
            tipo_token = self.obtener_tipo_token(token)
            self.tree.insert("", "end", values=(token, tipo_token, cantidad))

    def obtener_tipo_token(self, token):
        # Determinar el tipo de token (Palabras Reservadas, Operadores, Signos, etc.)
        for tipo, patron in tokens.items():
            if isinstance(patron, list):
                if token in patron:
                    return tipo
            else:
                if re.match(patron, token):
                    return tipo
        return "Desconocido"

# Clase para la pantalla de bienvenida
class PantallaBienvenida:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico - LF&A")
        self.root.geometry("900x500")  
        self.root.config(bg="#2c2c2c")

        # Título de bienvenida
        self.lbl_titulo1 = tk.Label(root, text="Lenguajes Formales y Autómatas", font=("Arial", 35, "italic", "bold"), bg="#2c2c2c", fg="white")
        self.lbl_titulo1.pack(pady=50)

        self.lbl_titulo = tk.Label(root, text="Proyecto #1 - Analizador Léxico", font=("Arial", 15, "bold"), bg="#2c2c2c", fg="white")
        self.lbl_titulo.pack(pady=50)

        # Nombres de los creadores
        self.lbl_creadores = tk.Label(root, text="Creado por:\nMiguel Salguero - 1626923\nJulio Cáceres - 1549223", font=("Arial", 12), bg="#2c2c2c", fg="white")
        self.lbl_creadores.pack(pady=20)

        # Botón para continuar a la aplicación
        self.btn_continuar = tk.Button(root, text="Iniciar", command=self.cargar_aplicacion, bg="#4CAF50", fg="white", font=("Arial", 15), width=20)
        self.btn_continuar.pack(pady=20)

    def cargar_aplicacion(self):
        self.root.destroy() 
        root = tk.Tk() 
        app = AnalizadorLexicoApp(root)
        root.mainloop()

# Función principal
if __name__ == "__main__":
    root = tk.Tk()
    app = PantallaBienvenida(root)
    root.mainloop()
