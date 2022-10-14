package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Libro extends Titulo{
    private String genero;
    public static ArrayList<EjemplarLibro> ejemplares = new ArrayList<>();

    public Libro(String nombre, String autor, int ISBN, String genero) {
        super(nombre, autor, ISBN);
        this.genero = genero;
    }

    public Libro(String genero) {
        this.genero = genero;
    }
}
