sa=float(input('Qual era o salario de funcionario?R$ '))
al = sa*0.15
ns=al+sa
print('O salario do funcionario era R${:.0f}, com 15% de aumento (R${:.0f})passou a ganhar R${:.0f}'.format(sa,al,ns))