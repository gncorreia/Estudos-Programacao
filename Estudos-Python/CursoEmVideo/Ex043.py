# Desenvolva uma lógica que leia o pesa e a altura de uma pessoa, calcule seu IMC e mostre
# seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
peso = float(input('Digite seu  em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura * altura)
if imc < 18.4:
    print('Seu IMC é de {:.2f} e você está abaixo do peso.'.format(imc))
elif imc == 18.5 or imc <= 25.0:
    print('Seu IMC é de {:.2f} e você está no peso ideal.'.format(imc))
elif imc == 25.1 or imc <= 30.0:
    print('Seu IMC é de {:.2f} e você está com sobrepeso.'.format(imc))
elif imc == 30.1 or imc <= 40.0:
    print('Seu IMC é de {:.2f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f} e você está com obesidade morbida'.format(imc))

# elif 18.5 <= imc < 30.0:

