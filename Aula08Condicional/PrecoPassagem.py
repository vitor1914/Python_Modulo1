passagem = int(input('Digite a distancia dessa viagem: '))

pre01 = passagem * 0.50

pre02 = passagem * 0.45

if passagem <= 200:
    print('Sua passagem custara {}'. format(pre01))

else:
    print('Sua passagem custara {}'.format(pre02))