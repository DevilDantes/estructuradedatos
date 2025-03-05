from ClasesFigurasGeometrica import *

def triangulo():
    t = Triangulo()
    t.set_l1(float(input("Digite el lado uno del triángulo: ")))
    t.set_l2(float(input("Digite el lado dos del triángulo: ")))
    t.set_l3(float(input("Digite el lado tres del triángulo: ")))
    if t.esTriangulo():
        print("El área del triángulo es:", t.area())
        print("El perímetro del triángulo es:", t.perimetro())
        print("Tipo de triángulo:", t.tipoTriangulo())
    else:
        print("No es un triángulo válido.")

def circulo():
    cir = Circulo()
    cir.set_diametro(float(input("Digite el diámetro del círculo: ")))
    print("El área del círculo es:", cir.area())
    print("El perímetro (circunferencia) es:", cir.perimetro())

def cilindro():
    t = Cilindro()
    t.set_diametro(float(input("Digite el diámetro del cilindro: ")))
    t.set_altura(float(input("Digite la altura del cilindro: "))) 
    print("El volumen del cilindro es:", t.volumen())
    print("El área lateral del cilindro es:", t.area_lateral())
    print("El área total del cilindro es:", t.area_total())

def cuadrado():
    c = Cuadrado()
    c.set_lado(float(input("Digite el lado del cuadrado: ")))
    print("El área del cuadrado es:", c.area())
    print("El perímetro del cuadrado es:", c.perimetro())

def cubo():
    cb = Cubo()
    cb.set_lado(float(input("Digite el lado del cubo: ")))
    print("El volumen del cubo es:", cb.volumen())
    print("El área superficial del cubo es:", cb.area_superficial())

def rombo():
    r = Rombo()
    r.set_diagonal_mayor(float(input("Digite la diagonal mayor del rombo: ")))
    r.set_diagonal_menor(float(input("Digite la diagonal menor del rombo: ")))
    r.set_lado(float(input("Digite el lado del rombo: ")))
    print("El área del rombo es:", r.area())
    print("El perímetro del rombo es:", r.perimetro())

def main():
    while True:
        opcion = int(input("\nMenu Principal\n"
                        "1. Triángulo\n"
                        "2. Círculo\n"
                        "3. Cilindro\n"
                        "4. Cuadrado\n"
                        "5. Cubo\n"
                        "6. Rombo\n"
                        "7. Salir\n"
                        "Digite la opción: "))
        if opcion == 7:
            break
        elif opcion == 1:
            triangulo()
        elif opcion == 2:
            circulo()
        elif opcion == 3:
            cilindro()
        elif opcion == 4:
            cuadrado()
        elif opcion == 5:
            cubo()
        elif opcion == 6:
            rombo()
        else:
            print("Opción no válida.")
        
        input("\nPresione Enter para continuar...")

if __name__ == '__main__':
    main()
