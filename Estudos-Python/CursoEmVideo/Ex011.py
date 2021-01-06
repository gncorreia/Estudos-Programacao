# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².
a = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
area = a * l
print('A área entre {} e {} é igual a {}m²'.format(a, l, area))
print('Para pinta uma área de {}m² é necessário {}L de tinta'.format(area, (area / 2)))
