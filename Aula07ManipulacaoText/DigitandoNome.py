nome = str(input('Digite seu nome: ')).strip()

print('Seu nome maiusculo é {}'.format(nome.upper()))

print('Seu nome minusculo é {} '.format(nome.lower()))

print('Seu nome tem {} letras no seu nome'.format(len(nome)-nome.count(' ')))

print('Seu primero nome tem ao todo {} letras'.format(nome.find(' ')))
