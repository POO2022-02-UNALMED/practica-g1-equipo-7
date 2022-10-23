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
    public static void generarReservaLibro(EjemplarLibro ejemplarLibroReservado, Biblioteca biblioteca, LocalDate fecha_reserva, LocalDate fecha_devolucion){

        Reserva reserva = new Reserva(biblioteca.getUsuario(), ejemplarLibroReservado, ejemplarLibroReservado.getLibro(), fecha_reserva, fecha_devolucion);
        int id_reserva = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(reserva, id_reserva);
        reserva.setTiquete(tiquete);
        ejemplarLibroReservado.getEstadoEjemplar().setReserva(reserva);
        ejemplarLibroReservado.getEstadoEjemplar().setReservado(true);
        Servicio.getEjemplarLibroDisponibles().remove(ejemplarLibroReservado);
        biblioteca.getUsuario().getReservas().add(reserva);
        biblioteca.getUsuario().getTiquetes().add(tiquete);
    }

    public static void generarReservaRevista(EjemplarRevista ejemplarRevistaReservada, Biblioteca biblioteca, LocalDate fecha_reserva, LocalDate fecha_devolucion){
        Reserva reserva = new Reserva(biblioteca.getUsuario(),ejemplarRevistaReservada, ejemplarRevistaReservada.getRevista(), fecha_reserva, fecha_devolucion);
        int id_reserva = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(reserva, id_reserva);
        reserva.setTiquete(tiquete);
        ejemplarRevistaReservada.getEstadoEjemplar().setReserva(reserva);
        ejemplarRevistaReservada.getEstadoEjemplar().setReservado(true);
        Servicio.getEjemplarRevistaDisponibles().remove(ejemplarRevistaReservada);
        biblioteca.getUsuario().getReservas().add(reserva);
        biblioteca.getUsuario().getTiquetes().add(tiquete);
    }

    public static void cancelarReserva(int indiceCancelarReserva, Biblioteca biblioteca){
        Tiquete tiqueteVacio = null;
        Reserva reservaAEliminar = biblioteca.getUsuario().getReservas().get(indiceCancelarReserva);
        for (Tiquete tiquete: biblioteca.getUsuario().getTiquetes()){
            if (tiquete.getServicio().equals(reservaAEliminar)){
                tiqueteVacio = tiquete;
            }
        }

        reservaAEliminar.getEjemplarEscogido().getEstadoEjemplar().setReservado(false);
        biblioteca.getUsuario().getReservas().remove(reservaAEliminar);
        biblioteca.getUsuario().getTiquetes().remove(tiqueteVacio);
    }

    @Override
    public String toString() {
        return (this.mostrarTituloEscogido() + " Fecha reserva: " + this.getFechaReserva() + " Fecha Devolucion: " + this.getFechaDevolucion());
    }
}
