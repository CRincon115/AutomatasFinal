from automathon import DFA
from PIL import Image

#traes la suma final del path del juego

def gameCaseFinal(total_value):
    def gameCaseSimple():
        Q = {'inicio', 'semáforo', 'ATM', 'máquina expendedora', 'juego'}
        sigma = {'0', '1'}
        delta = {'inicio': {'0': 'semáforo', '1': 'semáforo'},
                'semáforo': {'0': 'máquina expendedora', '1': 'ATM'},
                'ATM': {'0': 'máquina expendedora', '1': 'máquina expendedora'},
                'máquina expendedora': {'0': 'semáforo', '1': 'juego'}
                }
        initialState = 'inicio'
        F = {'juego'}

        automataSimple = DFA(Q, sigma, delta, initialState, F)
        automataSimple.view("Juego Completo simple")
        image = Image.open('Juego Completo simple.gv.png')
        image.show()
        input("Gracias por jugar!")

    def gameCase():
        Q = {'q0', 'q1', 'q2','q3', 'q4'}
        sigma = {'0', '1'}
        delta = { 'q0' : {'0' : 'q1', '1' : 'q1'},
                'q1' : {'0' : 'q3', '1' : 'q2'},
                'q2' : {'0' : 'q3', '1' : 'q3'},
                'q3' : {'0' : 'q1', '1' : 'q4'}
                }
        initialState = 'q0'
        F = {'q4'}

        automata1 = DFA(Q, sigma, delta, initialState, F)
        automata1.view("Juego Completo")
        image = Image.open('Juego Completo.gv.png')
        image.show()
        input("presiona para continuar")

        print("la cadena de aceptacion que generaste es: ", total_value)
        print(automata1.accept(total_value))


    print("Gracias por probar nuestro juego, toda esta aventura envuelve a un autómata también, de\n"
        "un autómata finito indeterminado para ser más precisos. Las deciciones que tomaste en esta historia se basan en la\n"
        "siguiente definición formal: \n"
        "M1 = (Q, Delta, Sigma(función de transición), Estado Inicial, Estados de aceptacion) \n"
        "Con la definicion anterior podemos mostrar los elementos de nuestro juego \n"
        "Q = {'q0', 'q1', 'q2','q3', 'q4'}\n"
        "sigma = {'0','1'}\n"
        "delta = { 'q0' : {'0' : 'q1', '1' : 'q1'}, 'q1' : {'0' : 'q3', '1' : 'q2'}, 'q2' : {'0' : 'q3', '1' : 'q3'},\n"
        "'q3' : {'0' : 'q1', '1' : 'q4'}"
        "initialState = 'q0'\n"
        "F = {'q4'}\n"
        "A continuacion se muestra el diagrama de nuestra definición")
    gameCase()
    input("Y ahora el diagrama con elementos simplificados para ser ejemplificados: Presiona para mostrar")
    gameCaseSimple()
    


