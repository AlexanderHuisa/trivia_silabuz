########################
#                     ##
#### REALIZADO POR #####
##Alexander Huisa-2022##
#                     ##
########################
import time
import os

#colores codigo
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


def limpiarConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # si la maquina tiene windows, use cls
        command = 'cls'
    os.system(command)


def numeroTrivia():
    respuesta2 = int(input('Seleccione el número de la trivia a realizar: '))
    while respuesta2 not in (1, 2, 3):
        respuesta2 = int(
            input(
                nombre +
                ' debes responder "1","2" o "3". Ingresa nuevamente tu repuesta:'
            ))
    return respuesta2


def mensaje(nombre, mensaje):
    print('Hola', BLUE, nombre, RESET, 'bienvenido a la trivia de', mensaje,
          'en donde pondremos a prueba tus conocimientos.\n')
    print(
        'En el juego lo único que debes hacer es responde las siguientes preguntas escribiendo la letra de la alternativa correcta presionando "enter" para enviar tu repuesta:\n'
    )
    print(BLUE, 'Iniciando juego....', RESET)
    time.sleep(3)


def pedirRespuesta():
    respuesta = input('¿Cuál es tu respueseta?: ')
    while respuesta not in ('a', 'b', 'c', 'd'):
        respuesta = input(
            nombre +
            ' debes responder "a","b","c" o "d". Ingresa nuevamente tu repuesta:'
        )
    return respuesta


def resultado(nombre, puntos, correctas, incorrectas, intentos,
              opcionIntentos):
    opcion = ' '
    if puntos >= 100:
        print('\n¡Felicidades!', nombre, ', obtuviste el puntaje perfecto')
    else:
        print('\n', nombre, ', obtuviste')
    print('Un total de', puntos, '/ 100 puntos, con:')
    print(GREEN, 'RESPUESTAS CORRECTAS', RESET, '=', correctas,
          'de 5 preguntas')
    print(RED, 'RESPUESTAS INCORRECTAS', RESET, '=', incorrectas,
          'de 5 preguntas')
    print(BLUE, 'NUMERO DE INTENTOS', RESET, '=', intentos, '\n')

    opcion = input(
        'Si deseas repetir la trivia preciona la letra "S", caso contrario presiona cualquier tecla.'
    )
    opcion = opcion.upper()
    if opcion != 'S':
        opcionIntentos = False
    else:
        opcionIntentos = True

    return opcionIntentos


print('\033[34m BIENVENIDO AL JUEGO \033[39m'.center(70, '='))

print('\nPon a prueba tu conocimiento sobre diversos temas.\n')

nombre = input('Para iniciar con la trivia cuentame, ¿Cual es tu nombre? ')
menu = """
\033[34mMENU.\033[39m

\033[34m1.\033[39m Trivia sobre tecnología.
\033[34m2.\033[39m Trivia sobre historia.
\033[34m3.\033[39m Salir.
"""
opcionMenu = True
respuesta = ' '

