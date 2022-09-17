real = float(input('qual  e o preço do produto em real? :R$'))
cf = real*0.05
final = real- cf
print('O valor que custava R${}, na promoçao com desconto de 5% vai custar {}'.format(real,final))