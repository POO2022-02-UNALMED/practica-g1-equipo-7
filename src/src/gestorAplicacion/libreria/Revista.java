package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Revista extends Titulo{
    private String categoria;
    public static ArrayList<EjemplarRevista> ejemplares = new ArrayList<>();

    public Revista(String categoria) {
        this.categoria = categoria;
    }
}
