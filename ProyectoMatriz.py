import tkinter as tk
from tkinter import messagebox
import numpy as np

class MatrixCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Algebra Lineal - Calculadora de Matrices")
        self.geometry("800x600")
        self.configure(bg='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        # Frame principal para encerrar todos los elementos
        main_frame = tk.Frame(self, bg='#ffffff', bd=2, relief='solid', padx=20, pady=20)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        # Título principal
        tk.Label(main_frame, text="Calculadora de Matrices", font=("Helvetica", 16, "bold"), bg='#ffffff').pack(pady=10)

        # Frame para entradas de dimensiones de las matrices
        frame_dim = tk.Frame(main_frame, bg='#ffffff')
        frame_dim.pack(pady=20)

        tk.Label(frame_dim, text="Número de filas de la primera matriz:", bg='#ffffff').grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.filas1 = tk.Entry(frame_dim, width=5)
        self.filas1.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_dim, text="Número de columnas de la primera matriz:", bg='#ffffff').grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.columnas1 = tk.Entry(frame_dim, width=5)
        self.columnas1.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_dim, text="Número de filas de la segunda matriz:", bg='#ffffff').grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.filas2 = tk.Entry(frame_dim, width=5)
        self.filas2.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_dim, text="Número de columnas de la segunda matriz:", bg='#ffffff').grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.columnas2 = tk.Entry(frame_dim, width=5)
        self.columnas2.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(frame_dim, text="Ingresar Matrices", command=self.ingresar_matrices, bg='#007acc', fg='white').grid(row=4, column=0, columnspan=2, pady=20)

        # Frame para botones de operaciones
        self.operaciones_frame = tk.Frame(main_frame, bg='#ffffff')
        self.operaciones_frame.pack(pady=20)

        tk.Button(self.operaciones_frame, text="Mostrar Matrices", command=self.mostrar_matrices, bg='#007acc', fg='white', width=15).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.operaciones_frame, text="Sumar Matrices", command=self.sumar_matrices, bg='#007acc', fg='white', width=15).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.operaciones_frame, text="Multiplicar Matrices", command=self.multiplicar_matrices, bg='#007acc', fg='white', width=15).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(self.operaciones_frame, text="Comprobar Inversas", command=self.comprobar_inversas, bg='#007acc', fg='white', width=15).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(self.operaciones_frame, text="Calcular Inversas", command=self.calcular_inversas, bg='#007acc', fg='white', width=15).grid(row=0, column=4, padx=10, pady=5)

        # Información del autor en la parte inferior
        tk.Label(main_frame, text="Daniel David Arteaga Perez ", font=("Helvetica", 12), bg='#ffffff').pack(pady=10)
        tk.Label(main_frame, text="Kevin Leonardo Yaruro Maldonado", font=("Helvetica", 12), bg='#ffffff').pack(pady=10)
        tk.Label(main_frame, text="Jaider Esteban Villamizar", font=("Helvetica", 12), bg='#ffffff').pack(pady=10)
        tk.Label(main_frame, text="Ingeniería de Software ", font=("Helvetica",            12), bg='#ffffff').pack(pady=10)

    def ingresar_matrices(self):
        try:
            filas1 = int(self.filas1.get())
            columnas1 = int(self.columnas1.get())
            filas2 = int(self.filas2.get())
            columnas2 = int(self.columnas2.get())
            
            self.crear_matriz(filas1, columnas1, filas2, columnas2)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos para las dimensiones.")

    def crear_matriz(self, filas1, columnas1, filas2, columnas2):
        top = tk.Toplevel(self)
        top.title("Ingresar Matrices")

        frame_entries = tk.Frame(top, bg='#f0f0f0')
        frame_entries.pack(pady=20)

        tk.Label(frame_entries, text="Primera Matriz", bg='#f0f0f0', font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=columnas1, pady=10)

        entries1 = []
        for i in range(filas1):
            fila_entries = []
            for j in range(columnas1):
                entry = tk.Entry(frame_entries, width=5)
                entry.grid(row=i+1, column=j, padx=5, pady=5)
                fila_entries.append(entry)
            entries1.append(fila_entries)

        start_row = filas1 + 2

        tk.Label(frame_entries, text="Segunda Matriz", bg='#f0f0f0', font=("Helvetica", 12, "bold")).grid(row=start_row, column=0, columnspan=columnas2, pady=10)

        entries2 = []
        for i in range(filas2):
            fila_entries = []
            for j in range(columnas2):
                entry = tk.Entry(frame_entries, width=5)
                entry.grid(row=i+start_row+1, column=j, padx=5, pady=5)
                fila_entries.append(entry)
            entries2.append(fila_entries)

        def guardar_matrices():
            matriz1 = []
            matriz2 = []
            try:
                for i in range(filas1):
                    fila = [float(entries1[i][j].get()) for j in range(columnas1)]
                    matriz1.append(fila)

                for i in range(filas2):
                    fila = [float(entries2[i][j].get()) for j in range(columnas2)]
                    matriz2.append(fila)

                self.matriz1 = np.array(matriz1)
                self.matriz2 = np.array(matriz2)
                messagebox.showinfo("Información", "Matrices ingresadas correctamente.")
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese solo números válidos.")

        tk.Button(frame_entries, text="Guardar Matrices", command=guardar_matrices, bg='#007acc', fg='white').grid(row=start_row+filas2+1, column=0, columnspan=columnas1+columnas2, pady=20)

    def mostrar_matrices(self):
        try:
            matriz1_str = f"Matriz 1:\n{self.matriz1}\n\n" if hasattr(self, 'matriz1') else "Matriz 1:\nNo ingresada\n\n"
            matriz2_str = f"Matriz 2:\n{self.matriz2}\n" if hasattr(self, 'matriz2') else "Matriz 2:\nNo ingresada\n"
            matrices_str = matriz1_str + matriz2_str

            messagebox.showinfo("Matrices", matrices_str)
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese las matrices.")

    def sumar_matrices(self):
        try:
            resultado = self.matriz1 + self.matriz2
            messagebox.showinfo("Resultado", f"La suma de las matrices es:\n{resultado}")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese las matrices.")
        except ValueError:
            messagebox.showerror("Error", "Las dimensiones de las matrices no son compatibles para la suma.")

    def multiplicar_matrices(self):
        try:
            resultado = np.matmul(self.matriz1, self.matriz2)
            messagebox.showinfo("Resultado", f"La multiplicación de las matrices es:\n{resultado}")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese las matrices.")
        except ValueError:
            messagebox.showerror("Error", "Las dimensiones de las matrices no son compatibles para la multiplicación.")

    def comprobar_inversas(self):
        try:
            if hasattr(self, 'matriz1') and hasattr(self, 'matriz2'):
                inversa1 = np.linalg.inv(self.matriz1)
                inversa2 = np.linalg.inv(self.matriz2)
                messagebox.showinfo("Inversas", f"Inversa de la Matriz 1:\n{inversa1}\n\nInversa de la Matriz 2:\n{inversa2}")
            else:
                messagebox.showerror("Error", "Primero ingrese las matrices.")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese las matrices.")
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "Alguna de las matrices no es invertible.")

    def calcular_inversas(self):
        try:
            if hasattr(self, 'matriz1') and hasattr(self, 'matriz2'):
                inversa1 = np.linalg.inv(self.matriz1)
                inversa2 = np.linalg.inv(self.matriz2)
                messagebox.showinfo("Inversas", f"Inversa de la Matriz 1:\n{inversa1}\n\nInversa de la Matriz 2:\n{inversa2}")
            else:
                messagebox.showerror("Error", "Primero ingrese las matrices.")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese las matrices.")
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "Alguna de las matrices no es invertible.")

if __name__ == "__main__":
    app = MatrixCalculator()
    app.mainloop()