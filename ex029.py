vel=float(input('Qual é a velocidade atual do carro?'))
if vel>80:
    print("Voce foi multado")
    multa= (vel-80)*7
    print('Voce deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia e digija com cuidado')

