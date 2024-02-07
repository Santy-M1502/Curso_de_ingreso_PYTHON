import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        python_contador = 0
        javascript_contador = 0
        asp_net_contador = 0

        femenino_cantidad = 0
        masculino_cantidad = 0
        no_binario_cantidad = 0
        femenino_edades = 0
        masculino_edades = 0
        no_binario_edades = 0

        cantidad_postulantes = 0

        postulante_pedido_especifico = 0
        nombre_jr_menor = "Nadie"
        edad_jr_menor = 0

        for programadores in range(10):
            
            nombre = prompt("UTN Software Factory", "Ingrese su nombre")
            if not nombre:
                break
            edad_texto = prompt("UTN Software Factory", "Ingrese su edad")
            if not edad_texto:
                break
            edad_numero = int(edad_texto)
            genero = prompt("UTN Software Factory", "Ingrese su genero(F-M-NB)")
            if not genero:
                break
            tecnologia = prompt("UTN Software Factory", "Ingrese la tecnologia con la que trabaja(PYTHON-JS-ASP.NET)")
            if not tecnologia:
                break
            puesto = prompt("UTN Software Factory", "Ingrese el puesto que busca(Jr-Ssr-Sr)")
            if not puesto:
                break
            cantidad_postulantes = cantidad_postulantes + 1

            if(genero == "NB" or "JS" and tecnologia == "ASP.NET" and 25 < edad_numero < 40 and puesto == "Ssr"):
                postulante_pedido_especifico = postulante_pedido_especifico + 1
            if(edad_numero < edad_jr_menor or edad_jr_menor == 0):
                del nombre_jr_menor
                del edad_jr_menor
                nombre_jr_menor = nombre
                edad_jr_menor = edad_numero
            if(genero == "F"):
                femenino_edades = femenino_edades + edad_numero
                femenino_cantidad = femenino_cantidad + 1
            if(genero == "M"):
                masculino_edades = masculino_edades + edad_numero
                masculino_cantidad = masculino_cantidad + 1
            if(genero == "NB"):
                no_binario_edades = no_binario_edades + edad_numero
                no_binario_cantidad = no_binario_cantidad + 1
            if(tecnologia == "PYTHON"):
                python_contador = python_contador + 1
            if(tecnologia == "JS"):
                javascript_contador = javascript_contador + 1
            if(tecnologia == "ASP.NET"):
                asp_net_contador = asp_net_contador + 1

        alert("UTN Software Factory", "La cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr es: " + str(postulante_pedido_especifico))
        alert("UTN Software Factory", "El nombre del postulante Jr con menor edad es: " + nombre_jr_menor)
        if masculino_cantidad != 0:
            alert("UTN Software Factory", "El promedio de edad de las personas de genero masculino es: " + str(masculino_edades / masculino_cantidad))
        if femenino_cantidad != 0:
            alert("UTN Software Factory", "El promedio de edad de las personas de genero femenino es: " + str(femenino_edades / femenino_cantidad))
        if no_binario_cantidad != 0:
            alert("UTN Software Factory", "El promedio de edad de las personas de genero no binario es: " + str(no_binario_edades / no_binario_cantidad))
        if(python_contador > javascript_contador and python_contador > asp_net_contador):
            alert("UTN Software Factory", "La tecnologia con mas postulantes es PYTHON")
        if(javascript_contador > python_contador and javascript_contador > asp_net_contador):
            alert("UTN Software Factory", "La tecnologia con mas postulantes es JavaScript")
        if(asp_net_contador > javascript_contador and asp_net_contador > python_contador):
            alert("UTN Software Factory", "La tecnologia con mas postulantes es ASP.NET")
        alert("UTN Software Factory", "Porcentaje genero masculino" + str(masculino_cantidad * 100 / cantidad_postulantes) + "%")
        alert("UTN Software Factory", "Porcentaje genero femenino" + str(femenino_cantidad * 100 / cantidad_postulantes) + "%")
        alert("UTN Software Factory", "Porcentaje genero no binario" + str(no_binario_cantidad * 100 / cantidad_postulantes) + "%")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
