
package figurageo;

import java.util.Scanner;

public class Figurageo {


    public static void main(String[] args) {
        // TODO code application logic here
        Scanner teclado = new Scanner(System.in);
        Circulo c = new Circulo();
        
        System.out.print("Digite el radio del circulo: ");
        c.setRadio(teclado.nextDouble());
        
        if(c.esCirculo()){
        System.out.print("El area del circulo es: " + c.area());
        System.out.print("El perimetro del circulo es: " + c.perimetro());
        
    }
        else{
            System.out.print("No es un circulo");
        }
                    
        teclado.close();
    }
    
}
