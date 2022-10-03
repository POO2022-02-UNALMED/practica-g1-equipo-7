package gestorAplicacion.clasesPrincipales;

import java.util.ArrayList;

public class Factura {
    private String fechaVenta;
    private int numeroGuia;
    private boolean entregado;
    private ArrayList<Producto> productos = new ArrayList<>();
    private Usuario usuario;
    private float costoEnvio;
    private float costoProductos;
    private float costoTotal = costoEnvio + costoProductos;

    public void verificarBonificacion(){

    }

    public void agregarAHistorialCompra(){
        usuario.historialCompra.add(this);
    }
}
