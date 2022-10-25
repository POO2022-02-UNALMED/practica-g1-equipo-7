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

    //Getters y Setters

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    //Metodos

    /**
     * Esta función lo que hace es añadir un prestamo al usuario, genera un tiquete y actualiza el 
       estado del libro que prestó
     * @param usuario Usuario al cual se le va a generar el prestamo
     * @param ejemplarPrestado Libro prestado
     * @param biblioteca Biblioteca que contiene los libros que estan disponibles para prestar
     */

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

    /**
     * Esta función lo que hace es añadir un prestamo al usuario, genera un tiquete y actualiza el 
       estado de la revista que prestó
     * @param usuario Usuario al cual se le va a generar el prestamo
     * @param ejemplarRevistaPrestada Revista prestada
     * @param biblioteca Biblioteca que contiene las revistas que estan disponibles para prestar
     */

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

    /**
     * El usuario elige el prestamo a devolver, se busca el prestamo y posteriormente se cambia el estado 
       de esta a 'FALSE'; de esta manera el servicio que estaba prestado vuelve a estar disponible. También
       se elimina el tiquete correspondiente a ese prestamo (almacenado en la lista 'tiquetes')
     * @param indiceTituloDevolucion Es el prestamo que se desea devolver 
     * @param biblioteca Parametro necesario para el contexto de la funcionalidad
     * @param usuario Usuario al que se le va a afectuar la devolucíon del prestamo 
     */

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
