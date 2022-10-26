'''
PRÁCTICA FINAL KATAS PROGRAMACIÓN KEEPCODING
Función process_matrix

María Ángeles Córdoba
'''

from process_matrix import *


square_matrix = [[2,4,5,7],[4,7,9,2],[5,7,3,7],[4,2,6,8]]
one_column_matrix = [[2,4,5,7],[4,7,9,2],[5,7,3,7],[4,2,6,8]]
empty_matrix = []


if __name__ == "__main__":
    #Matriz cuadrada
    averages_sq = process_matrix(square_matrix)
    print(f'Square Matrix: \n{square_matrix}')
    print('AVERAGES')
    print(f'{averages_sq}\n')

    #Matriz de 1 lista
    averages_one = process_matrix(one_column_matrix)
    print(f'One column matrix: \n{square_matrix}')
    print('AVERAGES')
    print(f'{averages_one}\n')

    #Matriz vacía
    averages_emp = process_matrix(empty_matrix)
    print(f'Empty Matrix: \n{empty_matrix}')
    print('AVERAGES')
    print(f'{averages_emp}\n')