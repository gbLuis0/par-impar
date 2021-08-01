from random import randint
print('''\033[36m
 /$$$$$$$                                  /$$$$$$ /$$$$ 
| $$__  $$                                |_  $$_//$$  $$
| $$  \ $$        /$$$$$$  /$$   /$$        | $$ |__/\ $$
| $$$$$$$/       /$$__  $$| $$  | $$        | $$     /$$/
| $$____/       | $$  \ $$| $$  | $$        | $$    /$$/ 
| $$            | $$  | $$| $$  | $$        | $$   |__/  
| $$            |  $$$$$$/|  $$$$$$/       /$$$$$$  /$$  
|__/             \______/  \______/       |______/ |__/  
\033[m''')
#Número e contador
n = c = 0
#Par ou ímpar
ppc = p = ''
while True:
    npc = randint(0, 10)
    n = int(input('\033[37;7mDigite o seu número: [0 a 10]\033[m '))
    p = str(input('\033[37;7mPar ou Ímpar? [P/I]\033[m ')).strip().upper()[0]
    if 'P' in p:
        ppc = 'Ímpar'
    else:
        ppc = 'Par'
    s = n + npc
    print(f'\033[34mOpções do pc:\033[m {ppc}, {npc}')
    if s % 2 == 0 and p == 'P':
        print('\033[32mVocê ganhou!!!\033[m')
        c += 1
    elif s % 2 != 0 and p == 'I':
        print('\033[32mVocê ganhou!!!\033[m')
        c += 1
    else:
        print('\033[31mOps, o computador ganhou de vc...\033[m')
        break
print(f'\033[35mVocê ganhou {c} vezes!\033[m')
print('\033[33mVolte sempre ;)\033[m')
