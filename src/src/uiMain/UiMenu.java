package uiMain;

import baseDatos.Serializador;
import gestorAplicacion.libreria.Biblioteca;
import gestorAplicacion.servicios.Usuario;
import javax.swing.JOptionPane;
import java.util.Scanner;

public class UiMenu {
    //Esta variable es para manejar todas las listas de prestamos y reservas, luego veremos si es mejor instanciar solo un usuario para ver las funcionalidades así o hacer un log con el nombre
    //No sé si eso sea recaer en multiusuarios
    private static Biblioteca biblioteca = new Biblioteca();
    private static Usuario usuario = biblioteca.getUsuarios().get(0);
    //public static Inicializador inicializador = new Inicializador();


    //getters, solo necesitamos este
    public static Biblioteca getBiblioteca() {
        return biblioteca;
    }

    public static Usuario getUsuario() {return usuario;}

    public static void showMenu(){
        //inicializador.inicializar();
        System.out.println("");
        System.out.println(":: Bienvenido a la Biblioteca");
        System.out.println("");
        System.out.println("Selecciona la opcion deseada");
        System.out.println("");
        //JOptionPane.showMessageDialog(null, ":: Bienvenido a la Biblioteca JJ_SALES");
        System.out.println("Selecciona una de las opciones");

        String respuesta = "0";
        do {
            System.out.println("1. Hacer una consulta");
            System.out.println("2. Realizar una reserva");
            System.out.println("3. Realizar un prestamo");
            System.out.println("4. Recomendaciones de libros o revistas");
            System.out.println("5. Gestionar Servicios");
            System.out.println("0. Salir del sistema");


            Scanner sc = new Scanner(System.in);
            respuesta = (String) sc.nextLine();

            switch (respuesta){
                case "1":
                    respuesta = "0";
                    UiMenuBusqueda.showMenuBusqueda();
                    break;
                case "2":
                    respuesta = "0";
                    UiMenuReserva.showMenuReserva();
                    break;
                case "3":
                    respuesta = "0";
                    UiMenuPrestamo.showMenuPrestamo();
                    break;
                case "4":
                    respuesta = "0";
                    UiMenuRecomendar.showMenuRecomendar();
                    break;
                case "5":
                    respuesta = "0";
                    UiMenuGestionarServicios.showMenuGestion();
                    break;
                case "0":
                    //System.out.println("Gracias por visitarnos");
                    System.out.println("Gracias por visitarnos");

                    //Al salir se guarda lo que se hizo
                    Serializador.serializar(biblioteca);
                    System.exit(0);
                    break;
                default:
                    //System.out.println("Por favor selecciona una de las opciones indicadas");
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while(!respuesta.equals("0"));
    }
}
