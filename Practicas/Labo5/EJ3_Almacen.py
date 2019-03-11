class Pieza:
    pass


class Tuberia(Pieza):
    def __init__(self, longitud):
        self.longitud = longitud

    def __str__(self):
        return "Tuberia " + str(self.longitud) + "mm"


class Tuerca(Pieza):
    def __init__(self, diametro):
        self.diametro = diametro

    def __str__(self):
        return "Tuerca " + str(self.diametro) + "mm"


class Codo(Pieza):
    def __init__(self, angulo):
        self.angulo = angulo

    def __str__(self):
        return "Codo " + str(self.angulo) + "º"


class Inventario:
    def __init__(self):
        self.piezas = list()

    def alta(self, pieza):
        self.piezas += [pieza]

    def baja(self, indice):
        pass

    def modificacion(self):
        pass

    def __getitem__(self, item):
        return self.piezas[item]

    def __len__(self):
        return len(self.piezas)


inventario = Inventario()
inventario.alta(Codo(90))
inventario.alta(Tuerca(90))
inventario.alta(Tuberia(90))

print(len(inventario))
