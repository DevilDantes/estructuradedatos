import math

class Rectangulo:
    def __init__(self, largo=0, ancho=0):
        self.__largo = largo
        self.__ancho = ancho
    
    def get__largo(self):
        return self.__largo
    
    def get__ancho(self):
        return self.__ancho
    
    def esRectangulo(self):
        return self.__largo>0 and self.__ancho>0
    
    def area(self):
        return self.__largo * self.__ancho
    
    def perimetro(self):
        return 2*(self.__largo + self.__ancho)
def main():
    try:
        largo=float(input("Ingrese el largo del rectangulo: "))
        ancho=float(input("Ingrese el ancho del rectangulo: "))
        r = Rectangulo(largo,ancho)

        if r.esRectangulo():
            print(f"el area del rectangulo: {r.area():.2f}")
            print(f"el perimetro del rectangulo: {r.perimetro():.2f}")
        else:
            print("no es un rectangulo")
    except ValueError:
        print("No hay sistema, por favor ingrese un numero que sea valido")
if __name__ == "__main__":
    main()