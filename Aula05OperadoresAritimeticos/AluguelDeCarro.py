km = float(input("Quantos km percorrido? "))

dias = int(input('Quantos dias ficou alugado? '))

dia = dias * 60

kms = km * 0.30

total = dia + kms

print('Total a pagar sera de {} R$ '.format(total))