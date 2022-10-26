from setting import * 
from list_utils import * 

class LinearBoard:
    '''
    Representa un tablero en una sola columna
    x representa jugador 1
    o represetna jugador 2
    None represetna espacio vacío
    '''

    @classmethod #Método de conveniencia para crear objetos con valores ya definidos
    def fromList(cls,list):
        '''
        Crea y devuelve un LInearBoard a partir de una lista
        que represnta una jugada. 
        '''
        board = cls() # LinearBoard() | cls -> evalua a la clase, crea una instancia de la clase
        board._column = list
        return board

    def __init__(self):
        '''
        Inicializa el tablero vacío, lleno de None
        '''
        self._column = [None for i in range(BOARD_COLUMN_SIZE)]
    
    def __str__(self):
        return f'{self._column}'
    
    def is_full(self):
        '''
        Devuelve True si el tablero está lleno
        '''
        #Si el último elemento es None, NO está lleno
        return self._column[-1] != None
    
    def as_list(self):
        '''
        devuevle la representación del tablero como una lista
        Getter de _column
        '''
        return self._column
    
    def add(self, char):
        '''
        Añade una 'ficha' en dicha columna en el primer espacio disponible
        '''
        if not self.is_full():
            #for i in self._column:
            #    if i == None:
            #        i = char
            #Necesitamos encontrar la primera instancia dentro de una lista: INDEX
            i = self._column.index(None)
            self._column[i] = char

    def is_victory(self, char):
        '''
        Define si hay un victoria
        '''
        #Comprobamos si hay vistoria, usando find_streak() 
        return find_streak(self._column, char, VICTORY_STRIKE)

    def is_tie(self, char1, char2):
        '''
        Define si hay un empate
        '''
        no_victory = self.is_victory(char1) == False and self.is_victory(char2) == False
        return no_victory and self.is_full()

