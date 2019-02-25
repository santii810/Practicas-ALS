import random

numeros = []
for i in range(0, 99):
    numeros.append(0)

for i in range(10000):
    x = int(random.random() * 100)
    numeros[x - 1] = numeros[x - 1] + 1

print(numeros)
