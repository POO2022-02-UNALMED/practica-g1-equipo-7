package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Revista extends Titulo{
    private String categoria;
    public static ArrayList<EjemplarRevista> ejemplares = new ArrayList<>();

    public Revista(String categoria) {
        this.categoria = categoria;
    }

    public Revista(String nombre, String autor, int ISBN, String categoria) {
        super(nombre, autor, ISBN);
        this.categoria = categoria;
    }
}
