package uiMain;

import java.util.Scanner;

public class UiMenuPrestamo {
    public static void showMenuPrestamo(){
        System.out.println(":: Prestamo");

        int respuesta = 0;
        do {
            System.out.println("\n\n");
            System.out.println("1. Prestar Libro");
            System.out.println("2. Prestar Revista");
            System.out.println("0. Regresar");
            System.out.println("\n\n");

            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            switch (respuesta){
                case 1:
                    respuesta = 0;
                    //Logica de prestamo libro
                    break;
                case 2:
                    respuesta = 0;
                    //Logica de prestamo Reserva
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
