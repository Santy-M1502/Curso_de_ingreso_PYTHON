import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Martinez
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        activador = True
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        
        while(activador):
            valor_ingresar = prompt("Sumas de todo", "Ingrese los valores que desee")
            if valor_ingresar != None and valor_ingresar != "":
                valor_ingresado = int(valor_ingresar)
            else:
                break
            if(valor_ingresado >= 0):
                suma_positivos = suma_positivos + valor_ingresado
                contador_positivos = contador_positivos + 1
            elif(valor_ingresado <= 0):
                suma_negativos = suma_negativos - valor_ingresado
                contador_negativos = contador_negativos + 1
            else:
                contador_ceros = contador_ceros + 1

        diferencia_pos_neg = contador_positivos - contador_negativos
        
        mensaje = f"Resultado \n la suma acumuladda de los negativos es: {suma_negativos} \n La suma acumulada de los positivos es: {suma_positivos} \n La cantidad de numeros negativos es: {contador_negativos} \n La cantidad de numeros positivos es: {contador_positivos} \n La cantidad de ceros es: {contador_ceros} \n La diferencia entre la cantidad de numeros positivos y negativos es: {diferencia_pos_neg}"
        alert("UTN FRA", mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
