class Aparato:
    def get_precio(self):
        return self.precio_hora

    def __str__(self):
        return self.nombre


class DVD(Aparato):
    def __init__(self):
        self.precio_hora = 12
        self.nombre = "DVD"


class TV(Aparato):
    def __init__(self):
        self.precio_hora = 12
        self.nombre = "TV"


class Reparacion:
    def __init__(self, aparato, horas):
        self.aparato = aparato
        self.horas = horas

    def __str__(self):
        return "Reparacion: " + str(self.aparato) + " -> " + str(int(self.aparato.get_precio()) * self.horas) + "€"


class Factura:
    def __init__(self, reparacion):
        self.reparacion = reparacion

    def __str__(self):
        return "Factura: " + str(self.reparacion)


print(Factura(Reparacion(DVD(), 3)))
