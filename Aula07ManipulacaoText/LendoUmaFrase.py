frase = str(input('Digite uma frase: ')).upper().strip()
print('Aletra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('Aultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
