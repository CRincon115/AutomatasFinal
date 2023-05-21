# #semaforo
# from automathon import DFA
# from PIL import Image

# tSigma = 0
# def q2():
#     Q = {'q0', 'q1', 'q2'}
#     sigma = {'1'}
#     delta = { 'q0' : {'1': 'q1'},
#               'q1' : {'1': 'q2'},
#               'q2' : {'1': 'q0'}
#             }
#     initialState = 'q0'
#     F = {}

#     automataSemaforo = DFA(Q, sigma, delta, initialState, F)
#     automataSemaforo.view("Semaforo")
#     image = Image.open('Semaforo.gv.png')
#     input("presiona para continuar")
#     image.show()

# def q2simple():
#     Q = {'rojo', 'verde', 'amarillo'}
#     sigma = {'cambio'}
#     delta = { 'rojo' : {'cambio': 'verde'},
#               'verde' : {'cambio': 'amarillo'},
#               'amarillo' : {'cambio': 'rojo'}
#             }
#     initialState = 'rojo'
#     F = {}

#     automataSemaforoSimple = DFA(Q, sigma, delta, initialState, F)
#     automataSemaforoSimple.view("Semaforo Simple")
#     image = Image.open('Semaforo Simple.gv.png')
#     input("presiona para continuar")
#     image.show()

# def gamelogic():
#     print("Segunda Logica")
#     token = input("Si/No")
#     text = token.casefold()
#     if text == "si":
#         return 1
#     elif text == "no":
#         return 0



# print("Al dirigirse a su partido de Baseball, Juan tuvo que trasladarse en carro. Es aqui cuando nos encontramos"
#       "nuestro primer Autómata en la vida cotidiana: el semaforo.\n"
#       "El semaforo consiste en uno de los automatas más simples, una maquina de estados finitos determinados, es decir, "
#       "una maquina de estados finitos (numero delimitado de estados) la cual cambia al siguiente estado dependiendo de la"
#       "entrada, la cual al ser determinada, solamente tiene una posible salida, a continuacion se muestra la definicion"
#       "de dicha maquina(los elementos serán escritos debido a la falta de simbolos): \n"
#       "M1 = (Q, Delta, Sigma(función de transición), Estado Inicial, Estados de aceptacion) \n"
#       "Con la definicion anterior podemos mostrar los elementos de un semaforo: \n"
#       "Q = {'q0', 'q1', 'q2'}\n"
#       "sigma = {'1'}\n"
#       "delta = { 'q0' : {'1': 'q1'}, 'q1' : {'1': 'q2'}, 'q2' : {'1': 'q0'}}\n"
#       "initialState = 'q0'\n"
#       "F = {}\n")

# q2()
# input("presiona para continuar")
# print("A continuacion se muestra lo anterior de forma explicita para la vida real"
#       "Q = {'rojo', 'verde', 'amarillo'}\n"
#       "sigma = {'cambio'}\n"
#       "delta = { 'rojo' : {'cambio': 'verde'}, 'verde' : {'cambio': 'amarillo'}, 'amarillo' : {'cambio': 'rojo'}}\n"
#       "initialState = 'rojo'\n"
#       "F = {sin estado final}\n")
# q2simple()
# input("presiona para continuar")

# tSigma = gamelogic()
# input("presiona para continuar")

# print(tSigma)
def q2():
    print("estas en q2 ok")

