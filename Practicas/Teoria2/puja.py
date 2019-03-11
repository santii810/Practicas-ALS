import datetime


class Puja():
    def __init__(self, importe, fecha):
        self.importe = importe
        self.fecha = fecha

    def __str__(self) -> str:
        return self.fecha.strftime("%d/%m/%y %H:%M:%S") + " - " + str(self.importe) + "€"


class Venta():
    def __init__(self, usuario):
        self._usuario = usuario

    @property
    def usuario(self):
        return self._usuario

    def __str__(self):
        return self.usuario + "ganó"


class Subasta(Venta):
    def __init__(self):
        self.pujas = []

    def añadirPuja(self, puja):
        if len(self.pujas) > 0:
            if self.pujas[len(self.pujas) - 1].importe < puja.importe:
                self.pujas += [puja]
        else:
            self.pujas += [puja]

    def __str__(self):
        toret = ""
        for i in self.pujas:
            toret += str(i) + "\n"
        return toret


now = datetime.datetime.now()
ventas = Subasta()
ventas.añadirPuja(Puja(20, now))
ventas.añadirPuja(Puja(20, now))
ventas.añadirPuja(Puja(30, now))
ventas.añadirPuja(Puja(20, now))
ventas.añadirPuja(Puja(50, now))
print(ventas)
