package gestorAplicacion.libreria;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;

public class Revista extends Titulo implements Serializable {
    private CATEGORIA categoria;

    public Revista(CATEGORIA categoria) {
        this("Independiente","Escritor anónimo",(int) (Math.random() * 10000), categoria);
    }

    public Revista() {
        this("Revista UNAL","Universidad Nacional de Colombia", (int) (Math.random() * 10000),CATEGORIA.ACTUALIDAD);
    }

    public Revista(String nombre, String autor, int ISBN, CATEGORIA categoria) {
        super(nombre, autor, ISBN);
        this.categoria = categoria;
    }

    //setters y getters

    public CATEGORIA getCategoria() {
        return categoria;
    }

    public void setCategoria(CATEGORIA categoria) {
        this.categoria = categoria;
    }

    // funcion

    public static ArrayList<Revista> filtrarRevistas(String filtro, String palabra, Biblioteca biblioteca){
        ArrayList<Revista> resultadosBusqueda = new ArrayList<>();
        palabra = palabra.toLowerCase();

        switch (filtro) {
            case "nombre":
                for (Revista revista:biblioteca.getRevistas()) {
                    if (revista.getNombre().toLowerCase().contains(palabra)){resultadosBusqueda.add(revista);}
                }
                break;
            case "autor":
                for (Revista revista:biblioteca.getRevistas()) {
                    if (revista.getAutor().toLowerCase().contains(palabra)){resultadosBusqueda.add(revista);}
                }
                break;
            case "categoria":
                CATEGORIA categoriaElegida = CATEGORIA.values()[Integer.valueOf(palabra)-1];
                for (Revista revista: biblioteca.getRevistas()) {
                    if (revista.getCategoria().equals(categoriaElegida)) {
                        resultadosBusqueda.add(revista);
                    }
                }
                break;
        }

        return resultadosBusqueda;
    }

    public static ArrayList<Revista> masSolicitados(Biblioteca biblioteca, CATEGORIA categoria) {
        ArrayList<Revista> revistas = new ArrayList<>();

        for (Revista revista:biblioteca.getRevistas()) {
            if (revista.getCategoria()==categoria){
                revistas.add(revista);
            }
        }

        Collections.sort(revistas);
        return revistas;
    }

    public static ArrayList masSolicitadas(Biblioteca biblioteca){
        ArrayList<Revista> revistas = biblioteca.getRevistas();
        Collections.sort(revistas);
        return revistas;
    }

    public String toString(){
        return "nombre: " + this.getNombre() + " autor: " + this.getAutor() + " ISBN: " + this.getISBN() + " Categoria: " + categoria;
    }

    //Metodo abstracto
    @Override
    public String mostrarse() {
        return ("Revista: " + this.getNombre() + " Escrita por: " + this.getAutor());
    }
}
