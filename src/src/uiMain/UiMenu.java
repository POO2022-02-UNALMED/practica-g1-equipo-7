package uiMain;

import gestorAplicacion.servicios.Usuario;

import java.util.Scanner;

public class UiMenu {
    //Esta variable es para manejar todas las listas de prestamos y reservas, luego veremos si es mejor instanciar solo un usuario para ver las funcionalidades así o hacer un log con el nombre
    //No sé si eso sea recaer en multiusuarios
    private static Usuario usuario = new Usuario("", 1);

    //getters, solo necesitamos este
    public static Usuario getUsuario() {
        return usuario;
    }

    public static void showMenu(){

        System.out.println(":: Bienvenido a la Biblioteca");
        System.out.println("Selecciona la opción deseada");

        int respuesta = 0;
        do {
            System.out.println("1. Hacer una consulta");
            System.out.println("2. Realizar una reserva");
            System.out.println("3. Realizar un prestamo");
            System.out.println("4. Hacer devolcion");
            System.out.println("5. Cancelar una reserva");
            System.out.println("0. Salir del sistema");

            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            switch (respuesta){
                case 1:
                    respuesta = 0;
                    UiMenuBusqueda.showMenuBusqueda();
                    break;
                case 2:
                    respuesta = 0;
                    UiMenuReserva.showMenuReserva();
                    break;
                case 3:
                    respuesta = 0;
                    UiMenuPrestamo.showMenuPrestamo();
                    break;
                case 4:
                    respuesta = 0;
                    UiMenuDevoluciones.showMenuDevoluciones();
                    break;
                case 5:
                    respuesta = 0;
                    UiMenuCancelarReserva.showMenuCancelarReserva();
                    break;
                case 0:
                    System.out.println("Gracias por visitarnos");
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while(respuesta!=0);
    }
}
