package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Libro extends Titulo{
    private GENERO genero;
    private  ArrayList<EjemplarLibro> ejemplares = new ArrayList<>();

    //Libros existentes
    private static ArrayList<Libro> libros = new ArrayList<>();

    public Libro(String nombre, String autor, int ISBN,  GENERO genero) {
        super(nombre, autor, ISBN);
        this.genero = genero;
        libros.add(this);
    }

    //getters y setters

    public GENERO getGenero() {
        return genero;
    }

    public void setGenero(GENERO genero) {
        this.genero = genero;
    }

    public ArrayList<EjemplarLibro> getEjemplares() {
        return this.ejemplares;
    }

    public void setEjemplares(ArrayList<EjemplarLibro> ejemplares) {
        this.ejemplares = ejemplares;
    }

    public static ArrayList<Libro> getLibros() {
        return libros;
    }

    public static void setLibros(ArrayList<Libro> libros) {
        Libro.libros = libros;
    }
    //Metodos

    public static ArrayList<Libro> filtrarLibros(String filtro, String palabra) {
        ArrayList<Libro> resultadosBusqueda = new ArrayList<>();
        palabra = palabra.toLowerCase();

        switch (filtro) {
            case "nombre":
                for (Libro libro:Libro.getLibros()) {
                    if (libro.getNombre().toLowerCase().contains(palabra)){resultadosBusqueda.add(libro);}
                }
                break;
            case "autor":
                for (Libro libro:Libro.getLibros()) {
                    if (libro.getAutor().toLowerCase().contains(palabra)){resultadosBusqueda.add(libro);}
                }
                break;
            case "genero":
                GENERO generoElegido = GENERO.values()[Integer.valueOf(palabra)-1];
                for (Libro libro:Libro.getLibros()) {
                    if (libro.getGenero().equals(generoElegido)){
                        resultadosBusqueda.add(libro);
                    }
                }
                break;
        }

        return resultadosBusqueda;
    }

    public String toString(){
        return "nombre: " + getNombre() + " autor: " + getAutor() + " ISBN: " + getISBN() + " genero: " + genero;
    }

    //Metodo abstracto
    @Override
    public String mostrarse() {
        return ("Libro: " + this.getNombre() + " Escrito por: " + this.getAutor());
    }
}
