import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Simulacro Turno Mañana
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:
Nombre del votante
Edad del votante (debe ser mayor a 13)
Género del votante (Masculino, Femenino, Otro)
El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:
El promedio de edad de las votantes de género Femenino 
Del votante más viejo, su nombre.
Nombre del votante más joven qué votó a Gianni.
Nombre de cada participante y porcentaje de los votos qué recibió.
El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_f =0
        acumulador_edad_f = 0

        edad_viejo = 0
        nombre_viejo = None
        banderin_v = True

        edad_joven_g = 0
        nombre_joven_g = None
        banderin_j = True

        contador_giovanni = 0
        contador_gianni = 0
        contador_esteban = 0

        while(True):
            nombre_votante = prompt("Gran Utniano", "Ingrese su nombre")
            while(nombre_votante == None or nombre_votante == ""):
                nombre_votante = prompt("Gran Utniano", "Reingrese su nombre")
            
            edad_votante_pre = prompt("Gran Utniano", "Ingrese su edad")
            while(edad_votante_pre == None or edad_votante_pre == ""    ):
                edad_votante_pre = prompt("Gran Utniano", "Ingrese un valor para edad")
            edad_votante = int(edad_votante_pre)
            while edad_votante < 13:
                edad_votante_pre = prompt("Gran Utniano", "Debe ser mayor de trece años")
                edad_votante = int(edad_votante_pre)
            
            genero_votante = prompt("Gran Utniano", "Ingrese su genero")
            while genero_votante != "Masculino" and genero_votante != "Femenino" and genero_votante != "Otro" or (genero_votante == None or genero_votante == ""):
                genero_votante = prompt("Gran Utniano", "Debe ingresar uno de los siguientes valores(Masculino, Femenino, Otro)")

            candidato_votante = prompt("Gran Utniano", "Ingrese a quien da su voto(Giovanni, Gianni y Esteban)")
            while (candidato_votante != "Giovanni" and candidato_votante != "Gianni" and candidato_votante != "Esteban" or (candidato_votante == None or candidato_votante == "")):
                candidato_votante = prompt("Gran Utniano", "Ingrese uno de los siguientes participantes (Giovanni, Gianni y Esteban)")
            
            #1)El promedio de edad de las votantes de género Femenino 
            if genero_votante == "Femenino":
                contador_f += 1
                acumulador_edad_f += edad_votante

            #2)Del votante más viejo, su nombre.
            if edad_votante > edad_viejo or banderin_v == True:
                edad_viejo = edad_votante
                nombre_viejo = nombre_votante
                banderin_v == False

            #3)Nombre del votante más joven qué votó a Gianni.
            if (edad_votante < edad_joven_g and candidato_votante == "Gianni") or banderin_j == True:
                edad_joven_g = edad_votante
                nombre_joven_g = nombre_votante
                banderin_j = False
                print(banderin_j)


            #4)Nombre de cada participante y porcentaje de los votos qué recibió.
            match(candidato_votante):
                case "Giovanni":
                    contador_giovanni += 1
                case "Gianni":
                    contador_gianni += 1
                case "Esteban":
                    contador_esteban += 1

            seguir = question("Gran Utniano", "¿Quiere ingresar otro voto?")
            if seguir == False:
                break
        
        #4)Nombre de cada participante y porcentaje de los votos qué recibió.
        contador_total = contador_esteban + contador_gianni + contador_giovanni

        porcentaje_giovanni = contador_giovanni * 100 / contador_total
        porcentaje_gianni = contador_gianni * 100 / contador_total
        porcentaje_esteban = contador_esteban * 100 / contador_total
        
        #1)El promedio de edad de las votantes de género Femenino 
        if contador_f != 0:
            promedio_edad_f = acumulador_edad_f / contador_f
            print(promedio_edad_f)
        else:
            print("No se han ingresado generos femeninos")

        
        #2)Del votante más viejo, su nombre.
        print(nombre_viejo, edad_viejo)

        #3)Nombre del votante más joven qué votó a Gianni.
        print(nombre_joven_g, edad_joven_g)
        
        #4)Nombre de cada participante y porcentaje de los votos qué recibió.
        print("Giovanni", porcentaje_giovanni)
        print("Gianni", porcentaje_gianni)
        print("Esteban", porcentaje_esteban)
        
        #5)El nombre del participante que debe dejar la casa (El que tiene más votos)
        if contador_esteban > contador_gianni and contador_esteban > contador_giovanni:
            print("El participante que debe abandonar la casa es Esteban")
        elif contador_gianni > contador_giovanni:
            print("El participante que debe abandonar la casa es Gianni")
        else:
            print("El participante que debe abandonar la casa es Giovanni")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()