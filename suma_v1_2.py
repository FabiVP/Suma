class OperacionesAritmeticas():


    def calcularsuna(self):
        return sumando1 + sumando2


    def leerSumandos(self):
    sumando1 = int(input("primer sumando"))
    sumando2 = int(input("segundo sumando"))
    return sumando1, sumando2


    if __name__ --'__main__':
    operacion = OperacionesAritmeticas()
    sumando1, sumando2 = operacion.leerSumandos()
    print(f"{sumando1} + {sumando2} = {operacion.calcularsuna(sumando1, sumando2)}")
