#                   Prueba evaluacion de fundamentos
#
#   Este proyecto es una evaluacion, presente en el curso rapido Python y Django,
#este proyecto fue indicado en un documento y fue entregado un archivo comprimido 
#con plantillas, previamente escritas. El proposito segun lo indica el documento
#es continuar el trabajo comenzado por uno o varios integrantes de uno varios
#equipos de trabajo, seguramente bajo la modalidad de desarrollo rapido al estilo
#"Scrum" o similar.
#
#   Por esta razon, no se pueden modificar:
#   *   La estructura base
#   *   Modulos
#   *   Funciones
#   *   Logica (probablemente funcional)
#   *
#
# Plantillas modificadas por César Aguas en 2024, para rendir examen.
#
#   Se han añadido muy pocas cosas, tales como la logica para devolver valores,
#en las funciones ya especificadas. Tambien se ha añadido modificaciones esteticas,
#para mejorar la apariencia. Eso seria todo.

# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# valores iniciales - 
n_pregunta = 0
continuar = 's'#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
correcto = True
p_level = 10
# Dependiendo de la plataforma, la instruccion "limpiar pantalla"
# cambia entre cls y clear.
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# ----------------------------------------

os.system(op_sys) # limpiar pantalla

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print('@     El Señor de los Anillos          @')
print('@             Trivia                   @')
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print()
opcion = input('''Desea Jugar [s/n]?
        S. Jugar
        N. Salir
        
    > ''')
# 1. validar opcion
#opcion = 
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Se pasa la eleccion a un bucle hasta que se elije la opcion adecuada
print()
print(f"Validando su eleccion")
opcion = validate(['s', 'n'], opcion)
#print(f"Opcion {opcion} validada...")
#print()
os.system(op_sys)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# 2. Definir el comportamiento de Salir
if opcion == 'n':
    #print()
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    print("Ok, saliendo de la aplicacion.")
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    time.sleep(2)
    os.system(op_sys)
    # finalizar programa
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    exit()
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    
print('''
    Ok!
    Esta trivia consta de 3 niveles de dificultad,
    se comienza desde el nivel facil,
    y cada nivel tiene 3 preguntas.

    Ej: Si elijes 1, tendras que responder 1 pregunta por nivel,
    3 en total.
''')
# Funcionamiento de preguntas
while correcto and n_pregunta < 3* p_level: #???? Que es esto de 3 * p_level????
    if n_pregunta == 0:
        p_level = int(input('¿Cuántas preguntas por nivel? (Máximo 3): '))
        # 3. Validar el número de preguntas por nivel
        #p_level = 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #print(type(p_level))
        p_level = validate([1, 2, 3], p_level)
        os.system(op_sys)
        print("Comenzemos...")
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    if continuar == 's':
        #contador de preguntas
        n_pregunta += 1
        # 4. Escoger el nivel de la pregunta
        #nivel = 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        print()
        #print(f"n_pregunta: {n_pregunta}, p_level:{p_level}")
        nivel = choose_level(n_pregunta, int(p_level))
        #print(f"p_level:{p_level}, nivel:{nivel}, n_pregunta: {n_pregunta}")
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        #enunciado, alternativas = 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        enunciado, alternativas = choose_q(nivel)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        #6. Imprimir el enunciado y sus alternativas en pantalla
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        print()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print()
        print_pregunta(enunciado, alternativas)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        respuesta = input('Escoja la alternativa correcta:\n> ').lower()
        # 7. Validar la respuesta entregada
        #respuesta = 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        respuesta = validate(['a', 'b', 'c', 'd'], respuesta)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # 8. Verificar si la respuesta es correcta o no
        #correcto = 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        correcto = verificar(alternativas, respuesta)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #print(type(correcto), type(n_pregunta), type(p_level))
        #print("Cambiando tipo de p_level")
        #p_level = int(p_level)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        if correcto and n_pregunta < 3*p_level:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #print(f"p_level:{p_level}, nivel:{nivel}, n_pregunta: {n_pregunta}")
            continuar = input('Desea continuar? [s/n]: ').lower()
            #9. Validar si es que se responde y o n
            #continuar = 
            continuar = validate(['s', 'n'], continuar)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            os.system(op_sys)

        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(6)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            os.system(op_sys)

            exit()

        else: 
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
            time.sleep(6)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
            #os.system(op_sys)

            exit()
    else: 
        print('Ok, talvez a la proxima!')
        time.sleep(3)


        os.system(op_sys)


        exit()
            
            
