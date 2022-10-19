package uiMain;

import gestorAplicacion.libreria.Ejemplar;
import gestorAplicacion.libreria.EjemplarLibro;
import gestorAplicacion.libreria.EjemplarRevista;
import gestorAplicacion.libreria.Libro;
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
                    prestarLibro();
                    break;
                case "2":
                    respuesta = "0";
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

    public static void generarPrestamoLibro(int resp_submenu) {
        String nombre_libro = Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getLibro().getNombre();
        Prestamo prestamo = new Prestamo(UiMenu.getUsuario(), Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getLibro(), new Date());
        int id_prestamo = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setPrestamo(prestamo);
        Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setPrestado(true);
        //Se remueve de disponibles el libro prestado
        Servicio.ejemplarLibroDisponibles.remove(resp_submenu - 1);
        UiMenu.getUsuario().getPrestamos().add(prestamo);
        UiMenu.getUsuario().getTiquetes().add(tiquete);

        System.out.println("Usted ha escogido el libro: " + nombre_libro + " y se le ha generado el prestamo con el id " + id_prestamo);
        UiMenu.showMenu();
    }

    public static void generarPrestamoRevista(int resp_submenu) {
        String nombre_revista = Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getRevista().getNombre();
        Prestamo prestamo = new Prestamo(UiMenu.getUsuario(), Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getRevista(), new Date());
        int id_prestamo = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setPrestamo(prestamo);
        Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setPrestado(true);
        //Se remueve la revista prestada
        Servicio.ejemplarRevistaDisponibles.remove(resp_submenu - 1);
        UiMenu.getUsuario().getPrestamos().add(prestamo);
        UiMenu.getUsuario().getTiquetes().add(tiquete);

        System.out.println("Usted ha escogido la revista: " + nombre_revista + " y se le ha generado el prestamo con el id " + id_prestamo);
        UiMenu.showMenu();

    }

    public static void prestarLibro() {
        Scanner sc = new Scanner(System.in);

        if (UiMenu.getUsuario().isMulta()) {
            System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
        } else if (Servicio.ejemplarLibroDisponibles.size() == 0) {
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
                if (resp_submenu > Servicio.ejemplarLibroDisponibles.size() || resp_submenu < 0) {
                    System.out.println("Por favor escoja un número valido");
                } else if (resp_submenu == 0) {
                    showMenuPrestamo();
                } else {
                    generarPrestamoLibro(resp_submenu);
                    System.out.println("\n");
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
        } else if (Servicio.ejemplarRevistaDisponibles.size() == 0) {
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

                if (resp_submenu > Servicio.ejemplarRevistaDisponibles.size() || resp_submenu < 0) {
                    System.out.println("Por favor escoja un número valido");
                } else if (resp_submenu == 0) {
                    showMenuPrestamo();
                } else {
                    generarPrestamoRevista(resp_submenu);
                    resp_submenu = 0;
                    System.out.println("\n");
                }

            }while (resp_submenu != 0) ;

        }
    }
}
