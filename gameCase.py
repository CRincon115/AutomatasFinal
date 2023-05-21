
from automathon import DFA

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
print(automata1.isValid())

automata1.view("Juego Completo")
