import math

# Clase Triángulo
class Triangulo:
    def __init__(self):
        self.__l1 = 0.0
        self.__l2 = 0.0
        self.__l3 = 0.0

    def get_l1(self) -> float:
        return self.__l1

    def get_l2(self) -> float:
        return self.__l2

    def get_l3(self) -> float:
        return self.__l3

    def set_l1(self, lado: float) -> None:
        self.__l1 = lado

    def set_l2(self, lado: float) -> None:
        self.__l2 = lado

    def set_l3(self, lado: float) -> None:
        self.__l3 = lado 

    def esTriangulo(self) -> bool:
        return (self.__l1 + self.__l2 > self.__l3 and self.__l1 + self.__l3 > self.__l2 and self.__l2 + self.__l3 > self.__l1)
    
    def area(self) -> float:
        s = (self.__l1 + self.__l2 + self.__l3) / 2
        return round(math.sqrt(s * (s - self.__l1) * (s - self.__l2) * (s - self.__l3)), 2)

    def perimetro(self) -> float:
        return self.__l1 + self.__l2 + self.__l3

    def tipoTriangulo(self) -> str:
        if self.__l1 == self.__l2 == self.__l3:
            return "Equilatero"
        elif self.__l1 != self.__l2 != self.__l3:
            return "Escaleno"
        else:
            return "Isoceles"

# Clase Círculo
class Circulo:
    def __init__(self):
        self.__diametro = 0.0

    def get_diametro(self) -> float:
        return self.__diametro

    def set_diametro(self, d: float) -> None:
        self.__diametro = d

    def radio(self) -> float:
        return self.__diametro / 2

    def area(self) -> float:
        return round(math.pi * math.pow(self.radio(), 2), 2)
    
    def perimetro(self) -> float:
        return round(2 * math.pi * self.radio(), 2)

# Clase Cilindro 
class Cilindro(Circulo):
    def __init__(self):
        super().__init__()
        self.__altura = 0.0

    def get_altura(self) -> float:
        return self.__altura

    def set_altura(self, a: float) -> None:
        self.__altura = a

    def volumen(self) -> float:
        return round(self.area() * self.__altura, 2)
    
    def area_lateral(self) -> float:
        return round(self.perimetro() * self.__altura, 2)

    def area_total(self) -> float:
        return round(2 * self.area() + self.area_lateral(), 2)

# Clase Cuadrado
class Cuadrado:
    def __init__(self):
        self.__lado = 0.0

    def get_lado(self) -> float:
        return self.__lado

    def set_lado(self, lado: float) -> None:
        self.__lado = lado

    def area(self) -> float:
        return round(self.__lado ** 2, 2)

    def perimetro(self) -> float:
        return round(4 * self.__lado, 2)

# Clase Cubo 
class Cubo(Cuadrado):
    def volumen(self) -> float:
        return round(self.get_lado() ** 3, 2)

    def area_superficial(self) -> float:
        return round(6 * self.area(), 2)

# Clase Rombo
class Rombo:
    def __init__(self):
        self.__diagonal_mayor = 0.0
        self.__diagonal_menor = 0.0
        self.__lado = 0.0
    
    def get__diagonal_mayor(self)->float:
        return self.__diagonal_mayor
    
    def get__diagonal_menor(self)->float:
        return self.__diagonal_menor    
    
    def get__lado(self)->float:
        return self.__lado 

    def set_diagonal_mayor(self, d: float) -> None:
        self.__diagonal_mayor = d

    def set_diagonal_menor(self, d: float) -> None:
        self.__diagonal_menor = d

    def set_lado(self, l: float) -> None:
        self.__lado = l

    def area(self) -> float:
        return round((self.__diagonal_mayor * self.__diagonal_menor) / 2, 2)

    def perimetro(self) -> float:
        return round(4 * self.__lado, 2)
