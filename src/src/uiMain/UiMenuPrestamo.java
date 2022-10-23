package uiMain;

import gestorAplicacion.libreria.*;
import gestorAplicacion.servicios.Prestamo;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Tiquete;
import gestorAplicacion.servicios.Usuario;

import javax.swing.*;
import java.io.Serial;
import java.util.Date;
import java.util.Scanner;

public class UiMenuPrestamo {
    public static void showMenuPrestamo() {
        System.out.println(":: Prestamo");

        String respuesta = "0";
        do {
            System.out.println("");
            System.out.println("1. Prestar Libro");
            System.out.println("2. Prestar Revista");
            System.out.println("0. Regresar");


            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    Servicio.filtrarLibrosDisponibles(UiMenu.getBiblioteca());
                    prestarLibro();
                    break;
                case "2":
                    respuesta = "0";
                    Servicio.filtrarRevistasDisponibles(UiMenu.getBiblioteca());
                    prestarRevista();
                    break;
                case "0":
                    UiMenu.showMenu();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        } while (!respuesta.equals("0"));
    }

    public static void prestarLibro() {
        Scanner sc = new Scanner(System.in);

        if (UiMenu.getUsuario().isMulta()) {
            System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
        } else if (Servicio.getEjemplarLibroDisponibles().size() == 0) {
            System.out.println("No hay libros disponibles");
        } else {

            //Se le presenta una lista de ejemplares que puede prestar, para que escoja
            System.out.println("Ejemplares disponibles: ");
            System.out.println(" ");
            UiMenuReserva.mostrarEjemplaresLibro();
            System.out.println("0. Regresar");

            //Se crea otro submenú en el que se le pregunta cuál de esos ejemplares anteriores quiere escoger
            //Se ejecuta un bucle hasta que elija una respuesta que esté en el rango indicado
            int resp_submenu = 0;
            do {
                System.out.println("");
                System.out.println("Cual quiere prestar?");
                resp_submenu = Integer.parseInt(sc.nextLine());
                if (resp_submenu > Servicio.getEjemplarLibroDisponibles().size() || resp_submenu < 0) {
                    System.out.println("Por favor escoja un número valido");
                } else if (resp_submenu == 0) {
                    showMenuPrestamo();
                } else {
                    EjemplarLibro ejemplarLibro = Servicio.getEjemplarLibroDisponibles().get(resp_submenu - 1);
                    Prestamo.generarPrestamoLibro(UiMenu.getUsuario(), ejemplarLibro, UiMenu.getBiblioteca());
                    System.out.println("Usted ha escogido el libro: " + ejemplarLibro.getLibro().getNombre() +
                            " y se le ha generado el prestamo con el id " + ejemplarLibro.getEstadoEjemplar().getPrestamo().getTiquete().getId());
                    System.out.println("\n");

                    UiMenu.showMenu();
                    resp_submenu = 0;
                    // Escoge un número correcto y se le crea un tiquete, se le genera el préstamo y se agrega
                    // todo al usuario que hay en UiMain, además de quitar el Ejemplar
                }
            } while (resp_submenu != 0);
        }
    }

    public static void prestarRevista() {
        Scanner sc = new Scanner(System.in);
        if (UiMenu.getUsuario().isMulta()) {
            System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
        } else if (Servicio.getEjemplarRevistaDisponibles().size() == 0) {
            System.out.println("No hay Revistas disponibles");
        } else {
            //Se le presenta una lista de ejemplares que puede prestar, para que escoja
            System.out.println("Ejemplares disponibles: ");
            System.out.println("");
            UiMenuReserva.mostrarEjemplaresRevista();
            System.out.println("0. Regresar");
            //Se crea otro submenú en el que se le pregunta cuál de esos ejemplares anteriores quiere escoger
            //Se ejecuta un bucle hasta que elija una respuesta que esté en el rango indicado
            int resp_submenu = 0;
            do {
                System.out.println("");
                System.out.println("Cual quiere prestar?");
                resp_submenu = Integer.parseInt(sc.nextLine());

                if (resp_submenu > Servicio.getEjemplarRevistaDisponibles().size() || resp_submenu < 0) {
                    System.out.println("Por favor escoja un número valido");
                } else if (resp_submenu == 0) {
                    showMenuPrestamo();
                } else {
                    EjemplarRevista ejemplarRevista = Servicio.getEjemplarRevistaDisponibles().get(resp_submenu - 1);
                    Prestamo.generarPrestamoRevista(UiMenu.getUsuario(), ejemplarRevista, UiMenu.getBiblioteca());
                    System.out.println("Usted ha escogido la revista: " + ejemplarRevista.getRevista().getNombre() +
                            " y se le ha generado el prestamo con el id " + ejemplarRevista.getEstadoEjemplar().getPrestamo().getTiquete().getId());
                    System.out.println("\n");

                    UiMenu.showMenu();
                    resp_submenu = 0;
                }

            }while (resp_submenu != 0) ;

        }
    }
}
