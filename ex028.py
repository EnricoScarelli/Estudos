from random import randint
from time import sleep
computador = randint(0,5) #Faz o PC 'PENSAR'
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente ativinhar...')
print('-=-'*20)
jogador = int(input('Em que numero pensei: ')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO:')
sleep(3)
if jogador == computador:
    print('PARABENS, vc ganhou!!')
else:
    print('GANHEI! Eu pensei no numero {} e nao no numero {}'.format(computador,jogador))
