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

    //Getters y Setters

    public CATEGORIA getCategoria() {
        return categoria;
    }

    public void setCategoria(CATEGORIA categoria) {
        this.categoria = categoria;
    }

    //Metodos

    /**
     * Esta función permite filtrar las revistas disponibles a las preferencias que indique el usuario 
     * @param filtro Filtro (según el 'nombre', 'autor' o 'categoria') seleccionado por el usuario para buscar revistas
     * @param palabra Palabra clave para buscar revistas (brindada por el usuario)
     * @param biblioteca Biblioteca donde se encuentran las revistas disponible a filtrar
     * @return Retorna una lista con todos los resultados que se encontraron con el filtro
     */
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
    
    /**
     * Esta función sirve para filtrar las revistas más utilizadas por categoria (tomando en cuenta el historial de revistas usadas) 
     * @param biblioteca Biblioteca en la que se encuentran las revistas a filtrar
     * @param categoria Categoria de las revistas
     * @return Retorna los resultados que se encontraron compatibles con el filtro aplicado
     */
    public static ArrayList<Revista> masSolicitadas(Biblioteca biblioteca, CATEGORIA categoria) {
        ArrayList<Revista> revistas = new ArrayList<>();

        for (Revista revista:biblioteca.getHistorialRevistasUsadas()) {
            if (revista.getCategoria()==categoria && !revistas.contains(revista)){
                revistas.add(revista);
            }
        }

        Collections.sort(revistas);
        return revistas;
    }

    /**
     * Esta función sirve para filtrar las revistas más utilizadas en general (tomando en cuenta el historial de revistas usadas)
     * @param biblioteca Bibliote en la que se encuentran las revistas a filtrar
     * @return Retorna los resultados que se encontraron compatibles con el filtro aplicado
     */
    public static ArrayList<Revista> masSolicitadas(Biblioteca biblioteca){
    	ArrayList<Revista> revistas = new ArrayList<>();

        for (Revista revista:biblioteca.getHistorialRevistasUsadas()) {
            if (!revistas.contains(revista)){
                revistas.add(revista);
            }
        }

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
