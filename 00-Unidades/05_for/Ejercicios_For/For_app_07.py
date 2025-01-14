import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresar = prompt("Numeros Primos", "Ingrese un numero")
        numero_ingresado = int(numero_ingresar)
        for NumeroPrimo in range(numero_ingresado):
           numero_ingresado = numero_ingresado % 2
           if(numero_ingresado == 1):
               alert("Numeros Primos","El numero ingresado es un numero PRIMO")
               break
           elif(numero_ingresado == 0):
               alert("Numeros Primos", "El numero ingresado es un numero COMPUESTO")
               break
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()