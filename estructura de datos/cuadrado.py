import math

class Cuadrado:
    def __init__(self, lado=0):
        self.__lado = lado
    
    def get_lado(self)->float:
        return self.__lado
    
    def set_lado(self, lado:float)->None:
        self.__lado = lado

    def esCuadrado(self)-> bool:
        return self.__lado>0
    
    def area(self)-> float:
        return self.__lado ** 2
    
    def perimetro(self)-> float:
        return 4 * self.__lado

def main():
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
        c = Cuadrado(lado)

        if c.esCuadrado():
            print(f"el area del cuadrado es: {c.area():.2f}")
            print(f"el perimetro del cuadrado es: {c.perimetro():.2f}")
        else:
            print("No es un Cuadrado")
    except ValueError:
        print("Error, introduzca un numero valido")

if __name__ == "__main__":
    main()


