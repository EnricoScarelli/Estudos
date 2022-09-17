real = float(input('Quanto voce tem na carteira? R$:'))
dolar = (real/3.27)
libra = (real/6.42)
print('Com R${:.2f} voce pode comprar US${:.2f} e £{:.2f}' .format(real,dolar,libra))