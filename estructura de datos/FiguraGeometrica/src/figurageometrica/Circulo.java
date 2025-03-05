/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package figurageometrica;

/**
 *
 * @author Javier
 */
public class Circulo {
    
    private double radio;

    public Circulo(double radio) {
        this.radio = radio;
    }
    public Circulo(){
        this.radio = 0;
    }

    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        this.radio = radio;
    
    }public boolean esCirculo(){
        return radio>0;
    }
    public double area(){
        return Math.PI * Math.pow(radio,2);
    }
    public double perimetro(){
        return 2*Math.PI*radio;
    }
    
}
