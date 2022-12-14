package gestorAplicacion.libreria;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

public class Libro extends Titulo implements Serializable {
    private GENERO genero;

    public Libro(String nombre, String autor, int ISBN,  GENERO genero) {
        super(nombre, autor, ISBN);
        this.genero = genero;
    }

    //Getters y Setters

    public GENERO getGenero() {
        return genero;
    }

    public void setGenero(GENERO genero) {
        this.genero = genero;
    }

    //Metodos
    
    /**
     * Esta función permite filtrar los libros disponibles a las preferencias que indique el usuario
     * @param filtro Filtro (según el 'nombre', 'autor' o 'genero') seleccionado por el usuario para buscar libros 
     * @param palabra Palabra clave para buscar revistas (brindada por el usuario)
     * @param biblioteca Biblioteca donde se encuentran los libros disponible a filtrar
     * @return Retorna una lista con todos los resultados que se encontraron con el filtro
     */
    public static ArrayList<Libro> filtrarLibros(String filtro, String palabra, Biblioteca biblioteca) {
        ArrayList<Libro> resultadosBusqueda = new ArrayList<>();
        palabra = palabra.toLowerCase();

        switch (filtro) {
            case "nombre":
                for (Libro libro:biblioteca.getLibros()) {
                    if (libro.getNombre().toLowerCase().contains(palabra)){resultadosBusqueda.add(libro);}
                }
                break;
            case "autor":
                for (Libro libro:biblioteca.getLibros()) {
                    if (libro.getAutor().toLowerCase().contains(palabra)){resultadosBusqueda.add(libro);}
                }
                break;
            case "genero":
                GENERO generoElegido = GENERO.values()[Integer.valueOf(palabra)-1];
                for (Libro libro:biblioteca.getLibros()) {
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

    /**
     * Esta función sirve para filtrar los libros más utilizados por gnereo (tomando en cuenta el historial de libros usados) 
     * @param biblioteca Biblioteca en la que se encuentran los libros a filtrar
     * @param genero Genero de los libros
     * @return Retorna los resultados que se encontraron compatibles con el filtro aplicado
     */
    public static ArrayList<Libro> masSolicitados(Biblioteca biblioteca, GENERO genero) {
        ArrayList<Libro> libros = new ArrayList<>();

        for (Libro libro:biblioteca.getHistorialLibrosUsados()) {
            if (libro.getGenero()==genero && !libros.contains(libro)){
                libros.add(libro);
            }
        }

        Collections.sort(libros);

        return libros;
    }

    /**
     * Esta función sirve para filtrar los libros más utilizadas en general (tomando en cuenta el historial de libros usados)
     * @param biblioteca Biblioteca en la que se encuentran los libros a filtrar
     * @return Retorna los resultados que se encontraron compatibles con el filtro aplicado
     */
    public static ArrayList<Libro> masSolicitados(Biblioteca biblioteca){
    	ArrayList<Libro> libros = new ArrayList<>();

        for (Libro libro:biblioteca.getHistorialLibrosUsados()) {
            if (!libros.contains(libro)){
                libros.add(libro);
            }
        }

        Collections.sort(libros);

        return libros;
    }


}

