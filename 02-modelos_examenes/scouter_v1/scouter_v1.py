# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings


'''
################# INTRODUCCION #################
#? El presentador del torneo de artes marciales quiere que desarrolles un modelo prototipico 
#? de scouter (un detector basicamente) para ver ciertas metricas de los participantes.
#? de cualquier parte del universo, es por eso que deberas realizar la carga 
#? de 10 participantes.
'''
NOMBRE = '' # Santiago Gabriel Martinez
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Participantes" para poder cargar 10 luchadoras/es.
Los datos que deberas pedir para los luchadoras/es son:
    * El nombre del luchador/a.
    * El tipo de raza (Terricola , Namekiano, Alienigena , Saiyajin).
    * La cantidad de poder del participante (entre 100 y 5000).
    
B)  Al presionar el boton "Mostrar Informe 1" se deberan listar los participantes
        y su posicion en la lista (por terminal), 
        adicionalmente mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Cantidad de luchadores Terricolas.
    #! 1) - Cantidad de luchadores Alienigenas.
    #! 2) - Nombre, Raza y Poder del luchador mas fuerte.
    #! 3) - Nombre, Raza y Poder del luchador mas debil. #ESTE#
    #! 4) - Cantidad de luchadores con mas de 2500 de poder.
    #! 5) - Cantidad de luchadores con menos de 2500 de poder.
    #! 6) - Raza que mas luchadores posea inscriptos. #ESTE#
    #! 7) - Raza que menos luchadores posea inscriptos.
    #! 8) - el promedio de poder de todos los luchadores inscriptos.
    #! 9) - el promedio de poder de todos los luchadores Saiyajines.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Scouter de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Scouter de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/scouter_v1/UTN_Scouter_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Participantes", command=self.btn_cargar_participantes_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.lista_nombre_participantes = [
            "Vegeta", "Goku", "Yamcha", "Pikoro", "Gohan",
            "Frieza", "Appule", "Krilin", "Roshi", "Dende"
        ]
        self.lista_raza_participantes = [
            "Saiyajin", "Saiyajin", "Terricola", "Namekiano", "Saiyajin",
            "Alienigena", "Alienigena", "Terricola", "Terricola", "Namekiano",
        ]
        self.lista_poder_participantes = [
            4900, 4800, 200, 4500, 3500, 5000, 600, 550, 450, 610
        ]


    def btn_cargar_participantes_on_click(self):
        for participante in range(10):
            nombre = prompt("Torneo de Artes Marciales", "Ingrese el nombre del luchador") 
            if not nombre:
                alert("Torneo de Artes Marciales", "Ingrese un valor valido")
                break
            else:
                self.lista_nombre_participantes.append(nombre)
            raza = prompt("Torneo de Artes Marciales", "Ingrese el tipo de raza del luchador(Terricola , Namekiano, Alienigena , Saiyajin)") 
            if not raza:
                alert("Torneo de Artes Marciales", "Ingrese un valor valido")
                break
            else:
                self.lista_raza_participantes.append(raza)
            poder_texto = prompt("Torneo de Artes Marciales", "Ingrese el poder del luchador(entre 100 y 5000)") 
            if not poder_texto:
                break
            else:
                poder = int(poder_texto)
                if(poder < 100 or poder > 5000):
                    alert("Torneo de Artes Marciales", "Ingrese un valor valido")
                    break
                else:
                    self.lista_poder_participantes.append(poder)
        

    def btn_mostrar_informe_1_on_click(self):
        participantes = zip(self.lista_nombre_participantes, self.lista_raza_participantes, self.lista_poder_participantes)
        contador = 0
        for info in participantes:
            contador += 1
            print(contador, info)


    
    def btn_mostrar_informe_2_on_click(self):
        raza = max(set(self.lista_raza_participantes), key=self.lista_raza_participantes.count)
        raza_cantidad = self.lista_raza_participantes.count(raza)
        print("La raza con mayor cantidad de participantes es " + raza + " son: " + str(raza_cantidad))
        alert("Torneo de Artes Marciales", "La raza con mayor cantidad de participantes es " + raza + " son: " + str(raza_cantidad))

        nombre_debil = "Nadie"
        raza_debil = "Ninguno"
        poder_debil = 0
        participantes = zip(self.lista_nombre_participantes, self.lista_raza_participantes, self.lista_poder_participantes)
        for info in participantes:
            if(info[2] < poder_debil or poder_debil == 0):
                nombre_debil = info[0]
                raza_debil = info[1]
                poder_debil = info[2]
        print("El participante mas debil del torneo es " + nombre_debil + " de raza " + raza_debil + " y tiene " + str(poder_debil) + " de poder")
        alert("Torneo de Artes Marciales", "El participante mas debil del torneo es " + nombre_debil + " de raza " + raza_debil + " y tiene " + str(poder_debil) + " de poder")


    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()