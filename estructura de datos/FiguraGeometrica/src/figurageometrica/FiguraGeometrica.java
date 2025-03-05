package figurageometrica;

import java.util.Scanner;

public class FiguraGeometrica {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Seleccione la figura:");
        System.out.println("1. Triangulo");
        System.out.println("2. Cuadrado");
        System.out.println("3. Cubo");
        System.out.println("4. Circulo");
        System.out.println("5. Cilindro");
         System.out.println("6. Rombo");
        int opcion = teclado.nextInt();

        if (opcion == 1) {
            Triangulo t = new Triangulo();
            try {
                System.out.print("Digite el lado uno del Triangulo: ");
                t.setL1(teclado.nextDouble());
                System.out.print("Digite el lado dos del Triangulo: ");
                t.setL2(teclado.nextDouble());
                System.out.print("Digite el lado tres del Triangulo: ");
                t.setL3(teclado.nextDouble());

                if (t.esTriangulo()) {
                    System.out.printf("Area: %.2f%n", t.area());
                    System.out.printf("Perimetro: %.2f%n", t.perimetro());
                    System.out.println("Tipo: " + t.tipoTriangulo());
                } else {
                    System.out.println("No es un triangulo valido.");
                }
            } catch (Exception e) {
                System.out.println("Error: Ingrese valores numericos.");
            }
        } 
        else if (opcion == 2) {
            cuadrado c = new cuadrado();
            try {
                System.out.print("Digite el lado del Cuadrado: ");
                c.setLado(teclado.nextDouble());

                System.out.printf("Area: %.2f%n", c.area());
                System.out.printf("Perimetro: %.2f%n", c.perimetro());

            } catch (Exception e) {
                System.out.println("Error: Ingrese un valor numerico.");
            }
        }
        else if (opcion == 3) {
            Cubo cubo = new Cubo();
            try {
                System.out.print("Digite el lado del Cubo: ");
                cubo.setLado(teclado.nextDouble());

                System.out.printf("Area superficial: %.2f%n", cubo.areaSuperficial());
                System.out.printf("Volumen: %.2f%n", cubo.volumen());
                System.out.printf("Perimetro total: %.2f%n", cubo.perimetroTotal());

            } catch (Exception e) {
                System.out.println("Error: Ingrese un valor numerico.");
            }
        } 
        else if (opcion == 4) {
            Circulo circulo = new Circulo();
            try {
                System.out.print("Digite el radio del Circulo: ");
                circulo.setRadio(teclado.nextDouble());

                System.out.printf("Area: %.2f%n", circulo.area());
                System.out.printf("Perimetro (Circunferencia): %.2f%n", circulo.perimetro());

            } catch (Exception e) {
                System.out.println("Error: Ingrese un valor numerico.");
            }
        } 
       else if (opcion == 5) {
    Cilindro cilindro = new Cilindro();
    try {
        System.out.print("Digite el radio del Cilindro: ");
        cilindro.setRadio(teclado.nextDouble());
        System.out.print("Digite la altura del Cilindro: ");
        cilindro.setAltura(teclado.nextDouble());

        System.out.printf("Area base: %.2f%n", cilindro.areaBase());
        System.out.printf("Area lateral: %.2f%n", cilindro.areaLateral());
        System.out.printf("Area total: %.2f%n", cilindro.areaTotal());
        System.out.printf("Volumen: %.2f%n", cilindro.volumen());

    } catch (Exception e) {
        System.out.println("Error: Ingrese valores numericos.");
    }
}
else if (opcion == 6) {
            Rombo rombo = new Rombo();
            try {
                System.out.print("Digite la diagonal mayor del Rombo: ");
                rombo.setDiagonalMayor(teclado.nextDouble());
                System.out.print("Digite la diagonal menor del Rombo: ");
                rombo.setDiagonalMenor(teclado.nextDouble());
                
                if (rombo.esRombo()) {
                    System.out.printf("Area: %.2f%n", rombo.area());
                    System.out.printf("Perimetro: %.2f%n", rombo.perimetro());
                } else {
                    System.out.println("No es un rombo valido.");
                }
            } catch (Exception e) {
                System.out.println("Error: Ingrese valores numericos.");
            }
        } 
        else {
            System.out.println("Opcion no valida.");
        }
        teclado.close();
    }
}
