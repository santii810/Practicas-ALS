import math


def media(numbers):
    media = 0.0
    for i in numbers:
        media += i / len(numbers)
    return media


def mayor(numbers):
    mayor = 0
    for i in numbers:
        mayor = max(mayor, i)
    return mayor


def menor(numbers):
    menor = 99999999999
    for i in numbers:
        menor = min(menor, i)
    return menor


def desviacion_tipica(numbers):
    tmp = 0.0
    for i in numbers:
        tmp += i ** 2 / len(numbers)
    tmp -= media(numbers) ** 2
    return math.sqrt(tmp)


# num = 1
# numbers = []
# while num != 0:
#     num = int(input("Numero: "))
#     if num != 0:
#         numbers += [num]

numbers = [1, 3, 6, 8, 4]
print("media: " + str(media(numbers)))
print("mayor: " + str(mayor(numbers)))
print("menor: " + str(menor(numbers)))
print("desviacion tipica: " + str(desviacion_tipica(numbers)))
