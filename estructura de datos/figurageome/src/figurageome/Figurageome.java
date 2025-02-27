package figurageome;

import java.util.Scanner;

public class Figurageome {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Ingrese el lado del rectangulo: ");
        double largo = teclado.nextDouble();
        
        System.out.print("Ingrese el ancho del rectangulo: ");
        double ancho = teclado.nextDouble();
        
        rectangulo r = new rectangulo(largo,ancho); 
        
        if(r.esRectangulo()){
            System.out.println("El area del rectangulo es: " + r.area());
            System.out.println("El perimetro del rectangulo es: " + r.perimetro());

        }
        else{
           System.out.print("No es un rectangulo");
        }
        teclado.close();
    }
    
}
