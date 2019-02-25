def dar_cambio(objetivo, recursos):
    cambio = "Cambio: "
    for i in recursos.keys():
        while objetivo >= i and recursos[i] > 0:
            objetivo -= i
            recursos[i] -= 1
            cambio += str(i) + ", "
    return cambio


def dar_cambio_recursivo(objetivo, recursos, i):
    if objetivo == 0:
        return "."
    if recursos[1] == 0:
        return "error, falta cambio"
    if 0 < list(recursos.keys())[i] <= objetivo:
    # if list(recursos.keys())[i] > 0 and objetivo >= list(recursos.keys())[i]:
        print(objetivo)
        objetivo -= list(recursos.keys())[i]
        return str(list(recursos.keys())[i]) + " "+dar_cambio_recursivo(objetivo,recursos,i)
    else:
        i += 1
    return dar_cambio_recursivo(objetivo, recursos, i)



monedas = {100: 3, 50: 0, 20: 3, 10: 6, 5: 4, 2: 4, 1: 3}
# print(dar_cambio(237, monedas))
print(dar_cambio_recursivo(237, monedas, 0))
