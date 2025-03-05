/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package figurageometrica;

/**
 *
 * @author Javier
 */
public class Cubo {
    private double lado;

    public double getLado() {
        return lado;
    }
    public Cubo() {
        this.lado = 0;
    }
    public void setLado(double lado) {
        this.lado = lado;
    }

    public Cubo(double lado) {
        this.lado = lado;
    }
    
     public double areaSuperficial() {
        return 6 * lado * lado;
    }

    public double volumen() {
        return lado * lado * lado;
    }

    public double perimetroTotal() {
        return 12 * lado;
    }
}
    

