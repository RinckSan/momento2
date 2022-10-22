def crearCiclista():
    
    #diccionario ciclista
    ciclista={

    }
# Nombre, edad, País, Equipo y tiempo en minutos
    ciclista['codigo']=input("Digita el codigo del ciclista: ")
    ciclista['nombre']=input("Digita el nombre del ciclista: ")
    ciclista['edad']=int(input(f"Digita el edad del ciclista: "))
    ciclista['pais']=input("Digita el país del ciclista: ")
    ciclista['equipo']=input("Digita el equipo del ciclista: ")
    ciclista['tiempo']=int(input(f"Digita el tiempo del ciclista: "))
    return(ciclista)