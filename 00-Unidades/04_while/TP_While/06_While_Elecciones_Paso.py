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

        cantidad_mas_votos = 0

        cantidad_menos_votos = 0
        cantidad_candidatos = 0
        edades = 0
        cantidad_votos_total = 0
        banderin = True
        while(True):
            sig_candidato = question("Las Paso", "¿Ingresar otro candidato?")
            if sig_candidato == False:
                break
            nombre_candidato = prompt("Las Paso", "Ingrese el nombre")
            while(True):          
                if nombre_candidato != None and nombre_candidato != "":
                    break
                else:
                    nombre_candidato = prompt("Las Paso", "Ingrese un nombre valido")

            edad_texto = prompt("Las Paso", "Ingrese la edad")
            while(True):
                if edad_texto != None and edad_texto != "":
                   if edad_texto.isdigit():
                        edad_candidato = int(edad_texto)
                        if edad_candidato < 26:
                            edad_texto = prompt("Las Paso", "Ingrese un valor mayor a 26")
                        else:
                            break
                else:
                    edad_texto = prompt("Las Paso", "Ingrese un valor mayor a 26")
        
            cantidad_texto = prompt("Las Paso", "Ingrese la cantidad de votos")
            while(True):
                if cantidad_texto != None and cantidad_texto != "":
                    if cantidad_texto.isdigit():
                        cantidad_votos = int(cantidad_texto)
                        if cantidad_votos < 0:
                            cantidad_texto = prompt("Las Paso", "Ingrese un valor mayor a 0")
                        else:
                            if cantidad_votos > cantidad_mas_votos or banderin:
                                candidato_mas_votos = nombre_candidato
                                cantidad_mas_votos = cantidad_votos
                            if cantidad_votos < cantidad_menos_votos or banderin:
                                edad_menos_votos = edad_candidato
                                candidato_menos_votos = nombre_candidato
                                cantidad_menos_votos = cantidad_votos
                                banderin = False 
                            break
                else:
                    cantidad_texto = prompt("Las Paso", "Ingrese un valor mayor a 0")
   

            cantidad_votos_total += cantidad_votos
            edades += edad_candidato
            cantidad_candidatos += 1
               
            if cantidad_texto == None or cantidad_texto == "":
                break

            
        if cantidad_candidatos != 0:
            promedio_edades = edades / cantidad_candidatos
            alert("Las Paso", f"El promedio de edad de los candidatos es: {promedio_edades}")

        alert("Las Paso", f"El candidato  con mas votos es: {candidato_mas_votos}, tuvo {cantidad_mas_votos} votos")
        alert("Las Paso", f"El candidato  con menos votos es: {candidato_menos_votos}, tuvo {cantidad_menos_votos} votos, y tiene {edad_menos_votos} años")
        alert("Las Paso", f"La cantidad total de votos fue de: {cantidad_votos_total}")
            

        
            




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
