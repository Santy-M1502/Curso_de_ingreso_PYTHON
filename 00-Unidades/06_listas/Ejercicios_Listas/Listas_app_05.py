import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: listas_05
---
Enunciado:
Al presionar el botón 'INGRESAR' se le solicitará al usuario que ingrese:
    Edad - Validar (Entre 15 y 90 años).
    Genero - Validar (Femenino/Masculino/No Binario).
Luego del ingreso, al presionar el boton 'INFORMAR' mostrar por Dialog Alert:
    A. Promedio de edad de los masculinos.
    B. Porcentaje de femeninos mayores de 18 respecto al total de personas.
    C. Porcentaje de personas de cada genero.
    D. Informar edad y genero de la persona con menor edad, puede ser mas de una.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label = customtkinter.CTkLabel(master=self, text="Edad")
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Genero")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_genero = customtkinter.CTkEntry(master=self)
        self.txt_genero.grid(row=1, column=1)

        self.btn_ingresar = customtkinter.CTkButton(master=self, text="INGRESAR", command=self.btn_ingresar_on_click)
        self.btn_ingresar.grid(row=2, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(master=self, text="INFORMAR", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=3, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.lista_edades = []
        self.lista_generos = []


    def btn_ingresar_on_click(self):
        edad_ingresado = int(self.txt_edad.get())
        if edad_ingresado < 15 or edad_ingresado > 90:
            alert("UTN FRA", "Ingrese una valor mayor a 15 y menor a 90")
            self.txt_edad.delete(0, 1000)
        else:
            self.lista_edades.append(edad_ingresado)

        genero_ingresado = self.txt_genero.get()
        if not genero_ingresado:
            alert("UTN FRA", "Ingrese una valor valido")
        else:
            self.lista_generos.append(genero_ingresado)

    def btn_informar_on_click(self):
        cantidad_total = len(self.lista_generos)
        edad_menor = 0
        genero_menor = []

        cantidad_masculino = 0
        cantidad_femenino = 0
        cantidad_no_binario = 0
        cantidad_f_mayor = 0

        edad_masculino = 0
        edad_femenino = 0
        edad_no_binario = 0
        lista = zip(self.lista_edades, self.lista_generos)
        for info in lista:
            if info[1] == "Masculino":
                cantidad_masculino += 1
                edad_masculino += info[0]
            if info[1] == "Femenino":
                cantidad_femenino += 1
                edad_femenino += info[0]
            if info[1] == "No Binario":
                cantidad_no_binario += 1
                edad_no_binario += info[0]
            if info[0] >= 18 and info[1] == "Femenino":
                cantidad_f_mayor += 1
            if info[0] <= edad_menor or edad_menor == 0:
                edad_menor = info[0]
                genero_menor.append(info[1])
        
        promedio_masculino = edad_masculino / cantidad_masculino
        porcentaje_f_mayor = cantidad_f_mayor * 100 / cantidad_total
        porcentaje_m = cantidad_masculino * 100 / cantidad_total
        porcentaje_f =cantidad_femenino * 100 / cantidad_total
        porcentaje_nb =cantidad_no_binario * 100 / cantidad_total
        
        alert("UTN FRA", f"El promedio de las edades de los hombres es: {promedio_masculino}")
        alert("UTN FRA", f"El porcentaje de mujeres mayores son: {porcentaje_f_mayor}")
        alert("UTN FRA", f"El porcentaje de hombres es: {porcentaje_m}")
        alert("UTN FRA", f"El porcentaje de mujeres es: {porcentaje_f}")
        alert("UTN FRA", f"El porcentaje de no binarios es: {porcentaje_nb}")
        alert("UTN FRA", f"Las personas con la edad mas baja son de genero: {genero_menor}, y tienen {edad_menor} años")





        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()