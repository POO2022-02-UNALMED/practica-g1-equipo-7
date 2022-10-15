package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Revista extends Titulo{
    private String categoria;
    public static ArrayList<EjemplarRevista> ejemplares = new ArrayList<>();

    public Revista(String categoria) {
        this("Independiente","Escritor anónimo",(int) (Math.random() * 10000), categoria);




    }

    public Revista(String nombre, String autor, int ISBN, String categoria) {
        super(nombre, autor, ISBN);
        this.categoria = categoria;
    }

    public Revista() {
        this("Revista UNAL","Universidad Nacional de Colombia", (int) (Math.random() * 10000),"Actualidad");

    }
}
