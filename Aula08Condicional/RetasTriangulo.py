print('-='*20)
print('Analisador de Trinagulos')
print('-='*20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulo')


