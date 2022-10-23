package gestorAplicacion.libreria;

import java.io.Serializable;

public class EjemplarLibro extends Ejemplar implements Serializable {
    Libro libro;

    public EjemplarLibro(int id, EstadoEjemplar estadoEjemplar, Libro libro) {
        super(id, estadoEjemplar);
        this.libro = libro;
    }

    public Libro getLibro() {
        return libro;
    }
}
