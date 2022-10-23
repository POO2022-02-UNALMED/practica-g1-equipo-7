package gestorAplicacion.servicios;

import gestorAplicacion.libreria.*;

import java.io.Serializable;
import java.util.Date;

public class Prestamo extends Servicio implements Serializable {
    Date fecha;

    //Constructores

    public Prestamo(Usuario usuario, Ejemplar ejemplar, Titulo tituloEscogido, Date fecha) {
        super(usuario, ejemplar,tituloEscogido);
        this.fecha = fecha;
    }

    //getters y setters
    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    //metodos
    public static void generarPrestamoLibro(EjemplarLibro ejemplarPrestado, Biblioteca biblioteca) {

        Prestamo prestamo = new Prestamo(biblioteca.getUsuario(), ejemplarPrestado, ejemplarPrestado.getLibro(), new Date());
        int id_prestamo = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        prestamo.setTiquete(tiquete);
        ejemplarPrestado.getEstadoEjemplar().setPrestamo(prestamo);
        ejemplarPrestado.getEstadoEjemplar().setPrestado(true);
        //Se remueve de disponibles el libro prestado
        Servicio.getEjemplarLibroDisponibles().remove(ejemplarPrestado);
        biblioteca.getUsuario().getPrestamos().add(prestamo);
        biblioteca.getUsuario().getTiquetes().add(tiquete);
    }

    public static void generarPrestamoRevista(EjemplarRevista ejemplarRevistaPrestada, Biblioteca biblioteca) {

        Prestamo prestamo = new Prestamo(biblioteca.getUsuario(), ejemplarRevistaPrestada, ejemplarRevistaPrestada.getRevista(), new Date());
        int id_prestamo = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        prestamo.setTiquete(tiquete);
        ejemplarRevistaPrestada.getEstadoEjemplar().setPrestamo(prestamo);
        ejemplarRevistaPrestada.getEstadoEjemplar().setPrestado(true);
        //Se remueve la revista prestada
        Servicio.getEjemplarRevistaDisponibles().remove(ejemplarRevistaPrestada);
        biblioteca.getUsuario().getPrestamos().add(prestamo);
        biblioteca.getUsuario().getTiquetes().add(tiquete);
    }

    public static void devolucion(int indiceTituloDevolucion, Biblioteca biblioteca){
        Prestamo prestamoAEliminar = biblioteca.getUsuario().getPrestamos().get(indiceTituloDevolucion);
        Tiquete tiqueteAEliminar = null;

        for (Tiquete tiquete: biblioteca.getUsuario().getTiquetes()) {
            if (tiquete.getServicio().equals(prestamoAEliminar)){
                tiqueteAEliminar = tiquete;
            }
        }

        prestamoAEliminar.getEjemplarEscogido().getEstadoEjemplar().setPrestado(false);
        biblioteca.getUsuario().getPrestamos().remove(prestamoAEliminar);
        biblioteca.getUsuario().getTiquetes().remove((tiqueteAEliminar));
    }
    @Override
    public String toString() {
        return (this.mostrarTituloEscogido()+ " Fecha prestamo: " + this.getFecha());
    }
}
