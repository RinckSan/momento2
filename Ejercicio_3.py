# El banco de hierro de la isla de Braavos necesita de sus servicios
# para programar un software que permita:
# Almacenar información de un cliente (nombre, apellido, cedula, ciudad)
# Almacenar información de la cuenta (numeroCuenta, saldo)
# Se debe permitir consultar saldo en cualquier momento
# Se debe permitir ingresar o retirar dinero cuando se desee
import os
os.system ("cls")

def crearMenu():
    print("***BANCO DE HIERRO***")
    print("(1) Ver datos de la cuenta")
    print("(2) Ingresar saldo a la cuenta")
    print("(3) Retirar saldo de la cuenta")
    print("(4) Limpiar pantalla")
    print("(5) actualizar datos del cliente")
    print("(0) Terminar")


class Usuario:
  #constructor
  #dentro del constructor son los atributos
  def __init__(self,nombredado,apellidodado,ceduladada,ciudaddada):
    self.nombre=nombredado,
    self.apellido=apellidodado,
    self.cedula=ceduladada,
    self.ciudad=ciudaddada
  #metodos
  def salular(self):
    print(f'hola yo soy {self.nombre}')

class Cuenta:
  #constructor
  #dentro del constructor son los atributos
  def __init__(self,cuentadada,saldodado):
    self.cuenta=cuentadada,
    self.saldo=saldodado,

  #metodos
  def retirar(self):
    print(f'hola yo soy {self.nombre}')

#para usar una clase instanciamos en el objeto batman
cliente=Usuario("santiago","alvarez","1193078088","Medellín")
cuenta=Cuenta("1","0")

i=1
crearMenu()
while(i!=0):
    #diccionario ciclista
    ciclista={

    }
    i=int(input("Digita una opcion: "))
    if(i==1):
        print("Consultar saldo de la cuenta")
        print("")
        print(f"el señor {cliente.nombre} identificado con documento: {cliente.cedula} tiene en su cuenta: {cuenta.saldo}: ")      
        print("")
        crearMenu()
    elif(i==2):
        print("Ingresar saldo a la cuenta")
        cuenta.saldo=int(input(f"Digita el saldo a ingresar a la cuenta: {cuenta.cuenta}"))
        os.system ("cls")
        crearMenu()               
    elif(i==3):
        print("Retirar saldo de la cuenta")
        print("")
        cuenta.saldo = cuenta.saldo - int(input(f"Digita el saldo a retirar de la cuenta: {cuenta.cuenta}: "))
        os.system ("cls")
        crearMenu();        
    elif(i==4):
        os.system ("cls")        
        crearMenu()
    elif(i==5):
        cliente.nombre=input(f"Actualiza tu nombre: ")
        cliente.apellido=input(f"Actualiza tu apellido: ")
        cliente.cedula=input(f"Actualiza tu cédula: ")
        cliente.ciudad=input(f"Actualiza tu ciudad: ")
        os.system ("cls")        
        crearMenu()   
    elif(i==0):
        break
    else:
        print("Digite una opcion valida.")
else:
    print("Digite una opcion valida.")





# #con el objeto accedo a los atributos o a los métodos
# cliente.nombre='santiago'
# cliente.apellido='murillo'
# cliente.cedula='4444444'
# cliente.ciudad='medellín'
# print(f'El nombre es: {cliente.nombre}')
# print(f'El apellido es: {cliente.apellido}')
# print(f'El cédula es: {cliente.cedula}')
# print(f'La ciudad es: {cliente.ciudad}')
# #con el objeso acceso a los métodos
# cliente.salular()


