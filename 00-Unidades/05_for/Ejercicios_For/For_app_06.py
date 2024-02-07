import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresar = prompt("Numeros Divisores", "Ingrese un numero")
        numero_ingresado = int(numero_ingresar)
        cantidad_divisores = 0
        numero_divisor = 0
        for numero_dividido in range(numero_ingresado):
            numero_divisor = numero_divisor + 1
            resto = numero_ingresado % numero_divisor
            if(resto == 0):
                alert("Numeros Divisores", "Numero Divisor: " + str(numero_divisor))
                cantidad_divisores = cantidad_divisores + 1
        alert("Numeros Divisores", "La cantidad de numeros divisores son: " + str(cantidad_divisores))
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()