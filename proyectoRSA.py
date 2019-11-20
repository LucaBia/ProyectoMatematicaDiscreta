# Criptografia RSA
# https://juncotic.com/rsa-como-funciona-este-algoritmo/

import random
import math

def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def mcd(a,b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

def menu():
  strMenu = """
  ----------------------------
  Sistema de Criptografia RSA
  1. Encriptar
  2. Desencriptar
  3. Salir
  ----------------------------
  """
  return strMenu

 #Main
opcion = 0
numerosPrimos = []
while opcion != 3:
    print(menu())
    opcion = int(input("Ingrese una opcion: "))

    if (opcion == 1):
        print(" ")
        print("Opcion1")

        #Codigo para generar numero primos entre un rango
        start = 11
        end = 25
        for val in range(start, end + 1):
           #Si el numero es divisicle por cualquier numero entre 2 y val, no es primo
            if val > 1:
                for n in range(2, val):
                    if (val % n) == 0:
                        break
                else:
                    # print(val)
                    numerosPrimos.append(val)

        #Se escoge aleatoriamente un numero primo para p
        p = random.choice(numerosPrimos)
        print("p: ", p)
        #Se elimina el numero primo seleccionado para asegurar que p no sea igual a q
        numerosPrimos.remove(p)
        #Se escoge aleatoriamente un numero primo para q
        q = random.choice(numerosPrimos)
        print("q: ", q)
        numerosPrimos.remove(q)

        n = p*q
        print("n: ", n)
        #Funcion Phi de Euler
        z = (p-1)*(q-1)
        print("phi: ", z)
        #Ciclo para encontrar un co-primo de z
        continueW = True
        while continueW:
            k = random.choice(numerosPrimos)
            if (mcd(z,k) == 1):
                continueW = False
        print("e: ", k)
        llavePublica = [n,k]

        continueW2 = True
        while continueW2:
            j = random.randint(0, 1000)
            if ((k*j)%z == 1):
                continueW2 = False
        print("d: ", j)
        llavePrivada = j

        #-----------------------------------------------------------------------
        mensaje = int(input("Ingrese el mensaje: "))
        mensajeEncriptado = (mensaje**k)%n
        print("El mensaje encriptado es: ", mensajeEncriptado)

        desencriptar = (mensajeEncriptado**j)%n
        print("El mensaje desencriptado es: ", desencriptar)




    elif(opcion == 2):
        print()
        print("Opcion2")
    else:
        print("Opcion no valida")
