def fmt_coordenadas(x, y):
    return '({:f}, {:f})'.format(x, y)


x = input("1º Nº \t")
y = input("2º Nº \t")

print(fmt_coordenadas(float(x), float(y)))
