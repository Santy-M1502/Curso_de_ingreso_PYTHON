import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: listas_02
---
Enunciado:
Al presionar el botón 'Calcular' se deberá sumar todos los numeros de la lista, mostrar el resultado de la sumatoria y el promedio por Dialog Alert . 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]
        
    def btn_calcular_on_click(self):
        suma_numeros = 0
        cantidad_numeros = 0
        for numero in self.lista_datos:
            cantidad_numeros += 1
            suma_numeros += numero
        promedio = suma_numeros / cantidad_numeros

        alert("Numeros", "La suma de los numeros en la lista es: " + str(suma_numeros))
        alert("Numeros", "El promedio del resultado anterior es: " + str(promedio))

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()