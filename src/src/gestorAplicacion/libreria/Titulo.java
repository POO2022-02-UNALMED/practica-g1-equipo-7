package gestorAplicacion.libreria;

import java.io.Serializable;

public abstract class Titulo implements Serializable, Comparable<Titulo> {
    private String nombre;
    private String autor;
    private final int ISBN;
    private int usos = 0;

    public Titulo(String nombre, String autor, int ISBN) {
        this.nombre = nombre;
        this.autor = autor;
        this.ISBN = ISBN;
    }

    public Titulo(int isbn) {
        ISBN = isbn;
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


    public int getUsos() {
        return usos;
    }

    public void setUsos(int usos) {
        this.usos = usos;
    }

    //Metodo abstracto
    public abstract String mostrarse();

    public void usado(){
        usos++;
    }

    @Override
    public int compareTo(Titulo titulo) {
        if (titulo.getUsos()>usos){
            return 1;
        } else if (titulo.getUsos()>usos) {
            return 0;
        }else {
            return -1;
        }
    }
}