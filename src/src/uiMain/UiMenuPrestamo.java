package uiMain;

import gestorAplicacion.libreria.Ejemplar;
import gestorAplicacion.libreria.EjemplarLibro;
import gestorAplicacion.libreria.EjemplarRevista;
import gestorAplicacion.libreria.Libro;
import gestorAplicacion.servicios.Prestamo;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Tiquete;
import gestorAplicacion.servicios.Usuario;

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

                    if(Usuario.multa){
                        System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
                    }else{
                        int i = 0;
                        //Se le presenta una lista de ejemplares que puede prestar, para que escoja
                        System.out.println("Ejemplares disponibles: ");
                        for(EjemplarLibro ejemplar: Servicio.ejemplarLibroDisponibles){
                            if(!ejemplar.getEstadoEjemplar().isPrestado() && !ejemplar.getEstadoEjemplar().isReservado()){
                                System.out.println((i+1) +". "+ ejemplar.getLibro().getNombre() + ".  Codigo: " +ejemplar.getId());
                                i++;
                            }

                        }

                        //Se crea otro submenú en el que se le pregunta cuál de esos ejemplares anteriores quiere escoger
                        //Se ejecuta un bucle hasta que elija una respuesta que esté en el rango [1, i]
                        int resp_submenu = 0;
                        while (resp_submenu < 1 || resp_submenu >= i ){
                            System.out.println("Cual quiere reservar?");
                            resp_submenu = Integer.parseInt(sc.nextLine());
                            if (resp_submenu > i || resp_submenu < 1){
                                System.out.println("Por favor escoja un número válido");
                            }
                            else {
                            /*Escoge un número correcto y se le crea un tiquete, se le genera el préstamo y se agrega
                              todo al usuario que hay en UiMain, además de quitar el Ejemplar*/

                                String nombre_libro = Servicio.ejemplarLibroDisponibles.get(resp_submenu-1).getLibro().getNombre();
                                Prestamo prestamo = new Prestamo(UiMenu.getUsuario(), new Date());
                                int id_prestamo = (int)(Math.random() * 10000);
                                Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
                                Servicio.ejemplarLibroDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestamo(prestamo);
                                Servicio.ejemplarLibroDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestado(true);
                                UiMenu.getUsuario().getPrestamos().add(prestamo);
                                UiMenu.getUsuario().getTiquetes().add(tiquete);

                                System.out.println("Usted ha escogido el libro: "+   nombre_libro + " y se le ha generado el prestamo con el id " + id_prestamo);
                                System.out.println("E para continuar");
                                sc.next();
                                UiMenu.showMenu();
                            }
                        }
                    }


                    break;
                case 2:
                    respuesta = 0;
                    if(Usuario.multa){
                        System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
                    }else{
                        int i = 0;
                        //Se le presenta una lista de ejemplares que puede prestar, para que escoja
                        System.out.println("Ejemplares disponibles: ");
                        for(EjemplarRevista ejemplar: Servicio.ejemplarRevistaDisponibles){
                            if(!ejemplar.getEstadoEjemplar().isPrestado() && !ejemplar.getEstadoEjemplar().isReservado()){
                                System.out.println((i+1) +". "+ ejemplar.getRevista().getNombre() + ".  Codigo: " +ejemplar.getId());
                                i++;
                            }

                        }

                        //Se crea otro submenú en el que se le pregunta cuál de esos ejemplares anteriores quiere escoger
                        //Se ejecuta un bucle hasta que elija una respuesta que esté en el rango [1, i]
                        int resp_submenu = 0;
                        while (resp_submenu < 1 || resp_submenu >= i ){
                            System.out.println("Cual quiere reservar?");
                            resp_submenu = Integer.parseInt(sc.nextLine());
                            if (resp_submenu > i || resp_submenu < 1){
                                System.out.println("Por favor escoja un número válido");
                            }
                            else {
                                /*Escoge un número correcto y se le crea un tiquete, se le genera el préstamo y se agrega
                                 todo al usuario que hay en UiMain,
                                 además de actualizar la información del ejemplar*/

                                String nombre_revista = Servicio.ejemplarRevistaDisponibles.get(resp_submenu-1).getRevista().getNombre();
                                Prestamo prestamo = new Prestamo(UiMenu.getUsuario(), new Date());
                                int id_prestamo = (int)(Math.random() * 10000);
                                Tiquete tiquete = new Tiquete(prestamo, id_prestamo);
                                Servicio.ejemplarRevistaDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestamo(prestamo);
                                Servicio.ejemplarRevistaDisponibles.get(resp_submenu-1).getEstadoEjemplar().setPrestado(true);
                                UiMenu.getUsuario().getPrestamos().add(prestamo);
                                UiMenu.getUsuario().getTiquetes().add(tiquete);


                                System.out.println("Usted ha escogido la revista: "+   nombre_revista + " y se le ha generado el prestamo con el id " + id_prestamo);
                                System.out.println("E para continuar");
                                sc.next();
                                UiMenu.showMenu();
                            }
                        }
                    }
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
