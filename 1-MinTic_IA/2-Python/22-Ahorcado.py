import random

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
    return WORDS[random.randint(0, len(WORDS)-1)]

def display_board(hidden_word, tries):
    print(IMAGENES[tries])
    print('')
    print(hidden_word)
    print('---*---*---*---*---*---')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

if __name__ == "__main__":
    print('B I E N V E N I D O S A A H O R C A D O S')
    run()