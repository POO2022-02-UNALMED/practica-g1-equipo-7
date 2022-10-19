package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Libro extends Titulo{
    private String genero;
    private  ArrayList<EjemplarLibro> ejemplares = new ArrayList<>();

    //Libros existentes
    private static ArrayList<Libro> libros = new ArrayList<>();

    public Libro(String nombre, String autor, int ISBN, String genero) {
        super(nombre, autor, ISBN);
        this.genero = genero;
        libros.add(this);
    }

    //getters y setters

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
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

    public String toString(){
        return "nombre: " + getNombre() + " autor: " + getAutor() + " ISBN: " + getISBN() + " genero: " + genero;
    }

    //Metodo abstracto
    @Override
    public String mostrarse() {
        return ("Libro: " + this.getNombre() + " Escrito por: " + this.getAutor());
    }
}
