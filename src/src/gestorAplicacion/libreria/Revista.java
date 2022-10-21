package gestorAplicacion.libreria;

import java.util.ArrayList;

public class Revista extends Titulo{
    private CATEGORIA categoria;
    private ArrayList<EjemplarRevista> ejemplares = new ArrayList<>();

    //Lista de revistas existentes
    private static ArrayList<Revista> revistas = new ArrayList<>();

    public Revista(CATEGORIA categoria) {
        this("Independiente","Escritor anónimo",(int) (Math.random() * 10000), categoria);
    }

    public Revista() {
        this("Revista UNAL","Universidad Nacional de Colombia", (int) (Math.random() * 10000),CATEGORIA.ACTUALIDAD);
    }

    public Revista(String nombre, String autor, int ISBN, CATEGORIA categoria) {
        super(nombre, autor, ISBN);
        this.categoria = categoria;
        revistas.add(this);
    }

    //setters y getters

    public CATEGORIA getCategoria() {
        return categoria;
    }

    public void setCategoria(CATEGORIA categoria) {
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

    // funcion

    public static ArrayList<Revista> filtrarRevistas(String filtro, String palabra){
        ArrayList<Revista> resultadosBusqueda = new ArrayList<>();
        palabra = palabra.toLowerCase();

        switch (filtro) {
            case "nombre":
                for (Revista revista:Revista.getRevistas()) {
                    if (revista.getNombre().toLowerCase().contains(palabra)){resultadosBusqueda.add(revista);}
                }
                break;
            case "autor":
                for (Revista revista:Revista.getRevistas()) {
                    if (revista.getAutor().toLowerCase().contains(palabra)){resultadosBusqueda.add(revista);}
                }
                break;
            case "categoria":
                CATEGORIA categoriaElegida = CATEGORIA.values()[Integer.valueOf(palabra)-1];
                for (Revista revista: Revista.getRevistas()) {
                    if (revista.getCategoria().equals(categoriaElegida)) {
                        resultadosBusqueda.add(revista);
                    }
                }
                break;
        }

        return resultadosBusqueda;
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
