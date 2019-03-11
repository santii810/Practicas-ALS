class Prestamo():
    def __init__(self, cuotas, importe, interes):
        self.__cuotas_restantes = cuotas
        self.__importe = importe
        self.__interes = interes
        self.__valor_cuotas = importe / cuotas

    @property
    def cuota(self):
        return self.__valor_cuotas + self.__importe * (self.__interes / 100)

    def get_num_cuotas(self):
        return self.__cuotas_restantes

    def paga_cuota(self):
        self.__importe -= self.__valor_cuotas
        self.__cuotas_restantes -= 1

    def amortiza(self, cantidad):
        self.__importe -= cantidad
        self.__valor_cuotas = self.__importe / self.__cuotas_restantes


prestamo = Prestamo(20, 1000, 2)
print(prestamo.get_num_cuotas())
print(prestamo.cuota)
prestamo.paga_cuota()
print(prestamo.get_num_cuotas())
print(prestamo.cuota)
prestamo.amortiza(150)
print(prestamo.get_num_cuotas())
print(prestamo.cuota)
