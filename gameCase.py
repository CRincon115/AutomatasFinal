from automathon import DFA
from PIL import Image

#traes la suma final del path del juego

def gameCaseSimple():
    Q = {'inicio', 'semaforo', 'atm', 'expendidora', 'fin'}
    sigma = {'0', '1'}
    delta = {'inicio': {'0': 'semaforo', '1': 'semaforo'},
             'semaforo': {'0': 'expendidora', '1': 'atm'},
             'atm': {'0': 'expendidora', '1': 'expendidora'},
             'expendidora': {'0': 'semaforo', '1': 'fin'}
             }
    initialState = 'inicio'
    F = {'fin'}

    automataSimple = DFA(Q, sigma, delta, initialState, F)
    automataSimple.view("Juego Completo simple")
    image = Image.open('Juego Completo simple.gv.png')
    input("presiona para continuar")
    image.show()

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
    input("presiona para continuar")
    image.show()



print("Gracias por probar nuestro juego, a final de cuentas toda esta aventura se trato de un autómata tambien, de\n"
      "un autómata finito indeterminado para ser mas precisos, las deciciones que tomaste en esta historia se basan en la\n"
      "siguiente definicion formal: \n"
      "M1 = (Q, Delta, Sigma(función de transición), Estado Inicial, Estados de aceptacion) \n"
      "Con la definicion anterior podemos mostrar los elementos de nuestro juego \n"
      "Q = {'q0', 'q1', 'q2','q3', 'q4'}\n"
      "sigma = {'0','1'}\n"
      "delta = { 'q0' : {'0' : 'q1', '1' : 'q1'}, 'q1' : {'0' : 'q3', '1' : 'q2'}, 'q2' : {'0' : 'q3', '1' : 'q3'},\n"
      "'q3' : {'0' : 'q1', '1' : 'q4'}"
      "initialState = 'q0'\n"
      "F = {'q4'}\n"
      "A continuacion se muestra el diagrama de nuestra definicion")
gameCase()
input("y Ahora el diagrama con elementos simplificados para ser ejemplificados. Presiona para continuar")
gameCaseSimple()
input("presiona para continuar")