while opcionMenu == True:
    limpiarConsole()
    print('\033[34m BIENVENIDO AL JUEGO \033[39m'.center(70, '='))
    intentos = 0
    puntos = 0
    correctas = 0
    incorrectas = 0
    opcionIntentos = True
    print(menu)
    print(
        "Hola,\033[34m", nombre,
        "\033[39m¿En qué tipo de trivia desea poner a prueba su conocimientos?"
    )
    opcionTrivia = numeroTrivia()

    #====================TRIVIA 1============================
    if opcionTrivia == 1:
        while opcionIntentos == True:
            limpiarConsole()
            mensaje(nombre, 'tecnología,')
            intentos += 1
            puntos = 0
            correctas = 0
            incorrectas = 0

            print(BLUE,
                  "\n1) ¿En qué año se envió el primer mensaje de texto SMS?",
                  RESET)
            print(CYAN,'\n a) En 1985.')
            print(' b) En 1992.')
            print(' c) En 1997.')
            print(' d) En 1999.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "b":
                print(GREEN, '¡Respuesta Correcta!\n', RESET,)
                print(GREEN, 'Según NPR, un ingeniro envió el mensaje que decía "feliz navidad" al teléfono mòvil del director de Vodafone, Richard Jarvis, el 3 de diciembre de 1992',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED,'¡Respuesta Incorrecta\n', RESET,)
                print(GREEN, 'Según NPR, un ingeniro envió el mensaje que decía "feliz navidad" al teléfono mòvil del director de Vodafone, Richard Jarvis, el 3 de diciembre de 1992',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(
                BLUE,
                '\n2) ¿Qué tecnología se utiliza para hacer posibles las llamadas telefónicas a través de Internet?',
                RESET)
            print(CYAN,'\n a) Ethernet.')
            print(' b) Bluetooth.')
            print(' c) POP.')
            print(' d) VoIP.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "d":
                print(GREEN, '¡Respuesta Correcta!\n', RESET)
                print(GREEN, 'Voz sobre protocolo de Internet, también llamada VoIP (Voice over IP), es un conjunto de recursos que hacen posible que la señal de voz viaje a través de Internet.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN, 'Voz sobre protocolo de Internet, también llamada VoIP (Voice over IP), es un conjunto de recursos que hacen posible que la señal de voz viaje a través de Internet.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(BLUE, '\n3) ¿Qué es el spam?', RESET)
            print(CYAN,'\n a) Un virus informático.')
            print(' b) Correos no solicitados.')
            print(' c) Un lenguaje de programación.')
            print(' d) Una marca de ordenadores.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "b":
                print(GREEN, '¡Respuesta Correcta!\n',RESET)
                print(GREEN, 'El spam engloba esos correos que normalmente no hemos solicitado, son correos publicitarios y que se envían de forma masiva a cientos de cuentas de correo.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN, 'El spam engloba esos correos que normalmente no hemos solicitado, son correos publicitarios y que se envían de forma masiva a cientos de cuentas de correo.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(
                BLUE,
                '\n4) Samsung es una empresa de tecnología proveniente de Asia ¿de qué país es?',
                RESET)
            print(CYAN,'\n a) Taiwan.')
            print(' b) Japon.')
            print(' c) Corea del sur.')
            print(' d) China.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "c":
                print(GREEN, '¡Respuesta Correcta!\n', RESET)
                print(GREEN,'La sede de la empresa, Samsung Town se encuentra en la ciudad de Seúl, capital de Corea del Sur.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN,'La sede de la empresa, Samsung Town se encuentra en la ciudad de Seúl, capital de Corea del Sur.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(BLUE, '\n5) ¿Qué son los Digital Twins?', RESET)
            print(CYAN,'\n a) Son réplicas Virtuales de objetos o procesos que simulan el comportamiento de sus homologos reales.'
            )
            print(' b) Son los Perfiles de los usuarios en la redes sociales.')
            print(' c) Son la  reproducción digital de los objetos reales.')
            print(' d) Son programas informaticos con los que son posible mantener una conversación fluidamente.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "a":
                print(GREEN, '¡Respuesta Correcta!\n', RESET)
                print(GREEN,'Los Digital Twins, son réplicas Virtuales de objetos o procesos que simulan el comportamiento de sus homologos reales. respuesta correcta.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN,'Los Digital Twins, son réplicas Virtuales de objetos o procesos que simulan el comportamiento de sus homologos reales. respuesta correcta.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            opcionIntentos = resultado(nombre, puntos, correctas, incorrectas,
                                       intentos, opcionIntentos)

#====================TRIVIA 2============================
    elif opcionTrivia == 2:
        while opcionIntentos == True:
            limpiarConsole()
            mensaje(nombre, 'historia,')
            intentos += 1
            puntos = 0
            correctas = 0
            incorrectas = 0

            print(
                BLUE,
                "\n1) ¿Qué hito informático de 1969 cambiaría radicalmente el curso de la historia de la humanidad?",
                RESET)
            print(CYAN,'\n a) El primer ordenador personal.')
            print(' b) El internet.')
            print(' c) El primer router wi-fi.')
            print(' d) El primer iPod.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "b":
                print(GREEN, '¡Respuesta Correcta!\n', RESET)
                print(GREEN, 'Bautizada originalmente como ARPANET, la red Internet cambiaría radicalmente el flujo de información y comercio a todos los niveles y en todas partes del mundo.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN, 'Bautizada originalmente como ARPANET, la red Internet cambiaría radicalmente el flujo de información y comercio a todos los niveles y en todas partes del mundo.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(BLUE,
                  '\n2) ¿Quién fue el primer Presidente de Estados Unidos?',
                  RESET)
            print(CYAN,'\n a) Abraham Lincoln.')
            print(' b) Thomas Jefferson.')
            print(' c) Andrew Jackson.')
            print(' d) George Washington.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "d":
                print(GREEN, '¡Respuesta Correcta!\n', RESET)
                print(GREEN,'El primer presidente de los Estados Unidos de América fue George Washington, quien comenzó su mandato el 30 de abril de 1789 y terminó el 4 de marzo de 1797. Es considerado uno de los Padres Fundadores. Murió de complicaciones por el tratamiento que recibía para su neumonía.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN,'El primer presidente de los Estados Unidos de América fue George Washington, quien comenzó su mandato el 30 de abril de 1789 y terminó el 4 de marzo de 1797. Es considerado uno de los Padres Fundadores. Murió de complicaciones por el tratamiento que recibía para su neumonía.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(BLUE, '\n3) ¿Qué año inicio la primera gerra mundial?',
                  RESET)
            print(CYAN,'\n a) En 1912.')
            print(' b) En 1914.')
            print(' c) En 1916.')
            print(' d) En 1918.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "b":
                print(RED, '¡Respuesta Correcta!\n', RESET)
                print(GREEN,'La Primera Guerra Mundial, anteriormente llamada la Gran Guerra, fue una confrontación bélica centrada en Europa que empezó el 28 de julio de 1914 y finalizó el 11 de noviembre de 1918.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN,'La Primera Guerra Mundial, anteriormente llamada la Gran Guerra, fue una confrontación bélica centrada en Europa que empezó el 28 de julio de 1914 y finalizó el 11 de noviembre de 1918.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(BLUE, '\n4) ¿Qué año el hombre llegó a la luna?', RESET)
            print(CYAN,'\n a) En 1961.')
            print(' b) En 1964.')
            print(' c) En 1966.')
            print(' d) En 1969.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "d":
                print(GREEN, '¡Respuesta Correcta!\n', RESET)
                print(GREEN,'El 20 de julio de 1969 la misión estadounidense Apolo 11, colocó a los primeros hombres en la Luna: el comandante Neil Armstrong y el piloto Edwin F. Aldrin.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN,'El 20 de julio de 1969 la misión estadounidense Apolo 11, colocó a los primeros hombres en la Luna: el comandante Neil Armstrong y el piloto Edwin F. Aldrin.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            print(BLUE, '\n5) ¿En qué año fue inaugurado el canal de Panamá?',
                  RESET)
            print(CYAN,'\n a) En 1912.')
            print(' b) En 1914.')
            print(' c) En 1916.')
            print(' d) En 1918.\n',RESET)
            respuesta = pedirRespuesta()
            if respuesta == "b":
                print(GREEN, '¡Respuesta Correcta!\n', RESET)
                print(GREEN,'Se hicieron planes para una gran celebración que marcara adecuadamente la apertura oficial del Canal de Panamá el 15 de agosto de 1914.',RESET)
                puntos += 20
                correctas += 1
            else:
                print(RED, '¡Respuesta Incorrecta!\n', RESET)
                print(GREEN,'Se hicieron planes para una gran celebración que marcara adecuadamente la apertura oficial del Canal de Panamá el 15 de agosto de 1914.',RESET)
                puntos -= 10
                incorrectas += 1
            time.sleep(2)

            opcionIntentos = resultado(nombre, puntos, correctas, incorrectas,intentos, opcionIntentos)

#====================SALIR============================
    elif opcionTrivia == 3:
        opcionMenu = False
        print(
            "\nGracias\033[34m", nombre,
            "\033[39mpor jugar la trivia, espero que te hayas divertido, nos vemos pronto...\n"
        )
