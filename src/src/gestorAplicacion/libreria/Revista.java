package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Revista extends Titulo{
    private String categoria;
    private ArrayList<EjemplarRevista> ejemplares = new ArrayList<>();

    //Lista de revistas existentes
    private static ArrayList<Revista> revistas = new ArrayList<>();

    public Revista(String categoria) {
        this("Independiente","Escritor anónimo",(int) (Math.random() * 10000), categoria);
    }

    public Revista() {
        this("Revista UNAL","Universidad Nacional de Colombia", (int) (Math.random() * 10000),"Actualidad");
    }

    public Revista(String nombre, String autor, int ISBN, String categoria) {
        super(nombre, autor, ISBN);
        this.categoria = categoria;
        revistas.add(this);
    }

    //setters y getters

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public ArrayList<EjemplarRevista> getEjemplares() {
        return ejemplares;
    }

    public void setEjemplares(ArrayList<EjemplarRevista> ejemplares) {
        this.ejemplares = ejemplares;
    }

    public static ArrayList<Revista> getRevistas() {
        return revistas;
    }

    public static void setRevistas(ArrayList<Revista> revistas) {
        Revista.revistas = revistas;
    }

    public String toString(){
        return "nombre: " + getNombre() + " autor: " + getAutor() + " ISBN: " + getISBN() + " Categoria: " + categoria;
    }
}
