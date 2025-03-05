/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package figurageometrica;

/**
 *
 * @author Oscar Perez
 */
public class Triangulo {
    // Declaracion de Atributos
    private double l1,l2,l3;
    //Constructores
    public Triangulo(double l1, double l2, double l3) {
        this.l1 = l1;
        this.l2 = l2;
        this.l3 = l3;
    }
    public Triangulo() {
        this.l1 = 0;
        this.l2 = 0;
        this.l3 = 0;
    }
    //Get
    public double getL1() {
        return l1;
    }
    public double getL2() {
        return l2;
    }
    public double getL3() {
        return l3;
    }
    //Set
    public void setL1(double l1) {
        this.l1 = l1;
    }
    public void setL2(double l2) {
        this.l2 = l2;
    }
    public void setL3(double l3) {
        this.l3 = l3;
    }
    //Operativos
    public boolean esTriangulo(){
        return l1 + l2 > l3 && l1 + l3 > l2 && l2 + l3 > l1;
    }
    public double area(){
        double s,a;
        s = (l1+l2+l3)/2;
        a = Math.sqrt(s*(s-l1)*(s-l2)*(s-l3));
        return a;
    }
    public double perimetro(){
        return l1+l2+l3;
    }
    public String tipoTriangulo(){
        if(this.l1 == this.l2 && this.l1 == this.l3){
            return "Equilatero";
        }
        else{
            if(this.l1 != this.l2 && this.l1 != this.l3 && this.l2 != this.l3){
                return "Escaleno";
            }
            else{
                return "Isoceles";
            }
        }
    }     
}
