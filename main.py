from automathon import DFA
import graphviz


Q = {'q0', 'q1', 'q2'}
sigma = {'0', '1'}
delta = { 'q0' : {'0' : 'q0', '1' : 'q1'},
          'q1' : {'0' : 'q2', '1' : 'q0'},
          'q2' : {'0' : 'q1', '1' : 'q2'}
        }
initialState = 'q0'
F = {'q0'}

automata1 = DFA(Q, sigma, delta, initialState, F)
## This is an example about creating a DFA with the library

print(automata1.isValid())   #True
print(automata1.accept("001001"))   #True
print(automata1.accept("00100"))    #False

automata1.view("DFA Visualization")

# def opcion_1():
#     print("Has elegido la opción 1.")
#     # Aquí puedes agregar el código correspondiente al evento de la opción 1

# def opcion_2():
#     print("Has elegido la opción 2.")
#     # Aquí puedes agregar el código correspondiente al evento de la opción 2

# def menu():
#     print("Elige una opción:")
#     print("1. Opción 1")
#     print("2. Opción 2")
#     opcion = input("Ingresa el número de opción: ")
    
#     if opcion == "1":
#         opcion_1()
#     elif opcion == "2":
#         opcion_2()
#     else:
#         print("Opción inválida. Por favor, elige una opción válida.")
#         menu()

# menu()
