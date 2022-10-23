package uiMain;

import java.util.Scanner;

public class UiMenuGestionarServicios {
    public static void showMenuGestion() {
        System.out.println("");
        System.out.println(":: Gestion de Servicios");
        System.out.println("");
        System.out.println("Que deseas Realizar?");

        String respuesta = "0";
        do {
            System.out.println("");
            System.out.println("1. Realizar Devoluciones");
            System.out.println("2. Cancelar Reservas");

            System.out.println("0. Regresar");


            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    UiMenuDevoluciones.showMenuDevoluciones();
                    break;
                case "2":
                    respuesta = "0";
                    UiMenuCancelarReserva.showMenuCancelarReserva();
                    break;
                case "0":
                    UiMenu.showMenu();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");

            }
        } while (!respuesta.equals("0"));
    }
}
