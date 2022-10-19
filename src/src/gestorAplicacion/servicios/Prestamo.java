package gestorAplicacion.servicios;

import gestorAplicacion.libreria.Libro;
import gestorAplicacion.libreria.Revista;
import gestorAplicacion.libreria.Titulo;

import java.util.Date;

public class Prestamo extends Servicio{
    Date fecha;

    //Constructores

    public Prestamo(Usuario usuario, Titulo tituloEscogido, Date fecha) {
        super(usuario, tituloEscogido);
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

    @Override
    public String toString() {
        return (this.mostrarTituloEscogido()+ " Fecha prestamo: " + this.getFecha());
    }
}
