package figurageom;

import java.util.Scanner;

public class Figurageom {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Ingrese el lado del Cuadrado: ");
        double lado = teclado.nextDouble();
        
        cuadrado c = new cuadrado(lado);
        
        if(c.esCuadrado()){
            System.out.println("el area del cuadrado es:  " + c.area());
            System.out.println("el perimetro del cuadrado es:  " + c.perimetro());
        }else{
            System.out.print("no es un cuadrado");
        }
        teclado.close();
    }
    
}
