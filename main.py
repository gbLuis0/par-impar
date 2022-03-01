from random import randint, choice
from os import system, name
try:
    from pyfiglet import Figlet
except:
    print('baixando as dependências...')
    system('pip install pyfiglet')
finally:
    from pyfiglet import Figlet

def cls():
    system('cls' if name == 'nt' else 'clear')

verd = '\033[1;32m'
roxo = '\033[1;35m'
f = '\033[m'
per = '\033[37;7m'

cores = '\033[1;31m', verd, '\033[1;33m', '\033[1;34m', roxo, '\033[1;36m'
dec = 's'
while dec == 's':
    c = 0
    while True:
        cls()
        n = 0
        ppc = p = ''
        npc = randint(0, 10)
        cor = choice(cores)

        print(cor+Figlet('big').renderText('P ou I ?').rstrip()+f)
        n = int(input(f'{per}Digite o seu número:{f} '))
        p = input(f'{per}Par ou Ímpar? [P/I]{f} ').strip().upper()[0]
        ppc = 'Ímpar' if 'P' in p else 'Par'
        s = n + npc

        print(f'{roxo}Opções do pc: {f}{ppc}, {npc}')
        if (s % 2 == 0 and p == 'P') or (s % 2 != 0 and p == 'I'):
            print(f'{verd}Você ganhou!!!{f}')
            c += 1
        else:
            print(f'\033[1;31mOps, o computador ganhou de vc...{f}')
            print(f'{roxo}Você ganhou {c} vezes!')
            break
        input('\nenter para continuar')

    dec = input(f'{per}Deseja continuar? [s/n]{f} ').strip().lower()[0]
cls()
print(f'{roxo}Volte sempre ;){f}')
