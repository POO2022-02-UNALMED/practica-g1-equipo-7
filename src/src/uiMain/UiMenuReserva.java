package uiMain;

import java.util.Scanner;

public class UiMenuReserva {
    public static void showMenuReserva(){
        System.out.println(":: Reservas");

        int respuesta = 0;
        do {
            System.out.println("\n\n");
            System.out.println("1. Reservar Libro");
            System.out.println("2. Reservar Revista");
            System.out.println("0. Regresar");
            System.out.println("\n\n");

            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            switch (respuesta){
                case 1:
                    respuesta = 0;
                    //Logica de  Reserva libro
                    break;
                case 2:
                    respuesta = 0;
                    //Logica de reserva revista
                    break;
                case 0:
                    UiMenu.showMenu();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while (respuesta!=0);
    }
}
