import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad): 
    #escoger preguntas por dificultad
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #print(f'question.py:::choose_q::opciones: {opciones}')
    #print()
    # AKA choose_q(nivel) ['basicas']
    #                     ['intermedias']
    #                     ['avanzadas']  
    #preguntas = 
    #           preguntas.pool_preguntas[clave, valor]
    preguntas = p.pool_preguntas[dificultad]
    #print(f'question.py:::choose_q::preguntas: {preguntas}')
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # usar opciones desde ambiente global
    #global 
    # escoger una pregunta
    #n_elegido = 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    n_elegido = random.choice(opciones[dificultad])
    #   AKA      elegir.entre(opciones[dificultad], [1, 2, 3])
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    p_n = preguntas[f"pregunta_{n_elegido}"]
    #print(p_n)
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # eliminarla del ambiente global para no escogerla de nuevo
    #   AKA     eliminarla de las opciones
    opciones[dificultad].remove(n_elegido)
    #print()
    #print(f'question.py:::choose_q::opciones: {opciones}')
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # escoger enunciado y alternativas mezcladas
    #pregunta = 
    #alternativas = 
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    enunciado = p_n['enunciado']
    alternativas = shuffle_alt(p_n)
    return enunciado, alternativas
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #return preguntas['enunciado'], alternativas




if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')