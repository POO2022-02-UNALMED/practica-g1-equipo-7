package gestorAplicacion.clasesPrincipales;

public class Tarjeta {
    private Usuario usuario;
    private String nombre;
    private int numeroSerie;
    private int CVC;
    private String fechaVencimiento;
    float saldo;

    public void reembolso(){
        saldo += 50000; /*Cifra cualquiera, inventada de momento*/
    }
}
