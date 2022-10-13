package gestorAplicacion.servicios;

import java.util.Date;

public class Reserva extends Servicio{
    Date fechaReserva;
    Date fechaDevolucion;

    //Constructores

    public Reserva(Date fechaReserva) {
        this.fechaReserva = fechaReserva;
    }


    //getters y setters

    public Date getFechaReserva() {
        return fechaReserva;
    }

    public void setFechaReserva(Date fechaReserva) {
        this.fechaReserva = fechaReserva;
    }

    public Date getFechaDevolucion() {
        return fechaDevolucion;
    }

    public void setFechaDevolucion(Date fechaDevolucion) {
        this.fechaDevolucion = fechaDevolucion;
    }

    //metodos
}
