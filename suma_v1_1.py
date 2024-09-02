class OperacionesAritmeticas():
def calcularsuna(sumando1,sumando2):
    return sumando1 + sumando2

def leerSumandos():
    sumando1 = int(input("primer sumando"))
    sumando2 = int(input("segundo sumando"))
    return sumando1,sumando2

if --name-- --'__main__':
    sumando1,sumando2 = leerSumandos()
    print(f"{sumando1} + {sumando2} = {calcularsuna(sumando1,sumando2)}")