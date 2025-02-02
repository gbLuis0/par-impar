from random import randint, choice
from colors import coloric_text, question_color, purple, green

dec = 's'
banner = open('banner.txt', 'r').read()

while dec == 's':
    c = 0
    while True:
        print('\x1b[2J\x1b[1;1H')
        n = 0
        ppc = p = ''
        npc = randint(0, 10)

        print(banner)
        n = int(input(coloric_text('Digite o seu número: ', question_color))) 
        p = input(coloric_text('Par ou Ímpar? [P/I] ', question_color)).strip().upper()[0]
        ppc = 'Ímpar' if 'P' in p else 'Par'
        s = n + npc

        print(coloric_text('Opções do pc:', purple), ppc, npc)

        if (s % 2 == 0 and p == 'P') or (s % 2 != 0 and p == 'I'):
            coloric_text('Você ganhou!!!', green, True)
            c += 1
        else:
            coloric_text('Ops, o computador ganhou de vc...', '\033[1;31m', True)
            coloric_text(purple, 'Você ganhou %d vezes!' % c, True)
            break
        
        input('\nenter para continuar')

    dec = input(coloric_text('Deseja continuar? [s/n] ', question_color)).strip().lower()[0]

print('\x1b[2J\x1b[1;1H')
coloric_text('Volte sempre ;)', purple, True)
