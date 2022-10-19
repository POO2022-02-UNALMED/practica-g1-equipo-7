package gestorAplicacion.servicios;


import gestorAplicacion.libreria.Libro;
import gestorAplicacion.libreria.Titulo;
import gestorAplicacion.libreria.EjemplarRevista;
import gestorAplicacion.libreria.EjemplarLibro;

import java.util.ArrayList;

public abstract class Servicio {
    public static ArrayList<EjemplarRevista> ejemplarRevistaDisponibles = new ArrayList<>();
    public static ArrayList<EjemplarLibro> ejemplarLibroDisponibles = new ArrayList<>();
    private Usuario usuario;
    private Titulo tituloEscogido;

    //Constructores

    public Servicio(Usuario usuario, Titulo tituloEscogido) {
        this.usuario = usuario;
        this.tituloEscogido = tituloEscogido;
    }

    //getters y setters
    public ArrayList<EjemplarRevista> getEjemplarRevistaDisponibles() {
        return ejemplarRevistaDisponibles;
    }

    public void setEjemplarRevistaDisponibles(ArrayList<EjemplarRevista> ejemplarRevistaDisponibles) {
        Servicio.ejemplarRevistaDisponibles = ejemplarRevistaDisponibles;
    }

    public ArrayList<EjemplarLibro> getEjemplarLibroDisponibles() {
        return ejemplarLibroDisponibles;
    }

    public void setEjemplarLibroDisponibles(ArrayList<EjemplarLibro> ejemplarLibroDisponibles) {
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

    //metodos
    //Metodo que implementa la ligadura dinamica
    public String mostrarTituloEscogido(){
        return (this.getTituloEscogido().mostrarse());
    }
}
