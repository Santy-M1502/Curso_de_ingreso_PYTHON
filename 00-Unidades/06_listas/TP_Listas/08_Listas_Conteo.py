import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
TP: Listas_conteo
---
Enunciado:
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

Bonus:
    i. El listado de numeros pares
    j. Que se ingreso mas? positivos, negativos o ceros

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista_numeros = []

    def btn_comenzar_ingreso_on_click(self):
        while(True):
            numero_ingresar = prompt("UTN FRA", "Ingrese todos los numeros que usted desee")
            if not numero_ingresar:
                break
            numero_ingresado = int(numero_ingresar)
            self.lista_numeros.append(numero_ingresado)

    def btn_mostrar_estadisticas_on_click(self):

        #Valores
        suma_negativos = 0
        suma_positivos = 0
        cantidad_negativos = 0
        cantidad_positivos = 0
        cantidad_ceros = 0
        minimo_negativo = 0
        maximo_positivo = 0
        numeros_pares = []
        for numeros in self.lista_numeros:
            
            #Condiciones
            if numeros > 0:
                suma_positivos += numeros
                cantidad_positivos += 1
                if numeros > maximo_positivo or maximo_positivo == 0:
                    maximo_positivo = numeros
            elif numeros < 0:
                suma_negativos += numeros
                cantidad_negativos += 1
                if numeros < minimo_negativo or minimo_negativo == 0:
                    minimo_negativo = numeros
            elif 0 in numeros:
                cantidad_ceros += 1
            if(numeros % 2 == 0):
                numeros_pares.append(numeros)

        promedio_negativo = suma_negativos / cantidad_negativos

        #Alerts
        alert("UTN FRA", "La suma acumulada de los numeros negativos es: " + str(suma_negativos))
        alert("UTN FRA", "La suma acumulada de los numeros positivos es: " + str(suma_positivos))
        alert("UTN FRA", "La cantidad de numeros negativos es: " + str(cantidad_negativos))
        alert("UTN FRA", "La cantidad de numeros positivos es: " + str(cantidad_positivos))
        alert("UTN FRA", "La cantidad de ceros es: " + str(cantidad_ceros))
        alert("UTN FRA", "El numero mas bajo es: " + str(minimo_negativo))
        alert("UTN FRA", "El numero mas alto es: " + str(maximo_positivo))
        alert("UTN FRA", "Los numeros pares son: " + str(numeros_pares))
        if(cantidad_ceros > cantidad_negativos and cantidad_ceros > cantidad_positivos):
            alert("El cero fue el numero mas ingresado")
        elif(cantidad_positivos > cantidad_ceros and cantidad_positivos > cantidad_negativos):
            alert("El cero fue el numero mas ingresado")
        elif(cantidad_negativos > cantidad_ceros and cantidad_negativos > cantidad_positivos):
            alert("El cero fue el numero mas ingresado")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
