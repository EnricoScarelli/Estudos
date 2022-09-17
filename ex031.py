dist = float(input('Qual a distancia da sua viagem?'))
print('Voce esta prestes a começar uma viagem de {}KM'.format(dist))
if dist <= 200:
        preço = dist * 0.5
else:
        preço = dist * 0.45
print('e o preço da sua passagem sera de {:.2f} R$'.format(preço))