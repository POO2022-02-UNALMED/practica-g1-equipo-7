package gestorAplicacion.servicios;

import java.io.Serializable;

public class Tiquete implements Serializable {
    private int id;
    private Servicio servicio;

    //Constructor

    public Tiquete(Servicio servicio, int i) {
        this.servicio = servicio;
    }

    //Getters y Setters

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Servicio getServicio() {
        return servicio;
    }

    public void setServicio(Servicio servicio) {
        this.servicio = servicio;
    }
}
