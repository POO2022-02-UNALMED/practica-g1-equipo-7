package gestorAplicacion.libreria;

public class EjemplarRevista extends Ejemplar{
    Revista revista;

    public EjemplarRevista(int id, EstadoEjemplar estadoEjemplar, Revista revista) {
        super(id, estadoEjemplar);
        this.revista = revista;
    }

    public Revista getRevista() {
        return revista;
    }


}
