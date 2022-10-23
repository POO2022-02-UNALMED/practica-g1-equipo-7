package gestorAplicacion.libreria;

import java.io.Serializable;

public class EjemplarRevista extends Ejemplar implements Serializable {
    Revista revista;

    public EjemplarRevista(int id, EstadoEjemplar estadoEjemplar, Revista revista) {
        super(id, estadoEjemplar);
        this.revista = revista;
    }

    public Revista getRevista() {
        return revista;
    }


}
