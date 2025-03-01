import math

class Circulo:
    def __init__(self, radio=0):
        self.__radio = radio
    
    def get_radio(self):
        return self.__radio
    
    def set_radio(self, radio):
        self.__radio = radio

    def es_un_circulo(self):
        return self.__radio > 0
    
    def area(self):
        return math.pi * self.__radio ** 2 
    
    def perimetro(self):
        return 2 * math.pi * self.__radio

def main():
    try:
        c = Circulo()
        c.set__radio(float(input("Ingrese el radio del círculo: ")))
    
        if c.es_un_circulo():
            print(f"El área del círculo es: {c.area():.2f}")
            print(f"El perímetro del círculo es: {c.perimetro():.2f}")
        else:
            print("No es un círculo")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

if __name__ == "__main__":
    main()
