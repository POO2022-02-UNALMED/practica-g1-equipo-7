package gestorAplicacion.libreria;

import baseDatos.Deserializador;
import gestorAplicacion.servicios.Usuario;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;

public class Biblioteca implements Serializable{

    private static final long serialVersionUID = 1L;
    private  ArrayList<EjemplarLibro> ejemplaresLibros = new ArrayList<>();
    private ArrayList<EjemplarRevista> ejemplaresRevistas = new ArrayList<>();

    private ArrayList<Libro> libros = new ArrayList<>();
    private ArrayList<Revista> revistas = new ArrayList<>();
    private ArrayList<Usuario> usuarios = new ArrayList<>();

    private ArrayList<Libro> historialLibrosUsados = new ArrayList<>();
    private ArrayList<Revista> historialRevistasUsadas = new ArrayList<>();

    //Constructor, escribimos los array guardados en los archivos
    public Biblioteca(){
        Deserializador.deserializar(this);
        }

    //Getters y Setters

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

    public ArrayList<Usuario> getUsuarios() {
        return usuarios;
    }

    public void setUsuarios(ArrayList<Usuario> usuario) {
        this.usuarios = usuario;
    }

    public ArrayList<Libro> getHistorialLibrosUsados() {
        return historialLibrosUsados;
    }

    public void setHistorialLibrosUsados(ArrayList<Libro> historialLibrosUsados) {
        this.historialLibrosUsados = historialLibrosUsados;
    }

    public ArrayList<Revista> getHistorialRevistasUsadas() {
        return historialRevistasUsadas;
    }

    public void setHistorialRevistasUsadas(ArrayList<Revista> historialRevistasUsadas) {
        this.historialRevistasUsadas = historialRevistasUsadas;
    }

    //Metodos

    public void a??adirLibro(Libro libro){
        this.libros.add(libro);
    }

    public void a??adirRevista(Revista revista){
        this.revistas.add(revista);
    }

    public void a??adirEjemplarLibro(EjemplarLibro ejemplarLibro){
        this.ejemplaresLibros.add(ejemplarLibro);
    }

    public void a??adirEjemplarRevista(EjemplarRevista ejemplarRevista){
        this.ejemplaresRevistas.add(ejemplarRevista);
    }

    public void a??adirUsuario(Usuario usuario){this.usuarios.add(usuario);}

    public void a??adirHistorialLibrosUsados(Libro libro){
        historialLibrosUsados.add(libro);
    }

    public void a??adirHistorialRevistasUsadas(Revista revista){
        historialRevistasUsadas.add(revista);
    }
}
