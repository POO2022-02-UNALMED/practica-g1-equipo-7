package gestorAplicacion.servicios;

import java.util.Date;

public class Prestamo extends Servicio{
    Date fecha;

    //Constructores

    public Prestamo(Date fecha) {
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
}
