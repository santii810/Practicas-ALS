def do_operation(x, y, operator):
    operations = {'+': x + y, '-': x - y, '*': x * y, "/": x / y, "^": x ** y}
    return operations[operator]


x = input("1º Nº \t")
y = input("2º Nº \t")
operator = input("operador \t")
print(do_operation(float(x), float(y), operator))
