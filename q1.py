#Semáforo
from automathon import DFA
from PIL import Image

tSigma = 0
def q1():
    def q1Origin():
        Q = {'q0', 'q1', 'q2'}
        sigma = {'1'}
        delta = { 'q0' : {'1': 'q1'},
                'q1' : {'1': 'q2'},
                'q2' : {'1': 'q0'}
                }
        initialState = 'q0'
        F = {}

        automataSemaforo = DFA(Q, sigma, delta, initialState, F)
        automataSemaforo.view("Semáforo")
        image = Image.open('Semáforo.gv.png')
        image.show()
        input("presiona para continuar")

    def q1simple():
        Q = {'rojo', 'verde', 'amarillo'}
        sigma = {'cambio'}
        delta = { 'rojo' : {'cambio': 'verde'},
                'verde' : {'cambio': 'amarillo'},
                'amarillo' : {'cambio': 'rojo'}
                }
        initialState = 'rojo'
        F = {}

        automataSemaforoSimple = DFA(Q, sigma, delta, initialState, F)
        automataSemaforoSimple.view("Semaforo Simple")
        image = Image.open('Semaforo Simple.gv.png')
        input("presiona para continuar")
        image.show()

    def gamelogic():
        print("Juan Tiene sed, y decide pasar a la Máquina expendedora para Comprar una bebida,¿Revisas tu cartera?")
        token = input("Si/No")
        text = token.casefold()
        if text == "si":
            return 1
        elif text == "no":
            return 0



    print("Al dirigirse a su partido de Baseball, Juan tuvo que trasladarse en carro. Es aqui cuando nos encontramos"
        "nuestro primer Autómata en la vida cotidiana: el semáforo.\n"
        "El semáforo consiste en uno de los automatas más simples, una maquina de estados finitos determinados, es decir, "
        "una maquina de estados finitos (número delimitado de estados) la cual cambia al siguiente estado dependiendo de la"
        "entrada, la cual solamente tiene una posible salida. A continuación se muestra la definición"
        "de dicha máquina(los elementos serán escritos debido a la falta de símbolos): \n"
        "M1 = (Q, Delta, Sigma(función de transición), Estado Inicial, Estados de aceptacion) \n"
        "Con la definicion anterior podemos mostrar los elementos de un semaforo: \n"
        "Q = {'q0', 'q1', 'q2'}\n"
        "sigma = {'1'}\n"
        "delta = { 'q0' : {'1': 'q1'}, 'q1' : {'1': 'q2'}, 'q2' : {'1': 'q0'}}\n"
        "initialState = 'q0'\n"
        "F = {}\n")

    q1Origin()
    
    print("A continuación, se muestra lo anterior de forma explícita reflejando el caso de la vida real."
        "Q = {'rojo', 'verde', 'amarillo'}\n"
        "sigma = {'cambio'}\n"
        "delta = { 'rojo' : {'cambio': 'verde'}, 'verde' : {'cambio': 'amarillo'}, 'amarillo' : {'cambio': 'rojo'}}\n"
        "initialState = 'rojo'\n"
        "F = {sin estado final}\n")
    q1simple()
    input("Presiona para continuar")

    global value 
    value =  gamelogic() 

def q1alternativo():
    print("No hay necesidad de regresar, mejor ve al partido...")
    def gamelogic():
        print("Ir al partido?")
        token = input("Si/No")
        text = token.casefold()
        if text == "si":
            return 1
        elif text == "no":
            q1alternativo()
    global value 
    value = gamelogic()
