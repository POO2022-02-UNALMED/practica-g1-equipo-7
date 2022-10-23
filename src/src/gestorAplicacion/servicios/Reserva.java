package gestorAplicacion.servicios;

import gestorAplicacion.libreria.*;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.Date;

public class Reserva extends Servicio implements Serializable {
    LocalDate fechaReserva;
    LocalDate fechaDevolucion;

    //Constructores

    public Reserva(Usuario usuario, Ejemplar ejemplar, Titulo tituloEscogido, LocalDate fechaReserva, LocalDate fechaDevolucion) {
        super(usuario, ejemplar,tituloEscogido);
        this.fechaReserva = fechaReserva;
        this.fechaDevolucion = fechaDevolucion;
    }


    //getters y setters

    public LocalDate getFechaReserva() {
        return fechaReserva;
    }

    public void setFechaReserva(LocalDate fechaReserva) {
        this.fechaReserva = fechaReserva;
    }

    public LocalDate getFechaDevolucion() {
        return fechaDevolucion;
    }

    public void setFechaDevolucion(LocalDate fechaDevolucion) {
        this.fechaDevolucion = fechaDevolucion;
    }

    //metodos

    //Esta función lo que hace es añadir la reserva al usuario, generar un tiquete y actualizar el estado del libro que//
    //el usuario reservó. Se le pasan esos parámetros porque son necesarios en el contexto del método//
    public static void generarReservaLibro(Usuario usuario, EjemplarLibro ejemplarLibroReservado, Biblioteca biblioteca, LocalDate fecha_reserva, LocalDate fecha_devolucion){

        Reserva reserva = new Reserva(usuario, ejemplarLibroReservado, ejemplarLibroReservado.getLibro(), fecha_reserva, fecha_devolucion);
        int id_reserva = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(reserva, id_reserva);
        reserva.setTiquete(tiquete);
        ejemplarLibroReservado.getEstadoEjemplar().setReserva(reserva);
        ejemplarLibroReservado.getEstadoEjemplar().setReservado(true);
        //Se agrega al historial de libros usados de bublioteca y usuario,y se aumenta su indice de uso
        biblioteca.añadirHistorialLibrosUsados(ejemplarLibroReservado.getLibro());
        usuario.getHistorialLibrosUsados().add(ejemplarLibroReservado.getLibro());
        ejemplarLibroReservado.getLibro().usado();
        //se elmimina de disponible
        Servicio.getEjemplarLibroDisponibles().remove(ejemplarLibroReservado);
        usuario.getReservas().add(reserva);
        usuario.getTiquetes().add(tiquete);
    }

    public static void generarReservaRevista(Usuario usuario, EjemplarRevista ejemplarRevistaReservada, Biblioteca biblioteca, LocalDate fecha_reserva, LocalDate fecha_devolucion){
        Reserva reserva = new Reserva(usuario,ejemplarRevistaReservada, ejemplarRevistaReservada.getRevista(), fecha_reserva, fecha_devolucion);
        int id_reserva = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(reserva, id_reserva);
        reserva.setTiquete(tiquete);
        ejemplarRevistaReservada.getEstadoEjemplar().setReserva(reserva);
        ejemplarRevistaReservada.getEstadoEjemplar().setReservado(true);
        //Se agrega al historial de revistas usadas de bublioteca y usuario,y se aumenta su indice de uso
        biblioteca.añadirHistorialRevistasUsadas(ejemplarRevistaReservada.getRevista());
        usuario.getHistorialRevistasUsadas().add(ejemplarRevistaReservada.getRevista());
        ejemplarRevistaReservada.getRevista().usado();
        //Se remueve de la lista de disponibles
        Servicio.getEjemplarRevistaDisponibles().remove(ejemplarRevistaReservada);
        usuario.getReservas().add(reserva);
        usuario.getTiquetes().add(tiquete);
    }

    public static void cancelarReserva(int indiceCancelarReserva, Biblioteca biblioteca, Usuario usuario){
        Tiquete tiqueteVacio = null;
        Reserva reservaAEliminar = usuario.getReservas().get(indiceCancelarReserva);
        for (Tiquete tiquete: usuario.getTiquetes()){
            if (tiquete.getServicio().equals(reservaAEliminar)){
                tiqueteVacio = tiquete;
            }
        }
        reservaAEliminar.getEjemplarEscogido().getEstadoEjemplar().setReservado(false);
        usuario.getReservas().remove(reservaAEliminar);
        usuario.getTiquetes().remove(tiqueteVacio);
    }

    @Override
    public String toString() {
        return (this.mostrarTituloEscogido() + " Fecha reserva: " + this.getFechaReserva() + " Fecha Devolucion: " + this.getFechaDevolucion());
    }
}
