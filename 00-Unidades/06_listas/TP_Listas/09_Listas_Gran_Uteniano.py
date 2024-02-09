import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
TP: Gran_uteniano
---
Enunciado:
INTRODUCCION:
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de 
los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está 
en la placa esta semana por haber ganado la inmunidad.

ENUNCIADO:
Cada televidente que vota deberá ingresar:
* Nombre del votante
* Edad del votante (debe ser mayor a 13)
* Género del votante (Masculino, Femenino, Otro)
* El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario mediante alert:
    A) El promedio de edad de las votantes de género Femenino 
    B) Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
    C) Nombre del votante más joven qué votó a Gianni.
    D) Nombre de cada participante y porcentaje de los votos qué recibió.
    E) El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Gran UTENIANO")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba
        # Cargar o modificar datos en estas listas
        self.lista_nombres = ["Pepe", "Moni","Paola","Coki", "Dardo", "Maria", "Fatiga"]
        self.lista_edades = [55, 45, 18, 17, 49, 45, 14]
        self.lista_genero = ["Masculino", "Femenino", "Femenino", "Masculino", "Masculino", "Femenino", "Otro"] 
        self.lista_participantes = ["Giovanni", "Gianni", "Facundo", "Gianni", "Gianni", "Facundo", "Giovanni"]


    def btn_mostrar_on_click(self):
        #Valores
        datos_general = zip(self.lista_nombres, self.lista_edades, self.lista_genero, self.lista_participantes)

        edad_f = 0
        cantidad_especifica = 0
        voto_joven = []
        edad_joven = 0
        voto_giovanni = 0
        voto_gianni = 0
        voto_facundo = 0
        cantidad_votantes = 0
        cantidad_f = 0

        #Condiciones y datos
        for informe in datos_general:
            cantidad_votantes += 1
            if("Femenino" in informe[2]):
              cantidad_f += 1
              edad_f += informe[1]
            if "Masculino" in informe[2] and ("Giovanni" in informe[3] or "Facundo" in informe[3]) and 25 <= informe[1] <= 40:
              cantidad_especifica += 1
            if(informe[1] < edad_joven or edad_joven == 0 and informe[3] == "Gianni"):
               voto_joven.append(informe[0])
               edad_joven = informe[1]
            if(informe[3] == "Giovanni"):
               voto_giovanni += 1
            if(informe[3] == "Gianni"):
               voto_gianni += 1
            if(informe[3] == "Facundo"):
               voto_facundo += 1
        
        if(cantidad_f != 0):
           promedio_f = edad_f / cantidad_f
           alert("Gran UTNIANO","El promedio de edad de las personas de genero femenino es: " + str(promedio_f))

           
        #Alerts
        porcentaje_giovanni = voto_giovanni * 100 / cantidad_votantes
        porcentaje_gianni = voto_gianni * 100 / cantidad_votantes
        porcentaje_facundo = voto_facundo * 100 / cantidad_votantes
        alert("Gran UTNIANO","La cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo es: " + str(cantidad_especifica))
        alert("Gran UTNIANO","El/los voto/s mas joven/es que voto a gianni es/son: " + str(voto_joven))
        alert("Gran UTNIANO","El participante Giovanni, recibio una cantidad de votos del " + str(porcentaje_giovanni) + "%")
        alert("Gran UTNIANO","El participante Gianni, recibio una cantidad de votos del " + str(porcentaje_gianni) + "%")
        alert("Gran UTNIANO","El participante Facundo, recibio una cantidad de votos del " + str(porcentaje_facundo) + "%")
        if(voto_giovanni > voto_facundo and voto_giovanni > voto_gianni):
           alert("Gran UTNIANO","El participante que abandona la casa es Giovanni")
        elif(voto_facundo > voto_giovanni and voto_facundo > voto_gianni):
           alert("Gran UTNIANO","El participante que abandona la casa es Facundo")
        elif(voto_gianni > voto_facundo and voto_gianni > voto_giovanni):
           alert("Gran UTNIANO","El participante que abandona la casa es Giovanni")
        else:
           alert("Gran UTNIANO", "Hubo empate!!!")
              
              

           


    def btn_cargar_on_click(self):

        #Toma de valores
        while(True):
         nombre = prompt("Gran UTNIANO","Ingrese su nombre")
         if not nombre:
            break
         edad_texto = prompt("Gran UTNIANO","Ingrese su edad")
         if not edad_texto:
            break
         edad = int(edad_texto)
         if(edad < 13):
            break
         genero = prompt("Gran UTNIANO","Ingrese su genero(Masculino, Femenino u Otro)")
         if not genero:
            break
         participante = prompt("Gran UTNIANO","Ingrese el nombre del participante que le dara su voto negativo(Giovanni, Gianni, Facundo)")
         if not participante:
            break
         
         self.lista_nombres.append(nombre)
         self.lista_edades.append(edad)
         self.lista_genero.append(genero)
         self.lista_participantes.append(participante)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()