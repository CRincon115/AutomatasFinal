from main import *

def menu():
    print("Elige una opción:")
    print("1. Opción 1")
    print("2. Opción 2")
    opcion = input("Ingresa el número de opción: ")
    
    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
        menu()

menu()