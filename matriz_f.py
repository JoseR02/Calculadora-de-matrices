import customtkinter as ctk
from customtkinter import *
from PIL import Image
import numpy as np

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")

        # variable para establecer el tema de la aplicacion
        self.modo = ctk.set_appearance_mode('dark')

        self.title("OPERACIONES CON MATRICES")

        self.imagen = ctk.CTkImage(light_image=Image.open("imagen_calculo.jpg"),
                                   dark_image=Image.open("imagen_calculo.jpg"),
                                   size=(950,1080))
        self.label_imagen = ctk.CTkLabel(self, text="", image=self.imagen)
        self.label_imagen.pack()
        self.label_imagen.place(x=700)

        self.label1 =  ctk.StringVar(value="Operacion con matrices")
        self.OPM = ctk.CTkLabel(master=self, textvariable = self.label1,
                               width=700,
                               fg_color=("white", "blue"),
                               padx=20,
                               pady=20,
                               height=20,
                               font=('text_var_origin', 30))
        # label de OPERACION DE MATRICES ESTA VARIABLE HACE LA COLOCACION DEL LABEL JUNTO A SU UBICACION
        self.anchor=self.OPM.place(relx=0.1, rely=0.1, anchor=ctk.SW, x=620)

        self.frame = ctk.CTkFrame(master=self, width=400, height=550)
        self.frame.place(x=80,y=150)

        # Todos los botones de cada operacion de matrices    
        self.button_suma = ctk.CTkButton(self, text="SUMA", command=self.boton_suma, border_width=3)
        self.button_suma.configure(width=200, height=50)
        self.button_suma.place(x=175, y=200)

        self.button_producto = ctk.CTkButton(self, text="MULTIPLICACION", command=self.boton_producto, border_width=3)
        self.button_producto.configure(width=200, height=50)
        self.button_producto.place(x=175, y=300)

        self.button_transpuesta = ctk.CTkButton(self, text="TRANSPUESTA", command=self.boton_transpuesta, border_width=3)
        self.button_transpuesta.configure(width=200, height=50)
        self.button_transpuesta.place(x=175, y=400)

        self.button_reduccion = ctk.CTkButton(self, text="REDUCCION", command=self.boton_reduccion, border_width=3)
        self.button_reduccion.configure(width=200, height=50)
        self.button_reduccion.place(x=175, y=500)

        self.button_salida = ctk.CTkButton(self, text="EXIT", command=self.boton_salida, border_width=3)
        self.button_salida.configure(width=200, height=50)
        self.button_salida.place(x=175, y=600)

        self.button_tema = ctk.CTkSwitch(master=self, text="Theme", command=self.boton_theme, border_width=3)
        self.button_tema.place(x=20, y=10)


    def boton_suma(self):
        self.OPM.destroy()
        self.label_imagen.destroy()
        print("button clicked")
    
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



app = App()
app.mainloop()