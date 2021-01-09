# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: todos os lado diferentes
a = float(input('Digite o ângulo A: '))
b = float(input('Digite o ângulo B: '))
c = float(input('Digite o ângulo C: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b and a == b and b == c:
    print('É possível fazer um triângulo Equilátero.')
elif b - c < a < b + c and a - c < b < a + c and a - b < c < a + b and a == b or b == c or a == c:
    print('É possível fazer um triângulo Isóceles.')
elif b - c < a < b + c and a - c < b < a + c and a - b < c < a + b and a != b and b != c:
    print('É possível fazer um triângulo Escaleno.')
else:
    print('Não é possível fazer um triângulo.')

# if a < b + c and b < a + c and c < a + b:
#   print('É possível fazer um triângulo')
#   if a == b == c:
#       print('Equilátero.')
#   elif a == b or b == c or a == c:
#       print('Isóceles.')
#   elif a != b != c != a:
#       print('Escaleno.')
# Ou só coloca um else na ultima condição: