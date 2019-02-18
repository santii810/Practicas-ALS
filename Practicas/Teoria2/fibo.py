def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fibo_list(n):
    toret = [None] * n
    for i in range(0, n):
        toret[i] = fibo(i)
    return toret


# num = input("Dime el tamaño: ")
num = 0
print(fibo_list(int(num)))
