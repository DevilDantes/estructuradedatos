/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package figurageom;

/**
 *
 * @author Javier
 */
public class cuadrado {
    
    private double lado;

    public double getLado() {
        return lado;
    }

    public void setLado(double lado) {
        this.lado = lado;
    }
    public cuadrado(){
        this.lado=0;
    } 

    public cuadrado(double lado) {
        this.lado = lado;
    }
    public boolean esCuadrado(){
        return lado>0;
}
    public double area(){
        return lado*lado;
    }
    public double perimetro(){
        return 4*lado;
    }
}
