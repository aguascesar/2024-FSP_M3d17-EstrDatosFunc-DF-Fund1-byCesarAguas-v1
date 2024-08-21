def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    #pass
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    match p_level:
        case 1:
            if n_pregunta == 1:
                level = 'basicas'
            elif n_pregunta == 2:
                level = 'intermedias'
            else:
                level = 'avanzadas'
        case 2:
            if n_pregunta <= 2:
                level = 'basicas'
            elif 2 < n_pregunta <= 4:
                level = 'intermedias'
            else:
                level = 'avanzadas'
        case 3:
            if n_pregunta <= 3:
                level = 'basicas'
            elif 3 < n_pregunta <= 6:
                level = 'intermedias'
            else:
                level = 'avanzadas'
        case _:
            print("level.py:::choose_level::  Error p_level")
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias