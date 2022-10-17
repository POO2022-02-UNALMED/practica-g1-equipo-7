package gestorAplicacion.servicios;

import gestorAplicacion.libreria.Libro;
import gestorAplicacion.libreria.Revista;

import java.time.LocalDate;
import java.util.Date;

public class Reserva extends Servicio{
    LocalDate fechaReserva;
    LocalDate fechaDevolucion;
    Revista revista;
    Libro libro;

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

    @Override
    public String toString() {
        String msgTitulo = "";
        if(this.getTituloEscogido() instanceof Libro){
            msgTitulo = "Libro reservado: " + this.getTituloEscogido().getNombre();
        } else if (this.getTituloEscogido() instanceof Revista) {
            msgTitulo = "Revista reservada: " + this.getTituloEscogido().getNombre();
        }
        return (msgTitulo + " Fecha reserva: " + this.getFechaReserva() + " Fecha Devolucion: " + this.getFechaDevolucion());
    }
}
