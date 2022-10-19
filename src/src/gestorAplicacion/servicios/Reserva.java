package gestorAplicacion.servicios;

import gestorAplicacion.libreria.Libro;
import gestorAplicacion.libreria.Revista;
import gestorAplicacion.libreria.Titulo;

import java.time.LocalDate;
import java.util.Date;

public class Reserva extends Servicio{
    LocalDate fechaReserva;
    LocalDate fechaDevolucion;

    //Constructores

    public Reserva(Usuario usuario, Titulo tituloEscogido, LocalDate fechaReserva, LocalDate fechaDevolucion) {
        super(usuario, tituloEscogido);
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

    @Override
    public String toString() {
        return (this.mostrarTituloEscogido() + " Fecha reserva: " + this.getFechaReserva() + " Fecha Devolucion: " + this.getFechaDevolucion());
    }
}
