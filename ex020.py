from random import shuffle
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
lista = [a1,a2,a3,a4]
shuffle(lista)
print('A ordem de apresentaçao foi:')
print(lista)
