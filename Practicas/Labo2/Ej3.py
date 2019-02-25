def analizador(elements):
    if len(elements) == 1:
        return elements[0]
    op = elements[0]
    x = int(elements[1])
    y = analizador(elements[2:])
    # Print to debug
    print(str(x) + op + str(y) + " = " + str(do_operation(op, x, int(y))))
    return do_operation(op, int(x), int(y))


def do_operation(op, x, y):
    operations = {'+': x + y, '-': x - y, '*': x * y, "/": x / y, "^": x ** y}
    return operations[op]


expresion = "+ 1 - 5 * 2 4"
elements = expresion.split(' ')
print(analizador(elements))
