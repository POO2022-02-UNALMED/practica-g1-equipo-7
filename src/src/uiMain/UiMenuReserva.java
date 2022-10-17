package uiMain;

import gestorAplicacion.libreria.EjemplarLibro;
import gestorAplicacion.libreria.EjemplarRevista;
import gestorAplicacion.servicios.Prestamo;
import gestorAplicacion.servicios.Reserva;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Tiquete;

import javax.swing.*;
import java.time.LocalDate;
import java.util.Date;
import java.util.GregorianCalendar;
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
            respuesta = Integer.parseInt(sc.nextLine());

            switch (respuesta){
                case 1:
                    respuesta = 0;
                    reservarLibro();
                    break;
                case 2:
                    respuesta = 0;
                    reservarRevista();
                    break;
                case 0:
                    UiMenu.showMenu();
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Por favor selecciona una de las opciones indicadas");
                    //System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while (respuesta!=0);
    }

    public static void reservarLibro(){
        Scanner sc = new Scanner(System.in);

        if(UiMenu.getUsuario().isMulta()) {
            JOptionPane.showMessageDialog(null, "Lo sentimos, no puede realizar esta acción porque tiene una multa");
            //System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
        }else{

            mostrarEjemplaresLibro();

            int resp_submenu = 0;
            while (resp_submenu < 1 || resp_submenu >= Servicio.ejemplarLibroDisponibles.size() ) {
                System.out.println("Cual quiere prestar?");
                resp_submenu = Integer.parseInt(sc.nextLine());
                if (resp_submenu > Servicio.ejemplarLibroDisponibles.size() || resp_submenu < 1) {
                    JOptionPane.showMessageDialog(null, "Por favor escoja un número valido");
                    //System.out.println("Por favor escoja un número valido");
                } else {

                     //Eleccion de las fechas
                    System.out.println("Para que dia lo quiere reservar? (1-30)");
                    int dia_reserva = Integer.parseInt(sc.nextLine());
                    System.out.println("Para que mes lo quiere reservar? (1-12)");
                    int mes_reserva = Integer.parseInt(sc.nextLine());

                    //Manejo de excepcion
                    if (mes_reserva > 12){
                        mes_reserva = 12;
                    }
                    if (dia_reserva > 31){
                        dia_reserva = 31;
                    }

                    LocalDate fecha_reserva = LocalDate.of(2022, mes_reserva, dia_reserva);
                    LocalDate fecha_devolucion = null;

                    int opcion;
                    do {
                        //System.out.println("Cuanto tiempo lo va a reservar?");
                        JOptionPane.showMessageDialog(null, "¿Cuanto tiempo lo va a reservar?");
                        System.out.println("""
                                            1. 7 dias
                                            2. 14 dias
                                            3. Un mes
                                            4. Cancelar""");

                        opcion = Integer.parseInt(sc.nextLine());
                        if (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4){
                            System.out.println("Seleccione una de las opciones");
                        }

                    } while (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4);
                    switch (opcion) {
                        case 1:
                            int dias_devolucion = dia_reserva + 7;
                            if(mes_reserva!=12 && dias_devolucion > 30 ){
                                mes_reserva++;
                                dias_devolucion = dias_devolucion - 30;
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else if (mes_reserva==12 && dias_devolucion < 30 ) {
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            } else{
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                            }
                            break;

                        case 2:
                            dias_devolucion = dia_reserva + 14;
                            if(mes_reserva!=12 && dias_devolucion > 30 ){
                                mes_reserva++;
                                dias_devolucion = dias_devolucion - 30;
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else if (mes_reserva==12 && dias_devolucion < 30 ) {
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            } else{
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                            }
                            break;

                        case 3:
                            if(mes_reserva!=12){
                                fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dia_reserva);
                            }
                            else{
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                            }
                            break;

                        case 4:
                            JOptionPane.showMessageDialog(null, "Usted ha cancelado la operación");
                            //System.out.println("Usted ha cancelado la operación");

                            UiMenu.showMenu();
                            break;
                    }

                    generarReservaLibro(resp_submenu, fecha_reserva, fecha_devolucion);
                    System.out.println("\n");
                    UiMenu.showMenu();
                }
            }
        }
    }

    public static void reservarRevista(){
        Scanner sc = new Scanner(System.in);

        if(UiMenu.getUsuario().isMulta()) {
            JOptionPane.showMessageDialog(null, "Lo sentimos, no puede realizar esta acción porque tiene una multa");
            //System.out.println("Lo sentimos, no puede realizar esta acción porque tiene una multa");
        }else{
            mostrarEjemplaresRevista();
            int resp_submenu = 0;
            while (resp_submenu < 1 || resp_submenu >= Servicio.ejemplarRevistaDisponibles.size() ) {
                System.out.println("");
                System.out.println("¿Cual quiere reservar?");
                resp_submenu = Integer.parseInt(sc.nextLine());
                if (resp_submenu > Servicio.ejemplarRevistaDisponibles.size() || resp_submenu < 1) {
                    System.out.println("Por favor escoja un número valido");
                } else {
                    System.out.println("Para que dia la quiere reservar? (1-30)");
                    int dia_reserva = Integer.parseInt(sc.nextLine());
                    System.out.println("Para que mes la quiere reservar? (1-12)");
                    int mes_reserva = Integer.parseInt(sc.nextLine());
                    if (mes_reserva > 12){
                        mes_reserva = 12;
                    }
                    if (dia_reserva > 31){
                        dia_reserva = 31;
                    }

                    LocalDate fecha_reserva = LocalDate.of(2022, mes_reserva, dia_reserva);
                    LocalDate fecha_devolucion = null;

                    int opcion;
                    do {
                        System.out.println("Cuanto tiempo lo va a reservar?");
                        System.out.println("""
                                            1. 7 dias
                                            2. 14 dias
                                            3. Un mes
                                            4. Cancelar""");

                        opcion = Integer.parseInt(sc.nextLine());
                        if (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4){
                            System.out.println("Seleccione una de las opciones");
                        }

                    } while (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4);
                    switch (opcion) {
                        case 1:
                            int dias_devolucion = dia_reserva + 7;
                            if(mes_reserva!=12 && dias_devolucion > 30 ){
                                mes_reserva++;
                                dias_devolucion = dias_devolucion - 30;
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else if (mes_reserva==12 && dias_devolucion < 30 ) {
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            } else{
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                            }
                            break;

                          /*  if (dias_devolucion > 30) {
                                mes_reserva++;
                                dias_devolucion = dias_devolucion - 30;

                            }
                            fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            break;*/

                        case 2:
                            dias_devolucion = dia_reserva + 14;
                            if(mes_reserva!=12 && dias_devolucion > 30 ){
                                mes_reserva++;
                                dias_devolucion = dias_devolucion - 30;
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else if (mes_reserva==12 && dias_devolucion < 30 ) {
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            } else{
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                            }
                            break;

                        case 3:
                            if(mes_reserva!=12){
                                fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dia_reserva);
                            }
                            else{
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                            }
                            break;

                        case 4:
                            JOptionPane.showMessageDialog(null, "Usted ha cancelado la operación");
                            //System.out.println("Usted ha cancelado la operación");
                            UiMenu.showMenu();
                            break;
                    }

                    generarReservaRevista(resp_submenu, fecha_reserva, fecha_devolucion);
                    System.out.println("\n");
                    UiMenu.showMenu();


                }
            }

        }

    }
    public static void mostrarEjemplaresLibro(){ //Recorre la lista de Ejemplares de Libro
        int i = 0;
        for(EjemplarLibro ejemplar: Servicio.ejemplarLibroDisponibles){
            if(!ejemplar.getEstadoEjemplar().isPrestado() && !ejemplar.getEstadoEjemplar().isReservado()){
                System.out.println((i+1) +". "+ ejemplar.getLibro().getNombre() + ".  Codigo: " +ejemplar.getId());
                i++;
            }
        }

    }

    public static void mostrarEjemplaresRevista(){ //Recorre la lista de Ejemplares de Revista
        int i = 0;
        for(EjemplarRevista ejemplar: Servicio.ejemplarRevistaDisponibles){
            if(!ejemplar.getEstadoEjemplar().isPrestado() && !ejemplar.getEstadoEjemplar().isReservado()){
                System.out.println((i+1) +". "+ ejemplar.getRevista().getNombre() + ".  Codigo: " +ejemplar.getId());
                i++;
            }
        }
    }

    //Esta función lo que hace es añadir la reserva al usuario, generar un tiquete y actualizar el estado del libro que//
    //el usuario reservó. Se le pasan esos parámetros porque son necesarios en el contexto del método//
    public static void generarReservaLibro(int resp_submenu, LocalDate fecha_reserva, LocalDate fecha_devolucion){
        String nombre_libro = Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getLibro().getNombre();
        Reserva reserva = new Reserva(UiMenu.getUsuario(), Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getLibro(),fecha_reserva, fecha_devolucion);
        int id_reserva = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(reserva, id_reserva);
        Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setReserva(reserva);
        Servicio.ejemplarLibroDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setReservado(true);
        UiMenu.getUsuario().getReservas().add(reserva);
        UiMenu.getUsuario().getTiquetes().add(tiquete);

        System.out.println("Se ha realizado con exito su reserva del libro " + nombre_libro +
                ". El id de esta operacion es " + id_reserva + "\n");

    }

    public static void generarReservaRevista(int resp_submenu, LocalDate fecha_reserva, LocalDate fecha_devolucion){
        String nombre_revista = Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getRevista().getNombre();
        Reserva reserva = new Reserva(UiMenu.getUsuario(), Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getRevista(),fecha_reserva, fecha_devolucion);
        int id_reserva = (int) (Math.random() * 10000);
        Tiquete tiquete = new Tiquete(reserva, id_reserva);
        Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setReserva(reserva);
        Servicio.ejemplarRevistaDisponibles.get(resp_submenu - 1).getEstadoEjemplar().setReservado(true);
        UiMenu.getUsuario().getReservas().add(reserva);
        UiMenu.getUsuario().getTiquetes().add(tiquete);

        System.out.println("Se ha realizado con exito su reserva de la revista " + nombre_revista +
                ". El id de esta operacion es " + id_reserva + "\n");

    }

}
