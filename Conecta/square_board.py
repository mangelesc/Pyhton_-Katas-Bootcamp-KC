from functools import reduce
from linear_board import LinearBoard
from square_board_victory import *
from setting import *


class SquareBoard:
    '''
    A partir de un a matriz, 
    crea un tablero
    '''
    @classmethod #NO es un método de la instancia, sino de la clase
    def fromList(cls, list_of_lists): #cls -> clase (NO self instancia)
        '''
        Recive una matriz y devuelve una lista de LinearBoards
        Crea una instancia con valores ya definidos. 
        '''
        columns = []
        for element in list_of_lists:
            columns.append(LinearBoard.fromList(element))
        board = cls()
        board._columns = columns
        return board
    
    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_SIZE)]

    def __str__(self):
        string = ""
        for i in range(BOARD_SIZE):
            string += f"{self._columns[i]._column}\n"
        return string

    def is_full(self):
        all_full = True
        for element in self._columns:
            all_full = all_full and element.is_full()
        return all_full

    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    def add(self, char, column):
        self._columns[column].add(char)


    def as_matrix(self):
        '''
        A partir de un tablero, 
        devuelve su representacón como matriz
        '''
        matrix = []
        for linear_board in self._columns:
            matrix.append(linear_board.as_list())
        return matrix

    '''
    MÉTODOS PARA DEFINIR LOS TIPOR DE VICTORIA
    '''
    def _any_vertical_victory(self, char):
        victory = False
        for linear_board in self._columns:
            victory = victory or linear_board.is_victory(char)
        return victory 

        
    def _any_horizontal_victory(self, char):
        '''
        Averigua si en el tablero hay una victora horizontal, rotando el tablero
        y al tablero resultante si tiene una victoria vertical
        Rotamos la lista de listas, calculando la transpuesta
        '''
        #obtengo la matriz que representa al tablero ACTURAL(self)
        #transpongo esa matriz
        #creo un tablero temporal a partir de esa matriz
        #le pregunto si tiene alguna victoria vertical
        #devuelvo ese valor

        victory = False
        return victory 


    def _any_rising_victory(self, char):
        pass 
    def _any_sinking_victory(self, char):
        pass


b = SquareBoard()
print(b)
b.add('x',2)
print(b)