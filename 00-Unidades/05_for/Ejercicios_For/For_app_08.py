import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = int(prompt("Numeros Primos", "Ingrese un numero"))
        cantidad_ingresados = 0
        for numero_primo in range(numero_ingresado + 1):
            if(numero_primo % 2 == 1):
                alert("Numeros Primos", str(numero_primo) + " es un numero primo")
                cantidad_ingresados += 1
        alert("Numeros Primos", "La cantidad de numeros primos es: " + str(cantidad_ingresados))

            
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()