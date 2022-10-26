'''
PRÁCTICA FINAL KATAS PROGRAMACIÓN KEEPCODING
Función process_matrix

María Ángeles Córdoba
'''

from functools import reduce


def process_list(elements):
    '''
    Recibe una lista de números y devuelve una nueva, con los elementos
    cambiados. Cada elemento de la nueva lista, seráel primedio del valor antiguo y el de sus 
    vecinos
    '''

    processed_list = []

    if len(elements) == 1:
        processed_list = elements
    
    else: 
        #Por cada elemento de la lista
        for i, value in enumerate(elements): 
            #Se procesa
            new_element = process_element(i, elements)
            #Se añade a la lista 
            processed_list.append(new_element)

    return processed_list


def process_element(index, elements):
    '''
    Recibe el indice de un elemento y la lista en la que está, 
    calcula su promedio con sus vecinos y
    devuelve dicho promedio
    '''
    #Obtenemos la lista de vecinos
    indices = get_neighbours_indices(index, elements)
    values = get_neighbours_values(indices, elements)

    #Calcualmos su promedio
    avr = get_average(values)

    return avr


def get_neighbours_indices(index, elements):
    '''
    Devuelve una lista con los indices de los vecinos.
    Se incluye al propio elemento en la lista
    '''

    neighbours_indices = []

    #añadimos los índices anteriores y posteriores
    neighbours_indices.append(index + 1)
    neighbours_indices.append(index - 1)

    #Eliminamso los índices incorrectos de la lista con map
    #(negativos y mayor o igual que la longitud de la lista)
    filtered_indices = filter(lambda i: i>= 0 and i <len(elements), neighbours_indices)

    #Convertimos el resultado de filter en una lista
    result = list(filtered_indices)
    
    #Incluimos al propio elemento como vecino de sí mismo
    result.append(index)

    return result


def get_neighbours_values(indices, elements):
    """
    Devuelve la lista con los valores de los vecinos. Se incluye al
    propio elemento
    """
    values = []
    for index in indices:
        values.append(elements[index])
    return values


def get_average(values):
    '''
    Recibe una lista de números y devuelve su promedio
    '''
    return reduce(lambda accum, b: accum + b, values, 0) / len(values)
