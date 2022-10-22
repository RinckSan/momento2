mayor = lambda numero1,numero2 : 1 if (numero1 > numero2 ) else -1
imprimir= lambda valor :"El primer número es mayor" if (valor==1) else "el segundo número es mayor"

valor=(mayor(5,6))
print(imprimir(valor))