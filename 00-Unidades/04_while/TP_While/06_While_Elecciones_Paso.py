import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        activador = True
        nombre_masvotos = "Nadie"
        nombre_menosvotos = "Nadie"
        mayor_voto = 0
        menor_voto = 0
        promedio_edades = 0
        total_votos = 0
        total_candidatos = 0
        total_edades = 0
        nombre_candidato = prompt("Las paso", "Ingrese nombre de candidato")
        edad_texto = prompt("Las paso", "Ingrese edad de candidato")
        edad_numero = int(edad_texto)
        cantidad_votos_texto = prompt("Las paso", "Ingrese la cantidad de votos de candidato")
        cantidad_votos_numero = int(cantidad_votos_texto)

        nombre_masvotos = nombre_candidato
        nombre_menosvotos = nombre_candidato
        total_candidatos = total_candidatos + 1
        total_votos = total_votos + cantidad_votos_numero
        total_edades = total_edades + edad_numero
        menor_voto = cantidad_votos_numero
        mayor_voto = cantidad_votos_numero
    
        while(activador):

            nombre_candidato = prompt("Las paso", "Ingrese nombre de candidato")
            if not nombre_candidato:
                break

            edad_texto = prompt("Las paso", "Ingrese edad de candidato")
            edad_numero = int(edad_texto)
            if(edad_numero < 25):
                break

            cantidad_votos_texto = prompt("Las paso", "Ingrese la cantidad de votos de candidato")
            cantidad_votos_numero = int(cantidad_votos_texto)
            if(cantidad_votos_numero < 0):
                break

            total_votos = total_votos + cantidad_votos_numero
            total_candidatos = total_candidatos + 1
            total_edades = total_edades + edad_numero

            if(cantidad_votos_numero >= 0 and cantidad_votos_numero <= mayor_voto):
                menor_voto = cantidad_votos_numero
                del nombre_menosvotos
                nombre_menosvotos = nombre_candidato

            if(cantidad_votos_numero > mayor_voto):
                mayor_voto = cantidad_votos_numero
                del nombre_masvotos
                nombre_masvotos = nombre_candidato

 
        promedio_edades = (promedio_edades + total_edades) / total_candidatos
        alert("Votaciones Presidenciales", "Candidato con mas votos: " + nombre_masvotos)
        alert("Votaciones Presidenciales", "Candidato con menos votos: " + nombre_menosvotos + " con " + str(menor_voto))
        alert("Votaciones Presidenciales", "Promedio de sus edades: " + str(promedio_edades))
        alert("Votaciones Presidenciales", "Total de votos emitidos: " + str(total_votos))


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
