import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from tkinter import *
import numpy as np


class ProyectoAppMatriz:

    def __init__(self, root):
         # inicializacion del root osea la app
        self.root = root
        self.root = root.title("Matriz.exe")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        root.geometry("1920x1080")

        self.crea_menus()

    def crea_menus(self):
        # pestañas de cada resolvencia
        self.pestana_suma = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_suma, text="Suma de matrices")
        self.crea_suma_pestana() 

        self.pestana_producto = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_producto, text="Producto de matrices")
        self.crea_product_pestana()

        self.pestana_transpuesta = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_transpuesta, text="Transpuesta de matriz")
        self.crea_transp_pestana()

        self.pestana_reducir = ttk.Frame(self.notebook)
        self.notebook.add(self.pestana_reducir, text="Matriz reducida")
        self.crea_reducir_pestana()

    #funciones de inputs para los datos de las matrices
    def crea_suma_pestana(self):

        tk.Label(self.pestana_suma, text="Tamaño de las matrices (n x m):").pack(pady=5)
        self.size_pestana_suma_entrada = tk.Entry(self.pestana_suma)
        self.size_pestana_suma_entrada.pack(pady=5)
        
        tk.Button(self.pestana_suma, text="Ingresar Datos y Sumar", command=self.realiza_suma).pack(pady=10)
    
    def crea_product_pestana(self):
        tk.Label(self.pestana_producto, text="Tamaño de las matrices (n x m):").pack(pady=5)
        self.size_pestana_producto_entrada = tk.Entry(self.pestana_producto)
        self.size_pestana_producto_entrada.pack(pady=5)
        
        tk.Button(self.pestana_producto, text="Ingresar Datos y Multiplicar", command=self.realizar_producto).pack(pady=10)

    def crea_transp_pestana(self):
        tk.Label(self.pestana_transpuesta, text="Tamaño de la matriz (n x m):").pack(pady=5)
        self.size_pestana_transpueta_entrada = tk.Entry(self.pestana_transpuesta)
        self.size_pestana_transpueta_entrada.pack(pady=5)
        
        tk.Button(self.pestana_transpuesta, text="Ingresar Datos y Transponer", command=self.realizar_transpuesta).pack(pady=10)

    def crea_reducir_pestana(self):
        tk.Label(self.pestana_reducir, text="Tamaño de la matriz (n x m):").pack(pady=5)
        self.size_pestana_reducir_entrada = tk.Entry(self.pestana_reducir)
        self.size_pestana_reducir_entrada.pack(pady=5)
        
        tk.Button(self.pestana_reducir, text="Ingresar Datos y Verificar Reducción", command=self.realizar_reduccion).pack(pady=10)

    # Funciones para la obtencion de los datos y realizar las operaciones
    def obtener_matriz(self, tamano_matriz):
        try:
            tamano = tamano_matriz.get()
            n, m = map(int, tamano.split('x'))
            matriz = []
            for i in range(n):
                row = simpledialog.askstring("Entrada", f"Ingrese los elementos de la fila {i+1} separados por comas:")
                matriz.append(list(map(float, row.split(','))))
            return np.array(matriz)
        except Exception as e:
            messagebox.showerror("Error", f"Error al ingresar datos: {str(e)}")
            return None

    def realiza_suma(self):
        matriz1 = self.obtener_matriz(self.size_pestana_suma_entrada)
        if matriz1 is None:
            return
        
        matriz2 = self.obtener_matriz(self.size_pestana_suma_entrada)
        if matriz2 is None:
            return
        
        if matriz1.shape != matriz2.shape:
            messagebox.showerror("Error", "Las matrices deben tener el mismo tamaño para la suma.")
            return
        
        result = matriz1 + matriz2
        messagebox.showinfo("Resultado", f"Resultado de la suma:\n{result}")

    def realizar_producto(self):
        matriz1 = self.obtener_matriz(self.size_pestana_producto_entrada)
        if matriz1 is None:
            return
        
        matriz2 = self.obtener_matriz(self.size_pestana_producto_entrada)
        if matriz2 is None:
            return
        
        if matriz1.shape[1] != matriz2.shape[0]:
            messagebox.showerror("Error", "Las matrices no se pueden multiplicar. Verifica las dimensiones.")
            return
        
        result = np.dot(matriz1, matriz2)
        messagebox.showinfo("Resultado", f"Resultado del producto:\n{result}")

    def realizar_transpuesta(self):
        matriz = self.obtener_matriz(self.size_pestana_transpueta_entrada)
        if matriz is None:
            return
        
        result = matriz.T
        messagebox.showinfo("Resultado", f"Matriz Transpuesta:\n{result}")
   
    def realizar_reduccion(self):
        matriz = self.obtener_matriz(self.size_pestana_reducir_entrada)
        if matriz is None:
            return
        if np.linalg.matrix_rank(matriz) == min(matriz.shape):
            messagebox.showinfo("Resultado", f"La matriz es reducida. \n{matriz}")    
        else:
            messagebox.showinfo("Resultado", f"La matriz no es reducida. \n{matriz}")

root = tk.Tk()
app = ProyectoAppMatriz(root)
root.mainloop()