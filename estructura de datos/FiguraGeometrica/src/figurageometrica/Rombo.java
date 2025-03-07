package figurageometrica;

public class Rombo {
    private double diagonalMayor;
    private double diagonalMenor;
    
    public Rombo() {
        this.diagonalMayor = 0;
        this.diagonalMenor = 0;
    }
    
    public Rombo(double diagonalMayor, double diagonalMenor) {
        setDiagonalMayor(diagonalMayor);
        setDiagonalMenor(diagonalMenor);
    }
    
    public double getDiagonalMayor() {
        return diagonalMayor;
    }
    
    public void setDiagonalMayor(double diagonalMayor) {
        if(diagonalMayor > 0)
            this.diagonalMayor = diagonalMayor;
        else
            System.out.println("Error: La diagonal mayor debe ser mayor a 0.");
    }
    
    public double getDiagonalMenor() {
        return diagonalMenor;
    }
    
    public void setDiagonalMenor(double diagonalMenor) {
        if(diagonalMenor > 0)
            this.diagonalMenor = diagonalMenor;
        else
            System.out.println("Error: La diagonal menor debe ser mayor a 0.");
    }
    
    public boolean esRombo() {
        return diagonalMayor > 0 && diagonalMenor > 0;
    }
    
    public double area() {
        return (diagonalMayor * diagonalMenor) / 2;
    }
    
    public double lado() {
        return Math.sqrt(Math.pow(diagonalMayor / 2, 2) + Math.pow(diagonalMenor / 2, 2));
    }
    
    public double perimetro() {
        return 4 * lado();
    }
}
