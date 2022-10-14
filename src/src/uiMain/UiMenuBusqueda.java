package uiMain;

import gestorAplicacion.libreria.Ejemplar;
import gestorAplicacion.libreria.Titulo;
import gestorAplicacion.servicios.Servicio;

import java.util.ArrayList;
import java.util.Scanner;

public class UiMenuBusqueda {
    public static void showMenuBusqueda(){
        System.out.println(":: Consulta");
        System.out.println("¿Que deseas consultar?");

        int respuesta = 0;
        do {
            System.out.println("\n\n");
            System.out.println("1. Buscar Libro");
            System.out.println("2. Buscar Revista");
            System.out.println("3. Mis Prestamos");
            System.out.println("4. Mis Reservas");
            System.out.println("0. Regresar");
            System.out.println("\n\n");

            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            switch (respuesta){
                case 1:
                    respuesta = 0;
                    //Logica de busqueda de libro
                    break;
                case 2:
                    respuesta = 0;
                    //Logica de busqueda de revista
                    break;
                case 3:
                    respuesta = 0;
                    //Logica de muestra de prestamos
                    break;
                case 4:
                    respuesta = 0;
                    //Logica de muestra de reservas
                    break;
                case 0:
                    UiMenu.showMenu();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while(respuesta!=0);
    }
}
