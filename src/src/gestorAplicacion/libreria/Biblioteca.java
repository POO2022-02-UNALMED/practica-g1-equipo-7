package gestorAplicacion.libreria;

import baseDatos.Deserializador;
import gestorAplicacion.servicios.Usuario;

import java.io.Serializable;
import java.util.ArrayList;

public class Biblioteca implements Serializable{

    private static final long serialVersionUID = 1L;
    private  ArrayList<EjemplarLibro> ejemplaresLibros = new ArrayList<>();
    private ArrayList<EjemplarRevista> ejemplaresRevistas = new ArrayList<>();

    private ArrayList<Libro> libros = new ArrayList<>();
    private ArrayList<Revista> revistas = new ArrayList<>();

    //Constructor, escribimos los array guardados en los archivos
    public Biblioteca(){Deserializador.deserializar(this);}

    private static Usuario usuario;

    //getters y setters

    public ArrayList<EjemplarLibro> getEjemplaresLibros() {
        return ejemplaresLibros;
    }

    public void setEjemplaresLibros(ArrayList<EjemplarLibro> ejemplaresLibros) {
        this.ejemplaresLibros = ejemplaresLibros;
    }

    public ArrayList<EjemplarRevista> getEjemplaresRevistas() {
        return ejemplaresRevistas;
    }

    public void setEjemplaresRevistas(ArrayList<EjemplarRevista> ejemplaresRevistas) {
        this.ejemplaresRevistas = ejemplaresRevistas;
    }

    public ArrayList<Libro> getLibros() {
        return libros;
    }

    public void setLibros(ArrayList<Libro> libros) {
        this.libros = libros;
    }

    public ArrayList<Revista> getRevistas() {
        return revistas;
    }

    public void setRevistas(ArrayList<Revista> revistas) {
        this.revistas = revistas;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        Biblioteca.usuario = usuario;
    }

    //Metodos

    public void añadirLibro(Libro libro){
        this.libros.add(libro);
    }

    public void añadirRevista(Revista revista){
        this.revistas.add(revista);
    }

    public void añadirEjemplarLibro(EjemplarLibro ejemplarLibro){
        this.ejemplaresLibros.add(ejemplarLibro);
    }

    public void añadirEjemplarRevista(EjemplarRevista ejemplarRevista){
        this.ejemplaresRevistas.add(ejemplarRevista);
    }
}
