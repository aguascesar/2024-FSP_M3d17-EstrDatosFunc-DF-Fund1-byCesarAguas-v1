#Este bucle solo sirve para las eleciones que no estan previamente anidadas (AKA 'Pensadas!'),
#Caso contrario devuelve el control a main con la misma eleccion que el usuario eligio.
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    #pass
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    while eleccion not in opciones:
        print('Por favor ingrese una alternativa:', opciones)
        eleccion = input('Ingrese la alternativa: ').lower()
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ##########################################################################
    return eleccion

#####################################################################
#Solamente en caso de que no sean las opciones esperadas.
if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    #validate(numeros, eleccion
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    valida = validate(numeros, eleccion)
    print('Opción válida ingresada:', valida)
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    
    
