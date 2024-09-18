import re

class AnalizadorLexicoApp:
    def __init__(self, root):
        # Código del constructor aquí (omitido para brevedad)
        pass

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, 'r') as file:
                contenido = file.read()
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, contenido)

    def guardar_archivo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, 'w') as file:
                contenido = self.textbox.get(1.0, tk.END)
                file.write(contenido)
            messagebox.showinfo("Guardado", "El archivo ha sido guardado correctamente")

    def limpiar_texto(self):
        self.textbox.delete(1.0, tk.END)

    def analizar(self):
        contenido = self.textbox.get(1.0, tk.END).strip()
        tokens_encontrados = {}

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
        for token, cantidad in tokens_encontrados.items():
            tipo_token = self.obtener_tipo_token(token)
            self.tree.insert("", "end", values=(token, tipo_token, cantidad))

    def obtener_tipo_token(self, token):
        for tipo, patron in tokens.items():
            if isinstance(patron, list):
                if token in patron:
                    return tipo
            else:
                if re.match(patron, token):
                    return tipo
        return "Desconocido"
