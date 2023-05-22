import q0,q1,q2,q3,q4
from gameCase import gameCaseFinal

# value = None


def print_story(name):
    print(f'Hola, {name}, bienvenido a nuestro juego interactivo: Automatas en tu vida diaria. '
          f'Este juego consiste en tomar decisiones para nuestro personaje principal, mientras te '
          f'enseñamos dónde se encuentran los autómatas en nuestra vida cotidiana.')
    input("Presiona enter para continuar")

    q0.q0()
    
    def vuelta():
        global total_value
        total_value = " "
        q1.q1() # Asignar el valor devuelto por q1() a la variable value 
        if q1.value == 0:
            total_value = total_value + "0"
            q3.q3alternativo()
            if q3.value == 0:
                total_value = total_value + "0"
                q4.q4()
            elif q3.value == 1:
                total_value = total_value + "1"
                vuelta()
            else:
                print("Ups, error")

    
        elif q1.value == 1:
            total_value = total_value + "1"
            q2.q2()
            total_value = total_value + "0"
            q3.q3()
            if q3.value == 1:
                total_value = total_value + "1"
                q4.q4()
            elif q3.value == 0:
                total_value = total_value + "0"
                q1.q1alternativo()
                if q1.value == 1:
                    total_value = total_value + "1"
                    q4.q4()
                else:
                    q4.q4()
            else:
                print("Ups, error")
        else:
            print("Ups, error")


    vuelta()

    gameCaseFinal()