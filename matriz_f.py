import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import *
import numpy as np

class App(ctk.CTk,tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("CALCULADORA DE MATRICES")
        self.geometry("1280x720")
        self.modo = ctk.set_appearance_mode('dark')
        
        self.create_frame()
        
        self.create_frame2()
        
    def create_frame(self):    
        self.frame = ctk.CTkFrame(master=self, width=500,  height=1015,  fg_color=("gray9", "gray9"), corner_radius=20, border_width=4, border_color="dark green")
        self.frame.place(x=0,y=0)
            
        self.label1 =  ctk.StringVar(value="Menú: ")
        self.OPS = ctk.CTkLabel(master=self, textvariable=self.label1, width=300, font=('Comic Sans MS', 25, 'bold'), text_color=("black", "white"), fg_color='gray9', bg_color='gray9', justify='center', anchor='center')
        self.anchor=self.OPS.place(relx=0.1, rely=0.1, anchor=ctk.SW, x=-60, y=50)
    
        # Todos los botones de cada operacion de matrices    
        self.button_suma = ctk.CTkButton(self, text="Suma", command=self.boton_suma, fg_color="gray9", hover_color="green", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="dark green", bg_color=("gray9", "gray9"))
        self.button_suma.configure(width=200, height=50)
        self.button_suma.configure(command=self.boton_suma)
        self.button_suma.place(x=130, y=200)
            
        self.button_producto = ctk.CTkButton(self, text="Multiplicación", command=self.boton_producto, fg_color="gray9", hover_color="green", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="dark green", bg_color=("gray9", "gray9"))
        self.button_producto.configure(width=200, height=50)
        self.button_producto.place(x=130, y=300)

        self.button_transpuesta = ctk.CTkButton(self, text="Transpuesta", command=self.boton_transpuesta, fg_color="gray9", hover_color="green", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="dark green", bg_color=("gray9", "gray9"))
        self.button_transpuesta.configure(width=200, height=50)
        self.button_transpuesta.place(x=130, y=400)

        self.button_reduccion = ctk.CTkButton(self, text="Reducción", command=self.boton_reduccion, fg_color="gray9", hover_color="green", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="dark green", bg_color=("gray9", "gray9"))
        self.button_reduccion.configure(width=200, height=50)
        self.button_reduccion.place(x=130, y=500)
        
        self.button_mostrar = ctk.CTkButton(self, text="Mostrar Matriz", command=self.mostrar_matrices, fg_color="gray9", hover_color="green", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="dark green", bg_color=("gray9", "gray9"))
        self.button_mostrar.configure(width=200, height=50)
        self.button_mostrar.place(x=130, y=600)

        self.button_salida = ctk.CTkButton(self, text="Salir", command=self.boton_salida, fg_color="red", hover_color="dark red", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="red3", bg_color=("gray9", "gray9"))
        self.button_salida.configure(width=200, height=50)
        self.button_salida.place(x=130, y=700)

        self.button_ayuda_suma = ctk.CTkButton(self, text="Ayuda", command=self.boton_help_suma, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("gray9", "gray9"))
        self.button_ayuda_suma.configure(width=80, height=50)
        self.button_ayuda_suma.place(x=380, y=200)

        self.button_ayuda_producto = ctk.CTkButton(self, text="Ayuda", command=self.boton_help_producto, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("gray9", "gray9"))
        self.button_ayuda_producto.configure(width=80, height=50)
        self.button_ayuda_producto.place(x=380, y=300)

        self.button_ayuda_transpuesta = ctk.CTkButton(self, text="Ayuda", command=self.boton_help_transpuesta, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("gray9", "gray9"))
        self.button_ayuda_transpuesta.configure(width=80, height=50)
        self.button_ayuda_transpuesta.place(x=380, y=400)

        self.button_ayuda_reduccion = ctk.CTkButton(self, text="Ayuda", command=self.boton_help_reduccion, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("gray9", "gray9"))
        self.button_ayuda_reduccion.configure(width=80, height=50)
        self.button_ayuda_reduccion.place(x=380, y=500)

        self.button_ayuda_reduccion = ctk.CTkButton(self, text="Creditos", command=self.creditos_usuarios, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("gray9", "gray9"))
        self.button_ayuda_reduccion.configure(width=80, height=50)
        self.button_ayuda_reduccion.place(x=380, y=600)

        self.label2 =  ctk.StringVar(value="Operación con matrices")
        self.OPM = ctk.CTkLabel(master=self, textvariable=self.label2, width=400, fg_color=('gray9'), bg_color='gray9', font=('Comic Sans MS', 25, 'bold'), text_color="white", justify='center', anchor='center', corner_radius=0)
        self.OPM.place(relx=0.1, rely=0.1,y=-60, x=-100)
        
    def create_frame2(self):  
        self.frame2 = ctk.CTkFrame(master=self, width=1420,  height=1015,  fg_color=("gray9", "gray9"), corner_radius=20, border_width=4, border_color="royal blue")
        self.frame2.place(x=500,y=0)
        
        self.frame_dim1 = ctk.CTkFrame(master=self, width=50, height=50, bg_color='gray9', fg_color='gray9')
        self.frame_dim1.place(x=870,y=180)
        
        self.frame_dim2 = ctk.CTkFrame(master=self, width=50, height=50, bg_color='gray9', fg_color='gray9')
        self.frame_dim2.place(x=870,y=225)
        
        self.frame_dim3 = ctk.CTkFrame(master=self, width=50, height=50, bg_color='gray9', fg_color='gray9')
        self.frame_dim3.place(x=870,y=265)
        
        self.frame_dim4 = ctk.CTkFrame(master=self, width=50, height=50, bg_color='gray9', fg_color='gray9')
        self.frame_dim4.place(x=870,y=305)
        
        self.label3 =  ctk.StringVar(value="Número de filas de la primera matriz:")
        self.OPM = ctk.CTkLabel(master=self, textvariable=self.label3, width=100, fg_color=('gray9'), bg_color='gray9', font=('Comic Sans MS', 15, 'bold'), text_color="white", justify='center', anchor='center', corner_radius=0)
        self.anchor=self.OPM.place(relx=0.1, rely=0.1,y=100, x=400)
        
        self.filas1 = ctk.CTkEntry(self.frame_dim1,width=5)
        self.filas1.grid(row=0, column=1, padx=10, pady=5)
        
        self.label4 =  ctk.StringVar(value="Número de columnas de la primera matriz:")
        self.OPM = ctk.CTkLabel(master=self, textvariable=self.label4, width=100, fg_color=('gray9'), bg_color='gray9', font=('Comic Sans MS', 15, 'bold'), text_color="white", justify='center', anchor='center', corner_radius=0)
        self.anchor=self.OPM.place(relx=0.1, rely=0.1,y=140, x=400)
        
        self.columnas1 = ctk.CTkEntry(self.frame_dim2,width=5)
        self.columnas1.grid(row=0, column=1, padx=10, pady=5)
        
        self.label5 =  ctk.StringVar(value="Número de filas de la segunda matriz:")
        self.OPM = ctk.CTkLabel(master=self, textvariable=self.label5, width=100, fg_color=('gray9'), bg_color='gray9', font=('Comic Sans MS', 15, 'bold'), text_color="white", justify='center', anchor='center', corner_radius=0)
        self.anchor=self.OPM.place(relx=0.1, rely=0.1,y=180, x=400)
        
        self.filas2 = ctk.CTkEntry(self.frame_dim3,width=5)
        self.filas2.grid(row=0, column=1, padx=10, pady=5)
        
        self.label6 =  ctk.StringVar(value="Número de columnas de la segunda matriz:")
        self.OPM = ctk.CTkLabel(master=self, textvariable=self.label6, width=100, fg_color=('gray9'), bg_color='gray9', font=('Comic Sans MS', 15, 'bold'), text_color="white", justify='center', anchor='center', corner_radius=0)
        self.anchor=self.OPM.place(relx=0.1, rely=0.1,y=220, x=400)
        
        self.columnas2 = ctk.CTkEntry(self.frame_dim4,width=5)
        self.columnas2.grid(row=0, column=1, padx=10, pady=5)
        
        self.button_ingresar = ctk.CTkButton(self, text="Ingresar matrices", command=self.ingresar_matriz, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("gray9", "gray9"))
        self.button_ingresar.configure(width=200, height=50)
        self.button_ingresar.configure(command=self.ingresar_matriz)
        self.button_ingresar.place(x=650, y=350)

        self.button_operaciones = ctk.CTkButton(self, text="¿Como funciona?", command=self.ayuda_funciona, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("gray9", "gray9"))
        self.button_operaciones.configure(width=200, height=50)
        self.button_operaciones.configure(command=self.ayuda_funciona)
        self.button_operaciones.place(x=950, y=350)

    def boton_suma(self):
        try:
            resultado = self.matriz1 + self.matriz2
            messagebox.showinfo("resultado",f"El resultado entre las matrices \n{self.matriz1} y  \n{self.matriz2}"f"\nLa suma de las matrices es:\n{resultado}")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese las matrices.")
        except ValueError:
            messagebox.showerror("Error", "Las dimensiones de las matrices no son compatibles para la suma.")
    
    def boton_help_suma(self):
        messagebox.showinfo(title="Reglas para sumar matrices",
                            message="""Regla fundamental:\nPara poder sumar dos matrices, ambas deben tener las mismas dimensiones.\nEs decir, deben tener el mismo número de filas y el mismo número de columnas.\nProceso de suma:\nSi dos matrices cumplen con la condición de tener las mismas dimensiones, la suma se realiza elemento a elemento.\nEsto significa que:\nCada elemento de la matriz resultante será la suma de los elementos correspondientes de las matrices originales.\n\nNOTA: máximo de la matriz 10x10""")

    def boton_producto(self):
        try:
            resultado = np.matmul(self.matriz1, self.matriz2)
            messagebox.showinfo("Resultado",f"El resultado entre las matrices \n{self.matriz1} y  \n{self.matriz2}" f"\nLa multiplicación de las matrices es:\n{resultado}")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese las matrices.")
        except ValueError:
            messagebox.showerror("Error", "Las dimensiones de las matrices no son compatibles para la multiplicación.")

    def boton_help_producto(self):
        messagebox.showinfo(title="Reglas para multiplicar matrices",
                            message="""Regla fundamental:\nPara poder multiplicar dos matrices, el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.\nEn resumen:\nVerifica las dimensiones:\nAsegúrate de que el número de columnas de la primera matriz coincida con el número de filas de la segunda.\nMultiplica y suma: Para cada elemento de la matriz resultante, realiza el producto escalar de una fila de la primera matriz y una columna de la segunda matriz.\n\nNOTA: máximo de la matriz 10x10""")


    def boton_transpuesta(self):
        try:
            if self.matriz1 is not None:
                resultado = self.matriz1.T
                messagebox.showinfo("Resultado", f"La transpuesta de la primera matriz es:\n{resultado}")
            else:
                messagebox.showerror("Error", "Primero ingrese la primera matriz.")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese la primera matriz.")

    def boton_help_transpuesta(self):
        messagebox.showinfo(title="Reglas de las matrices transpuestas",
                            message="""Regla fundamental:\nLa matriz transpuesta se obtiene al intercambiar las filas por las columnas y viceversa. Es decir, la primera fila de la matriz original se convierte en la primera columna de la matriz transpuesta, la segunda fila en la segunda columna, y así sucesivamente.\nLa transpuesta mostrada es del caso de la primera matriz.\n\nNOTA: máximo de la matriz 10x10 y solo trabaja con la primera matriz""")


    def boton_reduccion(self):
        try:
            if self.matriz1 is not None:
                if self.matriz1.shape[0] == self.matriz1.shape[1]:  # Check if the matrix is square
                    if np.linalg.matrix_rank(self.matriz1) == min(self.matriz1.shape):  # Check if the matrix has linearly independent rows and columns
                        resultado = self.matriz1
                        messagebox.showinfo("Resultado",f"La matriz es reducida.\n{resultado}")
                    else:
                        resultado = self.matriz1
                        messagebox.showinfo("Resultado", f"La matriz no es reducida.\n{resultado}")
                else:
                    resultado = self.matriz1
                    messagebox.showerror("Error", f"La matriz debe ser cuadrada para ser reducida.\n{resultado}")
            else:
                messagebox.showerror("Error", "Primero ingrese la primera matriz.")
        except AttributeError:
            messagebox.showerror("Error", "Primero ingrese la primera matriz.")

    def boton_help_reduccion(self):
        messagebox.showinfo(title="Reglas para verificar reducción de matrices",
                            message="""Reglas de la reducción de matrices:\nMatriz escalonada reducida por filas:\nUna matriz está en forma escalonada reducida por filas si cumple con las siguientes condiciones:\nFilas nulas abajo: Todas las filas nulas (filas con todos sus elementos iguales a cero) deben estar agrupadas en la parte inferior de la matriz.\nPivotes iguales a 1: El primer elemento no nulo de cada fila no nula (llamado pivote) debe ser igual a 1.\nPivotes escalonados: Los pivotes de cada fila deben estar estrictamente a la derecha del pivote de la fila superior.\nCeros debajo y arriba de los pivotes: Todos los elementos debajo y arriba de un pivote deben ser ceros.\n\nNOTA: máximo de la matriz 10x10 y solo trabaja con la primera matriz""")


    def boton_salida(self):
        response = messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?")
        if response:
            self.destroy()
        
    def ingresar_matriz(self):
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
    
    def ayuda_funciona(self):
        ayuda = messagebox.showinfo("¿COMO FUNCIONA?", "Pasos para tabajar en tu calculadora de matrices:\n1. Primer paso: introduzca el tamaño de cada matriz en el siguiente orden.\nPrimero filas.\nSegundo columnas.\n2. Segundo paso: Introduzca cada elemento de la matriz.\nRellenar la primera matriz y la segunda matriz.\n3. Tercer paso: Operar suma, multiplicación, la transpuesta y verificar la reducción pulsando los botones de la izquierda.\n Eso es todo lo que necesitas para empezar a operar espero que te diviertas.")  

    def creditos_usuarios(self):
        creditos = messagebox.showinfo("CREDITOS", "Desarrolladores:\n Jose Rojas y Diego Gollarza\nEditorial usada:\nDe Ernest F. Haeussler, Richard S. Paul. 2003. Matematicas para la administración y economía.\nEditorial: Prentice Hall")

if __name__ == "__main__":
    app = App()
    app.mainloop()