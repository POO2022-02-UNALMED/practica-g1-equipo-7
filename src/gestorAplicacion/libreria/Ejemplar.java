package gestorAplicacion.libreria;

import java.io.Serializable;

public class Ejemplar implements Serializable {
    private int id;
    private EstadoEjemplar estadoEjemplar;

    public Ejemplar(int id, EstadoEjemplar estadoEjemplar) {
        this.id = id;
        this.estadoEjemplar = estadoEjemplar;
    }

    public int getId() {
        return id;
    }

    public EstadoEjemplar getEstadoEjemplar() {
        return estadoEjemplar;
    }


}
