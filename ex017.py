import math
from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co,ca)
print('A hipotenusa de co e ca  sera {:.2f}'.format(hi))