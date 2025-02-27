import math

class Triangulo:
    def __init__(self, l1=0, l2=0, l3=0):
        self.__l1 = l1
        self.__l2 = l2
        self.__l3 = l3

    def es_triangulo(self):
        return self.__l1 + self.__l2 > self.__l3 and self.__l1 + self.__l3 > self.__l2 and self.__l2 + self.__l3 > self.__l1
    
    def area(self):
        s = (self.__l1 + self.__l2 + self.__l3) / 2
        return math.sqrt(s * (s - self.__l1) * (s - self.__l2) * (s - self.__l3))
    
    def perimetro(self):
        return self.__l1 + self.__l2 + self.__l3
    
    def tipo_triangulo(self):
        if self.__l1 == self.__l2 == self.__l3:
            return "Equilátero"
        elif self.__l1 != self.__l2 and self.__l1 != self.__l3 and self.__l2 != self.__l3:
            return "Escaleno"
        else:
            return "Isósceles"
    
    def get_l1(self):
        return self.__l1
    
    def get_l2(self):
        return self.__l2
    
    def get_l3(self):
        return self.__l3


def main():
    l1 = float(input("Digite el lado uno del Triángulo: "))
    l2 = float(input("Digite el lado dos del Triángulo: "))
    l3 = float(input("Digite el lado tres del Triángulo: "))
    
    t = Triangulo(l1, l2, l3)
    
    if t.es_triangulo():
        print(f"El área del triángulo es: {t.area():.2f}")
        print(f"El perímetro del triángulo es: {t.perimetro():.2f}")
        print(f"El tipo de triángulo es: {t.tipo_triangulo()}")
    else:
        print("No es un triángulo")

if __name__ == "__main__":
    main()