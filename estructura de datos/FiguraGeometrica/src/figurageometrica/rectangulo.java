/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package figurageometrica;

/**
 *
 * @author Javier
 */
public class rectangulo {
    private double largo, ancho;

    public double getLargo() {
        return largo;
    }

    public void setLargo(double largo) {
        this.largo = largo;
    }
    public rectangulo(){
        this.largo =0;
        this.ancho=0;
}

    public double getAncho() {
        return ancho;
    }

    public void setAncho(double ancho) {
        this.ancho = ancho;
    }

    public rectangulo(double largo, double ancho) {
        this.largo = largo;
        this.ancho = ancho;
    }
    public boolean esRectangulo(){
        return largo>0 && ancho>0;
    }
    public double area(){
        return largo * ancho;
    }
    public double perimetro(){
        return 2*(largo+ancho);
    }
}
