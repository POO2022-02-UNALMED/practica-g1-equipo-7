package gestorAplicacion.libreria;

import java.io.Serializable;

public abstract class Titulo implements Serializable {
    private String nombre;
    private String autor;
    private int ISBN;

    public Titulo(String nombre, String autor, int ISBN) {
        this.nombre = nombre;
        this.autor = autor;
        this.ISBN = ISBN;
    }

    public Titulo() {
    }

    //getters y setters

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getISBN() {
        return ISBN;
    }

    public void setISBN(int ISBN) {
        this.ISBN = ISBN;
    }

    //Metodo abstracto
    public abstract String mostrarse();
}