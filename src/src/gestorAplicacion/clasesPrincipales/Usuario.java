package gestorAplicacion.clasesPrincipales;

import java.util.ArrayList;

public class Usuario {
    private String nombre;
    private String apellido;
    private int edad;
    private String direccion;
    ArrayList<Factura> historialCompra = new ArrayList<>();
    BolsaCompra bolsaCompra;
    Tarjeta tarjeta;
    Bonificacion bonificacion;

    public void cambiarTarjeta(Tarjeta tarjeta){
        this.tarjeta = tarjeta;
    }

    public Factura verPedido(int numeroPedido){
        return historialCompra.get(numeroPedido);
    }


    public ArrayList<Factura> verPedido(){
        return historialCompra;
    }

    public void registro(){

    }

    /*public ArrayList<Producto> verProductos(){

    }*/

    public void agregarSaldo(float saldo){
        this.tarjeta.saldo = saldo;
    }


}
