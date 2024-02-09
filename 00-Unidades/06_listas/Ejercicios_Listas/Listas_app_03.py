import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: listas_03
---
Enunciado:
Al presionar el botón 'MÁXIMO' se analizará la lista_datos a efectos de determinar cuál es el número 
más grande allí contenido el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÁXIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        contador = 0
        for maximo_lista in self.lista_datos:
            if(maximo_lista > contador):
                contador = maximo_lista
        alert("Numero mas grande", contador)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()