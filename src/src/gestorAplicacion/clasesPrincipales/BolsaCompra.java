package gestorAplicacion.clasesPrincipales;

import java.util.ArrayList;

public class BolsaCompra {
    private ArrayList<Producto> productos = new ArrayList<>();
    private Usuario usuario;
    private int subtotal;

    /*buscará el producto pasado por parámetro en la lista y si lo encuentra, lo eliminará*/
    public void eliminarProducto(Producto producto){

    }

    public void aumentarProducto(Producto producto){
    }

    public void disminuirProducto(Producto producto){

    }

    public int VerCantidad(){
        return productos.size();
    }

    public int verCantidad(Producto producto){
        int cantidad = 0;
        for(Producto producto1: productos){
            if (producto1 == producto){
                cantidad++;
            }
        }
        return cantidad;
    }

    public void pagarProdBolsa(){
    }







}
