import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_masculino_IOT_IA = 0

        tecnologia_mas_votos = None

        iot_cantidad = 0
        ia_cantidad = 0
        ra_rv_cantidad = 0

        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0

        contador_iot_edad = 0

        contador_femenino_ia = 0
        acumulador_femenino_edad_ia = 0

        banderin = True
        edad_menor_edad = None
        nombre_menor_edad = None
        genero_menor_edad = None

        while(True):
            nombre_empleado = input("Ingrese el nombre del empleado ")
            while(nombre_empleado == None or nombre_empleado == ""):
                nombre_empleado = input("Reingrese el nombre del empleado ")

            edad_empleado_texto = input("Ingrese la edad del empleado ")
            edad_empleado_numero = int(edad_empleado_texto)
            while edad_empleado_numero < 18:
                edad_empleado_texto = input("Ingrese la edad del empleado ")
                edad_empleado_numero = int(edad_empleado_texto)

            genero_empleado = input("Ingrese el genero del empleado ")
            while(genero_empleado != "Masculino" and genero_empleado != "Femenino" and genero_empleado != "Otro"):
                genero_empleado = input("UTN tecnologies", "Reingrese el genero del empleado ")

            tecnologia_empleado = input("Ingrese la tecnologia a desarrollar ")
            while(tecnologia_empleado != "IA" and tecnologia_empleado != "RV" and tecnologia_empleado != "RA" and tecnologia_empleado != "IOT"):
                tecnologia_empleado = input("Reingrese la tecnologia a desarrollar(Asegurese de usar mayusculas) ")
            

        #!X 2) - Tecnología que mas se votó.
            match tecnologia_empleado:
                case "IA":
                    ia_cantidad += 1
                case "IOT":
                    iot_cantidad += 1
                    if (edad_empleado_numero >= 18 and edad_empleado_numero <= 25) or (edad_empleado_numero >= 33 and edad_empleado_numero <= 42):
                        contador_iot_edad += 1
                case _:
                    ra_rv_cantidad += 1
                    if banderin == True or edad_empleado_numero < edad_menor_edad:
                        edad_menor_edad = edad_empleado_numero
                        nombre_menor_edad = nombre_empleado
                        genero_menor_edad = genero_empleado
                        banderin = False
        
        #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
            match genero_empleado:
                case "Masculino":
                    if((tecnologia_empleado == "IOT" or tecnologia_empleado == "IA") and edad_empleado_numero > 25 and edad_empleado_numero < 50):
                        contador_masculino_IOT_IA += 1
                    contador_masculino += 1
                case "Femenino":
                    contador_femenino += 1
                    if tecnologia_empleado == "IA":
                        contador_femenino_ia += 1
                        acumulador_femenino_edad_ia += edad_empleado_numero
                case "Otro":
                    contador_otro += 1

            seguir = question("UTN tecnologies", "¿Desea ingresar datos de otro empleado? ")
            if seguir == False:
                break
        
        if ia_cantidad > iot_cantidad and ia_cantidad > ra_rv_cantidad:
            tecnologia_mas_votos = "IA"
        elif iot_cantidad > ra_rv_cantidad:
            tecnologia_mas_votos = "IOT"
        else:
            tecnologia_mas_votos = "RA/RV"
        
        #!X 3) - Porcentaje de empleados por cada genero
        
        total_empleados = contador_masculino + contador_femenino + contador_otro
        porcentaje_masculino = contador_masculino * 100 / total_empleados
        porcentaje_femenino = contador_femenino * 100 / total_empleados
        porcentaje_otro = 100 - porcentaje_masculino - porcentaje_femenino

        #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.

        porcentaje_iot_edad = contador_iot_edad * 100 / total_empleados

        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        
        if contador_femenino_ia != 0:
            promedio_edad_femenino_ia = acumulador_femenino_edad_ia / contador_femenino_ia
        else:
            promedio_edad_femenino_ia = "No se ingreso ningun femenino que cumpla con la condicion"

        #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

        print(f"La cantidad de hombres que eligio IOT/IA y tiene entre 25 y 50 años es: {contador_masculino_IOT_IA}")
        print(f"La tecnologia mas elegida fue: {tecnologia_mas_votos}")
        print(f"Porcentajes:\n\tEl porcentaje de genero masculino es: {porcentaje_masculino}\n\tEl porcentaje de genero femenino es: {porcentaje_femenino}\n\tEl porcentaje de genero otro es: {porcentaje_otro}")
        print(f"El porcentaje de empleados que eligieron IOT y tienen entre 18 y 25 o 33 y 42 años es: {porcentaje_iot_edad}")
        print(f"{promedio_edad_femenino_ia}")
        if banderin == True:
            print(f"{nombre_menor_edad}{genero_menor_edad}{edad_menor_edad}")
        else:
            print("No se encontro minimo para RV/RA")

        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
