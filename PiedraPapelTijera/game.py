from play import * 
from random import choice

def run_game():
    '''
    Arranca el juego
    '''
    display_game()
    while True:
        lets_play()
        try: 
            keep_playing = input(f"\n¿Do you want to play again? Choose one of the following options: \n  1 . Yes! Let's do it again \n 2. No, that's enough playing")
            keep_playing = int(keep_playing)
            if keep_playing == 1: 
                continue
            else:
                print(f'Bye, bye!')
                break
        except: 
            print(f'Ups, valor incorrecto!')


def display_game():
    '''
    Muestra el nombre del juego
    '''
    print(f'\n\n\nROCK - PAPER - SCISSORS - LIZARD - SPOCK')


def lets_play():
    user_play = get_user_play()
    comp_play = random_play()
    win = get_winner(user_play, comp_play)
    if win == None: #empate
        return display_tie(user_play, comp_play)
    else:
        if win == Result.WINS:
            winner = user_play
        else: 
            winner = comp_play

        return display_victory(winner)


def get_user_play():
    '''
    Presenta un menú de selecciones y pide que elija una
    Usando un diccionario 
    Devuelve el objeto que ha elegido. 
    '''
    print(f'\nChoose your play: \n 1. Rock \n 2. Paper \n 3. Scissors\n 4. Lizard\n 5. Spock\n')
    dict = {1: Rock(), 2: Paper(), 3: Scissors(), 4: Lizard(), 5: CaptainSpock()}
    while True: 
        try: 
            raw = input(f'Enter 1, 2, 3, 4 or 5: ')
            #Validar raw (Quita espacios antes y después)
            raw = int(raw)
            
            if raw>=1 or raw<=3:
                return dict[raw]
        except: 
            print(f'Ups, valor incorrecto!')


def random_play():
    '''
    Selecciona una juegada ramdom para competir con el usuario
    '''
    return choice ([Rock(), Paper(), Scissors(), Lizard(), CaptainSpock()])

def get_winner(play1,play2):
    '''
    Obtiene el vencedor o None si hay empate
    '''
    return play1.compare(play2)

def display_tie(play1,play2):
    '''
    Muestra que ha habido un empate
    '''
    print(f"{play1.name()} and {play2.name()}.\nUps, that' a tie!")

def display_victory(winner):
    '''
    Muestra que winner ha ganado
    '''
    print(f"And the winner is... \n {winner} !!!")

#Iniciamos el juego
if __name__ == '__main__':
    run_game()