frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# análise
len(frase)
frase.count('o')
frase.count('o',0,13)
frase.find('deo')
'Curso'in frase

#Transformação
frase.replace('Pyrhon','Android')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()
frase.strip()
frase.rstrip()
frase.lstrip()

# Divisão
frase.split()

# Junção
'-'.join(frase)

