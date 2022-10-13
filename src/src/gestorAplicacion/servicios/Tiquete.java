package gestorAplicacion.servicios;

public class Tiquete {
    private int id;
    private Servicio servicio;

    //Constructor

    public Tiquete(Servicio servicio) {
        this.servicio = servicio;
    }

    //getters y setters

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

    //metodos
}
