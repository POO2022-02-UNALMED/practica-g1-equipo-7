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
    public static void generarPrestamoLibro(Usuario usuario, EjemplarLibro ejemplarPrestado, Biblioteca biblioteca) {

        Prestamo prestamo = new Prestamo(usuario, ejemplarPrestado, ejemplarPrestado.getLibro(), new Date());
        int id_prestamo = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        prestamo.setTiquete(tiquete);
        ejemplarPrestado.getEstadoEjemplar().setPrestamo(prestamo);
        ejemplarPrestado.getEstadoEjemplar().setPrestado(true);
        //Se agrega al historial de libros usados de bublioteca y usuario, y se aumenta su indice de uso
        biblioteca.añadirHistorialLibrosUsados(ejemplarPrestado.getLibro());
        usuario.getHistorialLibrosUsados().add(ejemplarPrestado.getLibro());
        ejemplarPrestado.getLibro().usado();
        //Se remueve de disponibles el libro prestado
        Servicio.getEjemplarLibroDisponibles().remove(ejemplarPrestado);
        usuario.getPrestamos().add(prestamo);
        usuario.getTiquetes().add(tiquete);
    }

    public static void generarPrestamoRevista(Usuario usuario, EjemplarRevista ejemplarRevistaPrestada, Biblioteca biblioteca) {

        Prestamo prestamo = new Prestamo(usuario, ejemplarRevistaPrestada, ejemplarRevistaPrestada.getRevista(), new Date());
        int id_prestamo = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        prestamo.setTiquete(tiquete);
        ejemplarRevistaPrestada.getEstadoEjemplar().setPrestamo(prestamo);
        ejemplarRevistaPrestada.getEstadoEjemplar().setPrestado(true);
        //Se agrega al historial de revistas usadas de bublioteca y usuario, y se aumenta su indice de uso
        biblioteca.añadirHistorialRevistasUsadas(ejemplarRevistaPrestada.getRevista());
        usuario.getHistorialRevistasUsadas().add(ejemplarRevistaPrestada.getRevista());
        ejemplarRevistaPrestada.getRevista().usado();
        //Se remueve la revista prestada
        Servicio.getEjemplarRevistaDisponibles().remove(ejemplarRevistaPrestada);
        usuario.getPrestamos().add(prestamo);
        usuario.getTiquetes().add(tiquete);
    }

    public static void devolucion(int indiceTituloDevolucion, Biblioteca biblioteca, Usuario usuario){
        Prestamo prestamoAEliminar = usuario.getPrestamos().get(indiceTituloDevolucion);
        Tiquete tiqueteAEliminar = null;

        for (Tiquete tiquete: usuario.getTiquetes()) {
            if (tiquete.getServicio().equals(prestamoAEliminar)){
                tiqueteAEliminar = tiquete;
            }
        }

        prestamoAEliminar.getEjemplarEscogido().getEstadoEjemplar().setPrestado(false);
        usuario.getPrestamos().remove(prestamoAEliminar);
        usuario.getTiquetes().remove((tiqueteAEliminar));
    }
    @Override
    public String toString() {
        return (this.mostrarTituloEscogido()+ " Fecha prestamo: " + this.getFecha());
    }
}
