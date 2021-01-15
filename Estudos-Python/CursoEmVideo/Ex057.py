# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' e 'F'.
# caso esteja erraddo, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite um sexo válido. [M / F] ')).strip().upper()
print('Sexo {} registrado.'.format(sexo))



