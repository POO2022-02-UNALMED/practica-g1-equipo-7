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
            respuesta = Integer.parseInt(sc.nextLine());

            switch (respuesta){
                case 1:
                    respuesta = 0;
                    prestarLibro();
                    break;
                case 2:
                    respuesta = 0;
                    prestarRevista();
                    break;
                case 0:
                    UiMenu.showMenu();
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Por favor selecciona una de las opciones indicadas");
                   // System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while (respuesta!=0);
    }

    public static void generarPrestamoLibro(int resp_submenu){
        String nombre_libro = Servicio.ejemplarLibroDisponibles.get(resp_submenu-1).getLibro().getNombre();
        Prestamo prestamo = new Prestamo(UiMenu.getUsuario(), new Date());
        int id_prestamo = (int)(Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        Servicio.ejemplarLibroDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestamo(prestamo);
        Servicio.ejemplarLibroDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestado(true);
        UiMenu.getUsuario().getPrestamos().add(prestamo);
        UiMenu.getUsuario().getTiquetes().add(tiquete);

        System.out.println("Usted ha escogido el libro: "+   nombre_libro + " y se le ha generado el prestamo con el id " + id_prestamo);
    }

    public static void generarPrestamoRevista(int resp_submenu){
        String nombre_revista = Servicio.ejemplarRevistaDisponibles.get(resp_submenu-1).getRevista().getNombre();
        Prestamo prestamo = new Prestamo(UiMenu.getUsuario(), new Date());
        int id_prestamo = (int)(Math.random() * 10000);
        Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
        Servicio.ejemplarRevistaDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestamo(prestamo);
        Servicio.ejemplarRevistaDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestado(true);
        UiMenu.getUsuario().getPrestamos().add(prestamo);
        UiMenu.getUsuario().getTiquetes().add(tiquete);

        System.out.println("Usted ha escogido la revista: "+   nombre_revista + " y se le ha generado el prestamo con el id " + id_prestamo);

    }

    public static void prestarLibro(){
        Scanner sc = new Scanner(System.in);

        if(UiMenu.getUsuario().isMulta()){
            JOptionPane.showMessageDialog(null, "Lo sentimos, no puede realizar esta acción porque tiene una multa");
           // System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
        }else{

            //Se le presenta una lista de ejemplares que puede prestar, para que escoja
            System.out.println("Ejemplares disponibles: ");
            UiMenuReserva.mostrarEjemplaresLibro();

            //Se crea otro submenú en el que se le pregunta cuál de esos ejemplares anteriores quiere escoger
            //Se ejecuta un bucle hasta que elija una respuesta que esté en el rango indicado
            int resp_submenu = 0;
            while (resp_submenu < 1 || resp_submenu >= Servicio.ejemplarLibroDisponibles.size() ){
                System.out.println("Cual quiere prestar?");
                resp_submenu = Integer.parseInt(sc.nextLine());
                if (resp_submenu > Servicio.ejemplarLibroDisponibles.size() || resp_submenu < 1){
                    JOptionPane.showMessageDialog(null, "Por favor escoja un número válido");
                    //System.out.println("Por favor escoja un número válido");
                }
                else {
                    generarPrestamoLibro(resp_submenu);
                    System.out.println("\n");
                                // Escoge un número correcto y se le crea un tiquete, se le genera el préstamo y se agrega
                                 // todo al usuario que hay en UiMain, además de quitar el Ejemplar
                    UiMenu.showMenu();
                }
            }
        }
    }

    public static void prestarRevista(){
        Scanner sc = new Scanner(System.in);
        if(UiMenu.getUsuario().isMulta()){
            JOptionPane.showMessageDialog(null, "Lo sentimos, no puede realizar esta acción porque tiene una multa");
            //System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
        }else{

            //Se le presenta una lista de ejemplares que puede prestar, para que escoja
            System.out.println("Ejemplares disponibles: ");
            UiMenuReserva.mostrarEjemplaresRevista();

            //Se crea otro submenú en el que se le pregunta cuál de esos ejemplares anteriores quiere escoger
            //Se ejecuta un bucle hasta que elija una respuesta que esté en el rango indicado
            int resp_submenu = 0;
            while (resp_submenu < 1 || resp_submenu >= Servicio.ejemplarRevistaDisponibles.size() ){
                System.out.println("Cual quiere prestar?");

                resp_submenu = Integer.parseInt(sc.nextLine());
                if (resp_submenu > Servicio.ejemplarRevistaDisponibles.size() || resp_submenu < 1){
                    JOptionPane.showMessageDialog(null, "Por favor escoja un número válido");
                    //System.out.println("Por favor escoja un número válido");
                }
                else {
                    generarPrestamoRevista(resp_submenu);
                    System.out.println("\n");
                    UiMenu.showMenu();
                }
            }
        }

    }




}
