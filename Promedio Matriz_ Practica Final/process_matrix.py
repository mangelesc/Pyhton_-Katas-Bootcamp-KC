'''
PRÁCTICA FINAL KATAS PROGRAMACIÓN KEEPCODING
Función process_matrix

María Ángeles Córdoba
'''

from process_list import *

def process_matrix(list_of_list):
    '''
    Recibe una matriz de números
    Devuelve una nueva, con el mismo tamaño y número de elementos.
    El valor de cada elemento de la matriz procesada 
    será el promedio de su valor antiguo y los valores de sus vecinos.
    Se considera vecino, aquel elemento con el se comparte una arista.
    (derecha, izquierda, arriba, abajo)
    '''

    process_matrix = []

    #Si la matriz sólo tiene una lista, aplicamos process_list
    if len(list_of_list) == 1:
        process_matrix= process_list(list_of_list)
    
    #si no, procesamos cada elemento, obteniendo sus índices:
    #indice de columna: i
    #indice de fila: j
    else: 
        #Por cada columna de la lista
        for i, column in enumerate(list_of_list): 
            #por cada elemento
            for j, value in enumerate(column):
                #Se procesa
                new_element = process_element(i, j, list_of_list)
                #Se añade a la lista procesada
                process_matrix.append(new_element)

    #dDevolvemos la matriz procesada. 
    return process_matrix


def process_element(i, j, list_of_list):
    '''
    Recibe los incides i(columna) y j(fila) de un elemento, 
    y la matriz en la que se encuentra.
    Devuelve el promedio de su valor y el de sus vecinos.

    ----DIVIDE Y VENCERÁS:----
    Para calcular el valor final del promedio, dividiremos a los vecinos:
    vecinos verticales y horizontales, y una vez procesados estos valores,
    realizaremos el promedio de ambos.
    '''

    #Obtenemos los índices de los vecinos verticales y horizontales
    horizontal_indices = get_neighbours_indices(j, list_of_list[i])
    vertical_indices = get_neighbours_indices(i, list_of_list)
    
    #Obtenemos los valores de ambas listas de indices
    horizontal_values = get_neighbours_values(horizontal_indices, list_of_list[i])
    vertical_values = get_vertical_neighbours_values(j, vertical_indices, list_of_list)
    
    #Calculamos el promedio total
    avr= get_total_average(vertical_values, horizontal_values)

    #Devolvemos el valor final
    return avr


def get_vertical_neighbours_values(j, list_of_indices, list_of_list):
    '''
    Devuelve una lista con los indices de los vecinos verticales.
    Se incluye al propio elemento en la lista.
    '''
    vertical_values = []

    #Por cada elemento de la lista
    #que representa el índice de columna
    for column in list_of_indices:

        #Comprobamos que la longitud de la columna[j] de list_of_list
        #es mayor o igual a j (en caso de que la longitud de esa columna sea menos que 
        #la longitud de la columna de j, por lo que no existirá vecino en esa columna)
        if (len((list_of_list[column]))-1) >= j:

            #Añadimos el valor de esa columna de la fila j
            #(fila del valor actual pasada por parámetro)
            vertical_values.append(list_of_list[column][j])
        
        #si no, no calculamos el valor, ya que ese  vecino no existiría
        else: 
            pass

    return vertical_values


def get_total_average(vertical_values, horizontal_values):
    '''
    Reciba las listas de valores vecinos.
    Devuelve el total del promedio de todos los vecinos de un valor.
    '''
    #Calculamos el promedio de cada una de las listas
    vertial_avr = get_average(vertical_values)
    horizontal_avr = get_average(horizontal_values)

    #Calculamos el promedio del resultado anterior
    total_avr = [vertial_avr, horizontal_avr]

    return get_average(total_avr)
