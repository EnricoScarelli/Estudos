lar = float(input('Largura da parede:'))
alt = float(input('altura da parede:'))
area= lar*alt
print('Sua parede tem a dimensão de {:.0f}m x {:.0f}m e a area é {:.0f}m²'.format(lar,alt,area))
tinta = area/2
print('Para pintar uma parede de {:.0f}m² voce precisara de {:.0f} L'.format(area,tinta))