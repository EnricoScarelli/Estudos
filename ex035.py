l1= float(input('Primeiro lado'))
l2= float(input('Segundo lado'))
l3=float(input('Terceiro lado'))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Os seguimentos acima podem formar triangulo!')
else:
    print('Os seguimentos acima nao podem formar um triangulo')
