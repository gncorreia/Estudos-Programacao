# Escreva um programa que leia um valor e metros e o exiba convertido em centímetros e milímetros.
print('Conversor teste do Gabriel')
n = float(input('Digite o valor em metros: '))
print('{} metros é igual a {} centimetro e igual a {} milimetros'.format(n, (n * 100), (n * 1000)))
print('Que também corresponde a {} quilometros, {} hectometros, {:.1f} decametros e {} decimetros'.format((n * 0.001), (n * 0.01), (n * 0.1), (n * 10)))
