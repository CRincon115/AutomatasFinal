from q0 import q0
import q1
from q2 import q2
from q3 import q3
from q4 import q4

# value = None
total_value = str

def print_story(name):
    print(f'Hola, {name}, bienvenido a nuestro juego interactivo: Automatas en tu vida diaria. '
          f'Este juego consiste en tomar decisiones para nuestro personaje principal, mientras te '
          f'enseñamos dónde se encuentran los autómatas en nuestra vida cotidiana.')
    input("Press enter to continue")

    q0()

    q1.q1()  # Asignar el valor devuelto por q1() a la variable value
    
    if q1.value == 0:
        q3()
         if q3.value == 0:
           print("ok")
         elif q3.value == 1:
           print("ok")

    elif q1.value == 1:
        q2()
    else:
        print("Por favor, escoge una de las opciones correctas")


    # gamecase(value)

