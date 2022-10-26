from process_list import *

def process_matrix(elements):
    '''
    Recibe una matriz y devuelve una nueva, 
    de la misma longitud.
    Cada elemento será el promedio de sus valores vecinos
    (derecha, izquierda, arriba, abajo)
    '''

    process_matrix = []


    #Si la matriz sólo tiene una lista, aplicamos process_list
    if len(elements) == 1:
        process_matrix= process_list(elements)
    
    else: 
        # por cada elemento de la lista
        for i, column in enumerate(elements): 
            for j, value in enumerate(column):
                # lo proceso
                new_element = process_element(i, j, elements)
                # lo añado a la lista 
                process_matrix.append(new_element)

    return process_matrix

def process_element(i, j, elements):
    '''
    Recive el índice de un elemento, y la matriz en la que se encuentra
    Devuelve el promedio de su valor y el de sus vecinos.
    '''
    # obtengo la lista de vecinos
    indices = get_neighbours_indices(i, j, elements)
    values = get_neighbours_values(indices, elements)

    # calculo su promedio
    avr = get_average(values)

    # lo promedio con el elemento es sí
    # devuelve el valor final

    return avr

def get_neighbours_indices(i, j, elements):
    '''
    Devuelve una lista con los indices de los vecinos.
    Se incluye al propio elemento en la lista
    '''
    neighbours_indices = []

    #añadimos los índices vecinos
    #(anteriores, posteriores, arriba y abajo)
    neighbours_indices.append([i, j+1])
    neighbours_indices.append([i, j-1])
    neighbours_indices.append([i+1, j])
    neighbours_indices.append([i-1, j])

    
    def fil (i,j,elements):
        return elements[i][i]>= 0 and i[j] <len(elements)

    filtered_indices = filterindex(neighbours_indices, elements)
    '''COMPROBAR'''

    result = list(filtered_indices)

    return result


def filterindex(list_of_indices, elements):
    '''
    Función que recorre una lista donde previamente
    hemos almacenado los índices vecinos
    Filtra los valores imposibles
    '''
    result = []

    #recorremos la lista de indices
    for i in list_of_indices:
        for j in i:

            #si es mayor o igual a 0 Y menores que la longitud de la lista
            if j>= 0 and j <len(elements):

                #se añaden a la lista de resultados
                result.append(list_of_indices[j]) 
    
    ''''
    filtramos la lista de resultado,
    sólo añadimos a la lista final aquellas listas que tengas dos valores (columna y valor)
    ya que si sólo tienen un valor, será devido a que uno de los valores previamente
    almacenado era un valor imposible. 
    '''
    final_result = filter(lambda i: len(result[i]) == 2, result)

    final_result = list(final_result)
        
    return final_result


def get_neighbours_values(list_of_indices, elements):
    """
    Devuelve la lista de ínidces de los vecinos. Se incluye al
    propio elemento
    """
    values = []
    for i, column in enumerate(list_of_indices):
        values.append(elements([i][0])([i][1]))
    return values