package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Libro extends Titulo{
    private String genero;
    public static ArrayList<EjemplarLibro> ejemplares = new ArrayList<>();

    public Libro(String genero) {
        this.genero = genero;

    }


}
