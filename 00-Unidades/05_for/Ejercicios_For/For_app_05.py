import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresar = prompt("Numeros Pares", "Ingrese un numero")
        numero_ingresado = int(numero_ingresar)
        numero_par = 0
        cantidad_pares = 0
        for numeros_pares in range(numero_ingresado):
            numero_par = numero_par + 2
            if(numero_par > numero_ingresado):
                alert("Numeros Pares", "La cantidad de numeros pares son: " + str(cantidad_pares))
                break
            cantidad_pares = cantidad_pares + 1
            alert("Numeros Pares", numero_par)
                
            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()