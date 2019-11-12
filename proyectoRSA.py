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
while opcion != 3:
    print(menu())
    opcion = int(input("Ingrese una opcion: "))

    if (opcion == 1):
        print()
        print("Opcion1")
    elif(opcion == 2):
        print()
        print("Opcion2")
    else:
        print("Opcion no valida")
