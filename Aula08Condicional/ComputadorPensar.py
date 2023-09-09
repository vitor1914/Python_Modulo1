import random

num = int(input('Digite um numero de 0 a 5: '))

lista = [0, 1, 2, 3, 4, 5]
comp =random.choice(lista)

print('O número escolhido pelo computador foi {}'.format(comp))
print('Seu numero que voce digitou foi {}'.format(num))

if comp == num:
    print('Você ganhou!')

else:
    print('Você perdeu!')



