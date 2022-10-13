package gestorAplicacion.libreria;

public class EstadoEjemplar {
    private boolean prestado;
    private boolean reservado;
    private boolean retraso;
    private Prestamo prestamo;
    private Reserva reserva;
    private Ejemplar ejemplar;

    public EstadoEjemplar(boolean prestado, boolean reservado, boolean retraso, Prestamo prestamo, Reserva reserva, Ejemplar ejemplar) {
        this.prestado = prestado;
        this.reservado = reservado;
        this.retraso = retraso;
        this.prestamo = prestamo;
        this.reserva = reserva;
        this.ejemplar = ejemplar;
    }
}
