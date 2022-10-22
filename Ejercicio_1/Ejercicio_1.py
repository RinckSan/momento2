#Codificar un programa en Python utilizando funciones que permita
# recibir: Nombre, edad, País, Equipo y tiempo en minutos de
# múltiples ciclistas. El software estará en la capacidad de calcular y
# mostrar en pantalla cual fue el ciclista más rápido
# Recomendaciones: 
# Programar menú (1. Agregar ciclista, 2. Ver resultados) +2 

from funcion0 import crearMenu
from funcion1 import crearCiclista
import os
os.system ("cls")
i=1
ciclistas=[

]
crearMenu()
while(i!=0):
    #diccionario ciclista
    ciclista={

    }
    i=int(input("Digita una opcion: "))
    if(i==1):
        print("Crear datos del ciclista")
        #append
        # Nombre, edad, País, Equipo y tiempo en minutos
        ciclista=crearCiclista()
        ciclistas.append(ciclista)
        crearMenu()
    elif(i==2):
        print("Mostrar listado de ciclistas")        
        for elemento in ciclistas:           
            print(elemento)
            print("")
        crearMenu()         
    elif(i==3):
        os.system ("cls")
        crearMenu()
    elif(i==4):
        os.system ("cls")
        tiempo_aux=10000
        for elemento in ciclistas:
            if(elemento['tiempo'] < tiempo_aux):
                tiempo_aux=elemento['tiempo']
        print(f"El mejor tiempo fue:{tiempo_aux} ")
        print("") 
        i=2
        crearMenu()
        #pendiente calcular el mas rápido   
    elif(i==0):
        break
    else:
        print("Digite una opcion valida.")
else:
    print("Digite una opcion valida.")











#tupla productos con un diccionario producto adentro.
# productos[
#           producto
#                      {'codigo': 'a1', 'nombre': 'manzana', 'precio': 1000},
#                      {'codigo': 'a2', 'nombre': 'banano', 'precio': 2000},
#                      {'codigo': 'a3', 'nombre': 'papaya', 'precio': 5000}
#          ]