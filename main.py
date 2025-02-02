from random import randint
from colors import coloric_text, question_color, purple, green

keep_playing = True
banner = open('banner.txt', 'r').read()

while keep_playing:
    win_count = 0

    while True:
        print('\x1b[2J\x1b[1;1H')
        number = 0
        pair_odd_pc = pair_odd = ''

        print(banner)
        # player options
        number = input(coloric_text('Digite o seu número: ', question_color))
        numer = int(number)

        pair_odd = input(coloric_text('Par ou Ímpar? [P/I] ', question_color))
        pair_odd = pair_odd.strip().upper()[0]

        # pc options
        pair_odd_pc = 'Ímpar' if 'P' in pair_odd else 'Par'
        pc_number = randint(0, 10)

        sum = number + pc_number

        print(coloric_text('Opções do pc:', purple), pair_odd_pc, pc_number)

        if (sum % 2 == 0 and pair_odd == 'P') or (sum % 2 != 0 and pair_odd == 'I'):
            coloric_text('Você ganhou!!!', green, True)
            win_count += 1
        else:
            coloric_text('Ops, o computador ganhou de vc...', '\033[1;31m', True)
            coloric_text(purple, 'Você ganhou %d vezes!' % win_count, True)
            break
        
        input('\nenter para continuar')

    keep_playing = input(coloric_text('Deseja continuar? (enter para sair) ', question_color)) or False

print('\x1b[2J\x1b[1;1H')
coloric_text('Volte sempre ;)', purple, True)
