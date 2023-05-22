#ATM
from automathon import DFA
from PIL import Image

tSigma = 0
def q2():
    def q2Origin():
        Q = {'q0', 'q1', 'q2', 'q3'}
        sigma = {'0','1'}
        delta = { 'q0' : {'1': 'q1', '0':'q1'},
                'q1' : {'1': 'q2', '0':'q3'},
                'q2' : {'1': 'q1', '0':'q3'}
                }
        initialState = 'q0'
        F = {'q3'}

        automataATM = DFA(Q, sigma, delta, initialState, F)
        automataATM.view("ATM")
        image = Image.open('ATM.gv.png')
        image.show()
        input("presiona para continuar")

    def q2simple():
        Q = {'Retirar', 'Cantidad', 'Salir'}
        sigma = {'0','1'}
        delta = { 'Inicio' : {'0':'Retirar', '1':'Retirar'},
                'Retirar' : {'1': 'Cantidad', '0':'Salir'},
                'Cantidad' : {'1': 'Retirar', '0':'Salir'}
                }
        initialState = 'Inicio'
        F = {'Salir'}

        automataATMsimple = DFA(Q, sigma, delta, initialState, F)
        automataATMsimple.view("ATM Simple")
        image = Image.open('ATM Simple.gv.png')
        image.show()
        input("presiona para continuar")

    def gamelogic():
        print("Ya haz sacado dinero, ahora podemos ir comprar una bebida!")
        token = input("Ir a comprar bedida? Si/Si! ")
        text = token.casefold()
        if text == "si":
            return 1
        elif text == "si!":
            return 0



    print("Al haber revisado su cartera se dio cuenta de que no tenía mucho dinero para comprar refrigerios por lo que decide ir al cajero automático"
        "el cual también forma parte de los autómatas finitos.\n"
        "El ATM es, de igual forma, uno de los automatas más sencillos con los que interactuamos en la vida cotidiana, una máquina de estados finitos determinados, es decir, "
        "una maquina de estados finitos (numero delimitado de estados) la cual cambia al siguiente estado dependiendo de la"
        "entrada del usuario, la cual al ser determinada, solamente tiene una posible salida. A continuación se muestra la definición"
        "de dicha máquina(los elementos serán escritos debido a la falta de símbolos): \n"
        "M1 = (Q, Delta, Sigma(función de transición), Estado Inicial, Estados de aceptacion) \n"
        "Con la definicion anterior podemos mostrar los elementos de un cajero automático: \n"
        " Q = {'q0', 'q1', 'q2', 'q3'}\n"
        "sigma = {'0','1'}\n"
        "delta = { 'q0' : {'1': 'q1', '0':'q1'}, 'q1' : {'1': 'q2', '0':'q3'}, 'q2' : {'1': 'q1', '0':'q3'} }\n"
        "initialState = 'q0'\n"
        "F = {q3}\n")

    q2Origin()
    
    print("A continuación se muestra lo anterior de forma explícita para un caso muy sencillo de un cajero automático en la vida real."
        "Q = {'Retirar', 'Cantidad', 'Salir'}\n"
        " sigma = {'Opción'}\n"
        "delta = { 'Inicio' : {'0':'Retirar', '1':'Retirar'}, 'Retirar' : {'1': 'Cantidad', '0':'Salir'}, 'Cantidad' : {'1': 'Retirar', '0':'Salir'} }\n"
        "initialState = 'Inicio'\n"
        "F = {Salir}\n")
    q2simple()


    global value 
    value =  gamelogic() 
