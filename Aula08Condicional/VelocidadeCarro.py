vel = int(input('Digite a velocidade do carro: '))

valor = (vel - 80) * 7

if vel <= 80:
    print('Velocidade permitida')
else:
    print('Você levou uma multa de {}'. format(valor))


