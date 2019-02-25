class Empresa:
    ventas = {0, 0, 0, 0, 0, 0, 0}

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.ventas = {}

    def ventas_totales(self):
        ventasTotales = 0
        for i in self.ventas:
            ventasTotales += int(i)
        return ventasTotales

    def __str__(self):
        return "Empresa: " + str(self.id) + " " + self.name + "\tVentas totales: " + str(self.ventas_totales())


def read_first_line(data):
    i = 0;
    empresas = []
    while i < len(data):
        emp = Empresa(data[(i)], data[(i + 1)])
        empresas.append(emp)
        i = i + 2
    return empresas


def read_last_lines(lineas, empresas):
    for i in range(1, len(lineas) - 1):
        linea = lineas[i].split(", ")
        for emp in empresas:
            if emp.id == linea[0]:
                emp.fecha_ventas = linea[1]
                emp.ventas = [linea[2], linea[3], linea[4], linea[5], linea[6], linea[7], linea[8]]
    return empresas


f = open("datos.txt")
lineas = f.read().split("\n")
empresas = read_first_line(lineas[0].split(", "))
empresas = read_last_lines(lineas, empresas)

for i in empresas:
    print(i)
