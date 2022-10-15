package gestorAplicacion.servicios;

import java.time.LocalDate;
import java.util.Date;

public class Reserva extends Servicio{
    LocalDate fechaReserva;
    LocalDate fechaDevolucion;

    //Constructores

    public Reserva(Usuario usuario, LocalDate fechaReserva, LocalDate fechaDevolucion) {
        super(usuario);
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
}
