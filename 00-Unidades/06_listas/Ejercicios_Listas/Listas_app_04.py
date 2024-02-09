
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: listas_04
---
Enunciado:
Al presionar el botón 'INGRESAR' se le solicitará al usuario que ingrese:
    Edad.
    Genero.
Luego del ingreso, al presionar el boton 'INFORMAR' mostrar por Dialog Alert:
    A. Promedio de edad de los hombres.
    B. Porcentaje de mujeres mayores de 18 respecto al total de personas. 
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
        edad_texto = self.txt_edad.get()
        edad_numero = int(edad_texto)
        self.lista_edades.append(edad_numero)
        self.txt_edad.delete(0, 1000)

        genero_ingresado = self.txt_genero.get()
        self.lista_generos.append(genero_ingresado)
        self.txt_genero.delete(0, 1000)

    def btn_informar_on_click(self):
        cantidad_masculino = 0
        suma_m_edades = 0
        lista_m = zip(self.lista_edades, self.lista_generos)
        for info in lista_m:
            if info[1] == "Masculino":
                suma_m_edades += info[0]
                cantidad_masculino += 1
        promedio_m_edad = suma_m_edades / cantidad_masculino

        lista_f = zip(self.lista_edades, self.lista_generos)
        contador_total = len(self.lista_edades)
        cantidad_femenino_mayor = 0
        for info in lista_f:
            if info[0] >= 18 and info[1] == "Femenino":
                cantidad_femenino_mayor += 1
        porcentaje_femenino_mayor = cantidad_femenino_mayor * 100  / contador_total

        print(cantidad_masculino)
        print(suma_m_edades)
        print(promedio_m_edad)

        alert("UTN FRA",f"El promedio de edad entre los hombres es {promedio_m_edad}")
        alert("UTN FRA",f"El porcentaje de mujeres mayores es {porcentaje_femenino_mayor}")


    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()