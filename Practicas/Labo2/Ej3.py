def analizador(elements):
    if len(elements) == 0:
        return 0
    op = elements[0]
    n = elements[1]
    n2 = analizador(elements[2:])


expresion = "+ 1 - 5 * 2 4"
elements = expresion.split(' ')
print(analizador(elements))
