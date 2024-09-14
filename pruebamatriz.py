import customtkinter as ctk
from customtkinter import *
from PIL import Image
import numpy as np

def ingresar_matriz(filas, columnas):
    """Ingresa una matriz de tamaño filas x columnas."""
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"\nIngrese el elemento en la posición ({i+1}, {j+1}): "))
            fila.append(elemento)
        matriz.append(fila)
    return np.array(matriz)

def imprimir_matriz(matriz):
    """Imprime la matriz en formato tabular."""
    for fila in matriz:
        for elemento in fila:
            print(f"{int(elemento):6d}", end=" ")
        print()
        

def imprimir_matrices(matriz_original, matriz_resultado):
    """Imprime la matriz original y la matriz resultado."""
    print("Matriz original:")
    imprimir_matriz(matriz_original)
    print("\nMatriz resultado:")
    imprimir_matriz(matriz_resultado)

def sumar_matrices(matriz1, matriz2):
    """Suma dos matrices si tienen las mismas dimensiones."""
    if matriz1.shape == matriz2.shape:
        matriz_resultado = matriz1.copy()
        matriz_resultado += matriz2
        imprimir_matrices(matriz1, matriz_resultado)
        return matriz_resultado
    else:
        print("No se pueden sumar matrices de diferentes dimensiones.")
        return None

def multiplicar_matrices(matriz1, matriz2):
    """Multiplica dos matrices si el número de columnas de la primera es igual al número de filas de la segunda."""
    if matriz1.shape[1] == matriz2.shape[0]:
        matriz_resultado = matriz1.copy()
        matriz_resultado = np.dot(matriz_resultado, matriz2)
        imprimir_matrices(matriz1, matriz_resultado)
        return matriz_resultado
    else:
        print("No se pueden multiplicar estas matrices. El número de columnas de la primera matriz debe ser igual al número de filas de la   segunda.")
        return None

def transpuesta_matriz(matriz):
    """Calcula la transpuesta de una matriz."""
    matriz_transpuesta = matriz.copy()
    imprimir_matrices(matriz, matriz_transpuesta)
    return matriz_transpuesta.T

def reducir_filas(matriz):
    """Reduce una matriz a su forma escalonada reducida por filas."""
    matriz_reducida = matriz.copy() 
    filas, columnas = matriz_reducida.shape
    
    matriz_reducida = matriz_reducida.astype(float) 
    for i in range(filas):
        indice_pivote = np.argmax(np.abs(matriz_reducida[i:, i])) + i
        matriz_reducida[[i, indice_pivote]] = matriz_reducida[[indice_pivote, i]]
        pivote = matriz_reducida[i, i]
        if pivote != 0:
            matriz_reducida[i] /= pivote
            for j in range(i+1, filas):
                matriz_reducida[j] -= matriz_reducida[j, i] * matriz_reducida[i]
    
    es_reducida = np.all(np.tril(matriz_reducida, -1) == 0)
    
    if es_reducida:
        print("La matriz está en forma reducida.")
    else:
        print("La matriz no está en forma reducida.")
    
    return matriz_reducida

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1620x720")
        self.modo = ctk.set_appearance_mode('dark')
        self.title("OPERACIONES CON MATRICES")

        self.imagen = ctk.CTkImage(light_image=Image.open("imagen_calculo.jpg"),
                                   dark_image=Image.open("imagen_calculo.jpg"),
                                   size=(950,1080))
        self.label_imagen = ctk.CTkLabel(self, text="", image=self.imagen)
        self.label_imagen.pack()
        self.label_imagen.place(x=700)

        self.label1 =  ctk.StringVar(value="Operacion con matrices")
        self.OPM = ctk.CTkLabel(master=self, textvariable=self.label1,
                               width=700,
                               fg_color=('blue'),
                               font=('Comic Sans MS', 30, 'bold'),
                               text_color="white",
                               justify='center',
                               anchor='center',
                               corner_radius=25)
 
        # label de OPERACION DE MATRICES ESTA VARIABLE HACE LA COLOCACION DEL LABEL JUNTO A SU UBICACION
        self.anchor=self.OPM.place(relx=0.1, rely=0.1, anchor=ctk.SW, x=620)
        
        self.label2 =  ctk.StringVar(value="Menu de opciones: ")
        self.OPS = ctk.CTkLabel(master=self, textvariable=self.label2,
                               width=300,
                               font=('Comic Sans MS', 30, 'bold'),
                               text_color=("black", "white"),
                               justify='center',
                               anchor='center')
        
        self.anchor=self.OPS.place(relx=0.1, rely=0.1, anchor=ctk.SW, x=-20, y=70)      

        self.frame = ctk.CTkFrame(master=self, width=400,  height=540,  fg_color=("navy", "navy"), corner_radius=20, border_width=4, border_color="royal blue")
        self.frame.place(x=80,y=150)       
    
        # Todos los botones de cada operacion de matrices    
        self.button_suma = ctk.CTkButton(self, text="Suma", command=self.boton_suma, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("navy", "navy"))
        self.button_suma.configure(width=200, height=50)
        self.button_suma.place(x=175, y=200)
        
        self.button_producto = ctk.CTkButton(self, text="Multiplicacion", command=self.boton_producto, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("navy", "navy"))
        self.button_producto.configure(width=200, height=50)
        self.button_producto.place(x=175, y=300)

        self.button_transpuesta = ctk.CTkButton(self, text="Transpuesta", command=self.boton_transpuesta, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("navy", "navy"))
        self.button_transpuesta.configure(width=200, height=50)
        self.button_transpuesta.place(x=175, y=400)

        self.button_reduccion = ctk.CTkButton(self, text="Reduccion", command=self.boton_reduccion, fg_color="dodger blue", hover_color="dark blue", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("navy", "navy"))
        self.button_reduccion.configure(width=200, height=50)
        self.button_reduccion.place(x=175, y=500)

        self.button_salida = ctk.CTkButton(self, text="Salir", command=self.boton_salida, fg_color="red", hover_color="dark red", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("navy", "navy"))
        self.button_salida.configure(width=200, height=50)
        self.button_salida.place(x=175, y=600)
        
        #self.button_salida = ctk.CTkButton(self, text="Salir", command=self.boton_regresar, fg_color="red", hover_color="dark red", corner_radius=32, font=("Copperplate", 15, "bold"), border_width=3, border_color="royal blue", bg_color=("navy", "navy"))
        #self.button_salida.configure(width=200, height=50)
        #self.button_salida.place(x=175, y=700)
        
        self.button_tema = ctk.CTkSwitch(master=self, text="Tema", command=self.boton_theme, border_width=3)
        self.button_tema.place(x=20, y=10)    


    def boton_suma(self):
        self.OPM.destroy()
        self.label_imagen.destroy()
        
    def boton_producto(self):
        self.OPM.destroy()
        self.label_imagen.destroy()
        print("producto")

    def boton_transpuesta(self):
        self.OPM.destroy()
        self.label_imagen.destroy()
        print("transpuesta")

    def boton_reduccion(self):
        self.OPM.destroy()
        self.label_imagen.destroy()
        print("reduccion")

    def boton_salida(self):
        self.destroy()       

    def boton_theme(self):
        self.modo = "dark" if self.modo == "light" else "light"
        ctk.set_appearance_mode(self.modo)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()