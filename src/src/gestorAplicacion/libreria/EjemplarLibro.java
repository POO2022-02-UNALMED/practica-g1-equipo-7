package gestorAplicacion.libreria;

public class EjemplarLibro extends Ejemplar{
    Libro libro;

    public EjemplarLibro(int id, EstadoEjemplar estadoEjemplar, Libro libro) {
        super(id, estadoEjemplar);
        this.libro = libro;
    }

}
