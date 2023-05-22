#Vending Machine
from automathon import DFA
from PIL import Image

tSigma = 0
def q3():
    def q3Origin():
        Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
        sigma = {'0','1'}
        delta = { 'q0' : {'0' : 'q1', '1' : 'q5'},
                'q1' : {'0' : 'q2', '1' : 'q6'},
                'q2' : {'1' : 'q3', '0' : 'q2'},
                'q3' : {'1' : 'q4', '0' : 'q3'},
                'q4' : {'1' : 'q5', '0' : 'q4'},
                'q5' : {'1' : 'q6', '0' : 'q5'}
                }
        initialState = 'q0'
        F = {'q6'}

        automataVM = DFA(Q, sigma, delta, initialState, F)
        automataVM.view("Vending")
        image = Image.open('Vending.gv.png')
        image.show()
        input("presiona para continuar")

    def gamelogic():
        print("Ahora que compraste la bebida, estás listo para el partido!")
        print("Ir al partido?")
        token = input("Si/No ")
        text = token.casefold()
        if text == "si":
            return 1
        elif text == "no":
            return 0
        
    print("Haz llegado al lugar donde se encuentra el tercer autómata de la vida cotidiana: la máquina expendedora. \n"
        "La máquina expendedora es similar al cajero automático en el sentido de que se puede personalizar la complejidad "
        "de los estados que componen al autómata. De igual forma, estas dos máquinas forman parte del conjunto de los aútomatas finitos determinados"
        "los cuales dependiendo de una entrada en específico, tienen una salida determinada. A continuación se muestra la definición"
        "de la expendedora (los elementos serán escritos debido a la falta de símbolos): \n"
        "M1 = (Q, Delta, Sigma(función de transición), Estado Inicial, Estados de aceptacion) \n"
        "Con la definicion anterior podemos mostrar los elementos de un semaforo: \n"
        "Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}\n"
        "sigma = {'0','1'}\n"
        "delta = { 'q0' : {'0' : 'q1', '1' : 'q5'}, 'q1' : {'0' : 'q2', '1' : 'q6'}, 'q2' : {'1' : 'q3', '0' : 'q2'}, 'q3' : {'1' : 'q4', '0' : 'q3'}, 'q4' : {'1' : 'q5', '0' : 'q4'}, 'q5' : {'1' : 'q6', '0' : 'q5'} } \n"
        "initialState = 'q0'\n"
        "F = {q6}\n")

    def q3simple():
        Q = {'$0.00', '$0.25', '$0.50', '$0.75', '$1.00', '$1.25'}
        sigma = {'$0.25', '$1.00'}
        delta = { '$0.00' : {'$0.25': '$0.25', '$1.00' : '$1.00'},
                '$0.25' : {'$0.25': '$0.50', '$1.00' : '$1.25'},
                '$0.50' : {'$0.25': '$0.75', '$0.00' : '$0.50'},
                '$0.75' : {'$0.25': '$1.00', '$0.00' : '$0.75'},
                '$1.00' : {'$0.25': '$1.25', '$0.00' : '$1.00'}
                }
        initialState = '$0.00'
        F = {'$1.25'}

        automataVMsimple = DFA(Q, sigma, delta, initialState, F)
        automataVMsimple.view("Vending Simple")
        image = Image.open('Vending Simple.gv.png')
        image.show()
        input("presiona para continuar")

    q3Origin()

    print("A continuación, se muestra lo anterior de forma explícita reflejando el caso de la vida real."
        "Q = {'$0.00', '$0.25', '$0.50', '$0.75', '$1.00', '$1.25'} \n"
        "sigma = {'$0.25', '$1.00'} \n"
        "delta = { '$0.00' : {'$0.25': '$0.25', '$1.00' : '$1.00'}, '$0.25' : {'$0.25': '$0.50', '$1.00' : '$1.25'}, '$0.50' : {'$0.25': '$0.75', '$0.00' : '$0.50'}, '$0.75' : {'$0.25': '$1.00', '$0.00' : '$0.75'}, '$1.00' : {'$0.25': '$1.25', '$0.00' : '$1.00'} } \n"
        "initialState = '$0.00'\n"
        "F = {'$1.25'}\n")

    q3simple()


    global value 
    value =  gamelogic()

def q3alternativo():
    print("No tienes suficiente dinero para comprar una soda, tal vez sacando dinero de un ATM...")
    def gamelogic():
        print("Puedes regresar o irte directamente al partido.")
        token = input("Regresar/Irme ")
        text = token.casefold()
        if text == "regresar":
            return 1
        elif text == "irme":
            return 0
    global value 
    value =  gamelogic()
