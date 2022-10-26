from linear_board import LinearBoard
from settings import BOARD_SIZE


class SquareBoard:
    """
    Clase que representa un tablero Cuadrado
    
    Métodos para:

    1. Añadir un carácter (jugar en una columna)
    2. Detectar la victoria de un jugador
    3. Detectar el empate de 2 jugadores
    4. Detectar que el tablero está lleno
    
    """

    def __init__(self):
        self._columns = [LinearBoard()] * BOARD_SIZE

    def is_full(self):
        all_full = True
        for element in self._columns:
            all_full = all_full and element.is_full()
        return all_full



    def is_victory(self, char):
        pass

    def add(self, char, index):
        pass
