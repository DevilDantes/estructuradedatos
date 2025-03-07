package figurageometrica;

public class Cilindro {
    private double radio;
    private double altura;

    public Cilindro() {
        this.radio = 0;
        this.altura = 0;
    }

    public Cilindro(double radio, double altura) {
        setRadio(radio);
        setAltura(altura);
    }

    public double getRadio() {
        return radio;
    }

    public void setRadio(double radio) {
        if (radio > 0) {
            this.radio = radio;
        } else {
            System.out.println("Error: El radio debe ser mayor que 0.");
        }
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        if (altura > 0) {
            this.altura = altura;
        } else {
            System.out.println("Error: La altura debe ser mayor que 0.");
        }
    }

    public double areaBase() {
        return Math.PI * Math.pow(radio, 2);
    }

    public double areaLateral() {
        return 2 * Math.PI * radio * altura;
    }

    public double areaTotal() {
        return 2 * areaBase() + areaLateral();
    }

    public double volumen() {
        return areaBase() * altura;
    }
}
