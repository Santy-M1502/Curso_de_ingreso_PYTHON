import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        activador = True
        self.txt_maximo.insert(0, 0)
        self.txt_minimo.insert(0, 0)
        primer_valor = prompt("Numero", "Ingrese un numero")
        self.txt_maximo.delete(0, 100000)
        self.txt_minimo.delete(0, 100000)
        self.txt_maximo.insert(0, primer_valor)
        self.txt_minimo.insert(0, primer_valor)
        numero_maximo_texto = self.txt_maximo.get()
        numero_minimo_texto = self.txt_minimo.get()
        numero_maximo = float(numero_maximo_texto)
        numero_minimo = float(numero_minimo_texto)
        while(activador):   
            numero_maximo_texto = self.txt_maximo.get()
            numero_minimo_texto = self.txt_minimo.get()
            numero_maximo = float(numero_maximo_texto)
            numero_minimo = float(numero_minimo_texto)              
            numero_ingresar = prompt("Numero", "Ingrese un numero")
            numero_ingresado = float(numero_ingresar)
            if(numero_ingresado > numero_maximo):
                self.txt_maximo.delete(0, 100000)
                self.txt_maximo.insert(0, numero_ingresado)
            if(numero_ingresado < numero_minimo):
                self.txt_minimo.delete(0, 100000)
                self.txt_minimo.insert(0, numero_ingresado)
            elif(numero_ingresado == None):
                break


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
