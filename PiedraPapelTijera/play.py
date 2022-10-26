from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2

class Play():
    '''
    Representa una jugada
    '''
    def beats(self):
        '''
        Devuelve un set con aquellos plays a los que self derrota
        '''
        pass

    def compare(self, otherPlay):
        '''
        Se compara con la otra jugada y devuelve un Result
        de la comparación
        '''
        result = ''

        if self == otherPlay:
            result = Result.EQUAL
        elif otherPlay in self.beats():
            result = Result.WINS
        else: 
            result = Result.LOSES
        
        return result

    # Dunders
    
    # Siempre que se pregunt == se llama a eq
    def __eq__(self, other): 
        '''
        Devuelve si el self y Other son equivalentes
        '''
        if isinstance(self, other.__class__):#Si quizás son iguales(misma clase o subclase), comparara propiedades
            return self.description() == other.description()
        else: #Si NO son iguales
            return False 


    def __hash__(self): #Si implemetas iquals es OLIGATORIO implementar hash
        '''
        Devuelve un hash que represente a self
        '''
        return hash(self.description())
    
    def description(self):
        pass

class Paper (Play):
    def beats(self):
        return {Rock(), CaptainSpock()}

    def description(self):
        return (f'Paper')

class Scissors (Play):
    def beats(self):
        return {Paper(), Lizard()}

    def description(self):
        return (f'Scissors')
    


class Rock (Play):
    def beats(self):
        return {Scissors(), Lizard()}
    
    def description(self):
        return (f'Rock')

class Lizard(Play):
    def beats(self):
        return {Paper(), CaptainSpock()}

    def description(self):
        return(f'Lizard')

class CaptainSpock(Play):
    def beats(self):
        return {Scissors(), Rock()}

    def description(self):
        return(f'Captain Spock')
