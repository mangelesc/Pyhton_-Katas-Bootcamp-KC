from setting import *

def find_one(list, needle):
    '''
    Devuelve True si encuentra needle en la lista, en alguna posición
    False si no la encuentra
    '''
    #inicializo found y un contador
    found = False
    i = 0
    #recorro la lista mientras no encuentro needle
    while not found and i < len(list):
        #compruebo si el elemento actual es needle
        if list[i] == needle:
            #Si lo es, termina y devuelve True
            found = True
        i += 1
    #Si llega al final sin encontrar needle, devuelve False 
    return found
    
def find_n(list, needle, n):
    #Compromabos que el número es mayor a 0
    if n > 0:
        #inicializo el bool si hemos encontrado o no needle, el contador de n, y el index)
        count = 0 
        i = 0

        while count<n and i < len(list):
            #Si encuentro needle sumamos 1 al contador
            if list[i] == needle:
                count +=1
            #Sumo 1 al indice
            i += 1
            
        return count >= n
    
    else: 
        return False

def find_streak(list, element, size):
    '''
    Devuelve True si en list hay size o más elementor seguidos
    False en caso contrario o si size es <= 0
    '''
    #inicializo el contador
    count = 0
    positive_number = False

    #comprobamos que es mayor a 0 
    if size > 0:
        #inicializo el indice
        i = 0
        positive_number = True
        
        #MIENTRAS no haya encontrado size elementos seguidos y la lista no se haya terminado
        while count < size and i < len(list):
            
            #si lo element incremento en contador
            if list[i] == element:
                count += 1
            
            #Si no lo encuentro en el elemento siguiente pongo el contador a 0
            else: 
                count = 0
            
            #Avanzo al siguiente elemento
            i += 1
        
    #Devuelvo si el contador de elements es igual a size y es un numero positivo
    return positive_number and count >= size

def first_elements(list_of_lists):
    '''
    Recibe una matriz(lista de listas) y devuelve una lista
    con los primeros elementos de cada una de las listas de la matriz
    '''
    return nth_elements(list_of_lists, 0)

def nth_elements(list_of_lists, n):
    '''
    Recibe una matriz(lista de listas) y devuelve una lista
    con los enésmos elementos de cada una de las listas de la matriz
    '''
    result = []
    for sub_list in list_of_lists:
        result.append(sub_list[n])
    return result

def transpose(list_of_lists):
    '''
    Recbe una matriz y devuelve su transpuesta
    '''
    transpose_list = []
    for index in range(len(list_of_lists)):
        transpose_list.append(nth_elements(list_of_lists, index))
            
    return transpose_list