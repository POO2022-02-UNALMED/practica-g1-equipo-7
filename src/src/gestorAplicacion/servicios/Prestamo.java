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
        String msgTitulo = "";
        if (this.getTituloEscogido() instanceof Libro) {
            msgTitulo = "Libro reservado: " + this.getTituloEscogido().getNombre();
        } else if (this.getTituloEscogido() instanceof Revista) {
            msgTitulo = "Revista reservada: " + this.getTituloEscogido().getNombre();
        }
        return (msgTitulo + " Fecha prestamo: " + this.getFecha());
    }
}
