#Codificar un programa en Python utilizando funciones que permita
# recibir: Nombre, edad, País, Equipo y tiempo en minutos de
# múltiples ciclistas. El software estará en la capacidad de calcular y
# mostrar en pantalla cual fue el ciclista más rápido
# Recomendaciones: 
# Programar menú (1. Agregar ciclista, 2. Ver resultados) +2 
from itertools import product
import os
os.system ("cls")
i=1
ciclistas=[

]
print("***MENU***")
print("(1) Crear datos del ciclista")
print("(2) Mostrar listado de ciclista")
print("(3) Buscar por codigo y editar")
print("(4) Buscar por codigo y eliminar")
print("(5) Limpiar pantalla")
print("(6) Ciclista más rápido")
print("(0) Terminar")
while(i!=0):
    #diccionario ciclista
    ciclista={

    }
    i=int(input("Digita una opcion: "))
    if(i==1):
        print("Crear datos del ciclista")
        #append
        # Nombre, edad, País, Equipo y tiempo en minutos
        ciclista['codigo']=input("Digita el codigo del ciclista: ")
        ciclista['nombre']=input("Digita el nombre del ciclista: ")
        ciclista['edad']=int(input(f"Digita el edad del ciclista: "))
        ciclista['pais']=input("Digita el país del ciclista: ")
        ciclista['equipo']=input("Digita el equipo del ciclista: ")
        ciclista['tiempo']=int(input(f"Digita el tiempo del ciclista: "))
        ciclistas.append(ciclista)
        print("***MENU***")
        print("(1) Crear datos del ciclista")
        print("(2) Mostrar listado de ciclistas")
        # print("(3) Buscar por codigo y editar")
        # print("(4) Buscar por codigo y eliminar")
        print("(5) Limpiar pantalla")
        print("(6) Ciclista más rápido")
        print("(0) Terminar")
    elif(i==2):
        print("Mostrar listado de ciclistas")        
        for elemento in ciclistas:           
            print(elemento)
            print("")
        print("***MENU***")
        print("(1) Crear datos del ciclista")
        print("(2) Mostrar listado de ciclistas")
        # print("(3) Buscar por codigo y editar")
        # print("(4) Buscar por codigo y eliminar")
        print("(5) Limpiar pantalla")
        print("(6) Ciclista más rápido")
        print("(0) Terminar")
    elif(i==3):
        print("Buscar por codigo y editar")
        codigo=input(f"Digita el codigo del ciclista: ")        
        for elemento in ciclistas:
            if(elemento['codigo'] == codigo):
                print("encontrado")
                print(elemento)
                precioNuevo=int(input(f"Digita el precio del ciclista: "))
                elemento['precio']=precioNuevo  
        i=2
        print("***MENU***")
        print("(1) Crear datos del ciclista")
        print("(2) Mostrar listado de ciclistas")
        # print("(3) Buscar por codigo y editar")
        # print("(4) Buscar por codigo y eliminar")
        print("(5) Limpiar pantalla")
        print("(6) Ciclista más rápido")
        print("(0) Terminar")   
    elif(i==4):
        print("Buscar por codigo y eliminar")
        codigo=input(f"Digita el codigo del ciclista: ")        
        for elemento in ciclistas:
            if(elemento['codigo'] == codigo):
                print("encontrado")
                print(elemento)
                sw=1
                productos.remove(elemento) 
            else:
                sw=0             
        if(sw==0):
            print("NO ESTA EL REGISTRO (ciclistas(ciclista[]))")  
    elif(i==5):
        os.system ("cls")
        print("***MENU***")
        print("(1) Crear datos del ciclista")
        print("(2) Mostrar listado de ciclistas")
        # print("(3) Buscar por codigo y editar")
        # print("(4) Buscar por codigo y eliminar")
        print("(5) Limpiar pantalla")
        print("(6) Ciclista más rápido")
        print("(0) Terminar")
    elif(i==6):
        os.system ("cls")
        tiempo_aux=10000
        for elemento in ciclistas:
            if(elemento['tiempo'] < tiempo_aux):
                tiempo_aux=elemento['tiempo']
        print(f"El mejor tiempo fue:{tiempo_aux} ")
        print("") 
        i=2
        print("***MENU***")
        print("(1) Crear datos del ciclista")
        print("(2) Mostrar listado de ciclistas")
        # print("(3) Buscar por codigo y editar")
        # print("(4) Buscar por codigo y eliminar")
        print("(5) Limpiar pantalla")
        print("(6) Ciclista más rápido")
        print("(0) Terminar")
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