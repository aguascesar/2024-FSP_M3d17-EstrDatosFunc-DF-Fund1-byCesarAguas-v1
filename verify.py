import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    #pass
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #print(f"alternativas:{alternativas}")
    #alternativas:[['Train', 0], ['Theoden', 0], ['Bofur', 0], ['Isildur', 1]]
    #Buscando nuestro indice 1
    j = alternativas[eleccion][1]
    if j == 1: 
        #print("verify.py:::verificar::eleccion:  Respuesta Correcta!.")
        print("Respuesta Correcta!.")
        return True
    elif j == 0:
        #print("verify.py:::verificar::eleccion:  Respuesta Incorrecta.")
        print("Respuesta Incorrecta.")
        return False         
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ##########################################################################################
    #return correcto

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, 
    #e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






