sal = int(input('Digite seu salario: '))

if sal >= 1250:
    aum10 = (sal / 100) * 10
    aumento01 = sal + aum10
    print('O seu salario vai ser de {} reais'.format(aumento01))

else:
    aum15 = (sal / 100) * 15
    aumento02 = sal + aum15
    print('Seu salario vai ser {} reais'.format(aumento02))