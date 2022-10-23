package gestorAplicacion.servicios;


import gestorAplicacion.libreria.*;
import uiMain.UiMenu;

import java.io.Serializable;
import java.util.ArrayList;

public abstract class Servicio implements Serializable {
    private static ArrayList<EjemplarRevista> ejemplarRevistaDisponibles = new ArrayList<>();
    private static ArrayList<EjemplarLibro> ejemplarLibroDisponibles = new ArrayList<>();
    private Usuario usuario;
    private Titulo tituloEscogido;
    private Ejemplar EjemplarEscogido;
    private Tiquete tiquete;

    //Constructores

    public Servicio(Usuario usuario, Ejemplar ejemplarEscogido,Titulo tituloEscogido) {
        this.usuario = usuario;
        this.EjemplarEscogido = ejemplarEscogido;
        this.tituloEscogido = tituloEscogido;
    }

    //getters y setters
    public static ArrayList<EjemplarRevista> getEjemplarRevistaDisponibles() {
        return ejemplarRevistaDisponibles;
    }

    public static void setEjemplarRevistaDisponibles(ArrayList<EjemplarRevista> ejemplarRevistaDisponibles) {
        Servicio.ejemplarRevistaDisponibles = ejemplarRevistaDisponibles;
    }

    public static ArrayList<EjemplarLibro> getEjemplarLibroDisponibles() {
        return ejemplarLibroDisponibles;
    }

    public static void setEjemplarLibroDisponibles(ArrayList<EjemplarLibro> ejemplarLibroDisponibles) {
        Servicio.ejemplarLibroDisponibles = ejemplarLibroDisponibles;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public Titulo getTituloEscogido() {
        return tituloEscogido;
    }

    public void setTituloEscogido(Titulo tituloEscogido) {
        this.tituloEscogido = tituloEscogido;
    }

    public Ejemplar getEjemplarEscogido() {
        return EjemplarEscogido;
    }

    public void setEjemplarEscogido(Ejemplar ejemplarEscogido) {
        EjemplarEscogido = ejemplarEscogido;
    }

    public Tiquete getTiquete() {
        return tiquete;
    }

    public void setTiquete(Tiquete tiquete) {
        this.tiquete = tiquete;
    }

    //metodos
    public static void filtrarLibrosDisponibles(Biblioteca biblioteca){
        ArrayList<EjemplarLibro> ejemplares = new ArrayList<>();
        for(EjemplarLibro ejemplar: UiMenu.getBiblioteca().getEjemplaresLibros()){
            if(!ejemplar.getEstadoEjemplar().isPrestado() && !ejemplar.getEstadoEjemplar().isReservado()){
                ejemplares.add(ejemplar);
            }
        }
        setEjemplarLibroDisponibles(ejemplares);
    }

    public static void filtrarRevistasDisponibles(Biblioteca biblioteca){
        ArrayList<EjemplarRevista> ejemplares = new ArrayList<>();
        for(EjemplarRevista ejemplar: UiMenu.getBiblioteca().getEjemplaresRevistas()){
            if(!ejemplar.getEstadoEjemplar().isPrestado() && !ejemplar.getEstadoEjemplar().isReservado()){
                ejemplares.add(ejemplar);
            }
        }
        setEjemplarRevistaDisponibles(ejemplares);
    }

    //Metodo que implementa la ligadura dinamica
    public String mostrarTituloEscogido(){
        return (this.getTituloEscogido().mostrarse());
    }
}
