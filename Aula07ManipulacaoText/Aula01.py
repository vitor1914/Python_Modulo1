frase = 'Fazendo cupim caseiro'
print(frase[1:15:2]) #fatia a frase, pegando o pelo numero da posição a frase 1

print(frase.count('o')) #Conta quantos "o" tem na frase

print(frase.upper().count('f')) #upper deixa maiusculo

print(len(frase)) #Conta quantidade de letras na frase com espaços

print(len(frase.strip())) #Tira espaços inutilizaveis

print(frase.replace('cupim', 'picanha')) #Substitui um nome pelo outro novo

print('caseiro' in frase) #verifica se a palavra caseiro esta dentro da frase

print(frase.find('cupim')) #Verifica qual posição esta a palavra

print(frase.split()) #Separa a frase

dividido = frase.split()

print(dividido[0][2]) #[0] verifica qual palavra é [2] verifica qual palavra é na casa 2 
