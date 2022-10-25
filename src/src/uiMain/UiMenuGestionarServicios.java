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

            //Se almacena la respuesta del usuario
            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            /**
             * El condicional multiple recibe la respuesta del usuario y en los dos primeros casos se le 
               da el valor de '0' a la variable 'respuesta' para que se ejecute nuevamente el ciclo en el
               caso '0', lo cual hace que después de hacer la devolución o cancelación pertinente el programa
               no finalice y se abra nuevamente el menu inicial  
             */
            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    UiMenuDevoluciones.showMenuDevoluciones(); //Se abre el menu para las devolver un prestamo
                    break;
                case "2":
                    respuesta = "0";
                    UiMenuCancelarReserva.showMenuCancelarReserva(); //Se abre el menu para cancelar una reserva
                    break;
                case "0":
                    UiMenu.showMenu(); //Abre nuevamente el menu inicial
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");

            }
        } while (!respuesta.equals("0"));
    }
}
