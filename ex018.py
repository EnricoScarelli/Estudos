import math
ang= float(input('Digite o angulo que voce deseja:'))
sen = math.sin(math.radians(ang))
print('O angulo {} tem o seno de {:.2f}'.format(ang,sen))
cos = math.cos(math.radians(ang))
print('O angulo {} tem o cosseno de {:.2f}'.format(ang,cos))
tan = math.tan(math.radians(ang))
print('Ao angulo {} tem a tangente{:.2f}'.format(ang,tan))