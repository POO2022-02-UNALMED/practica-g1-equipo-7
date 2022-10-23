package uiMain;

import gestorAplicacion.libreria.Biblioteca;
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

        String respuesta="0";
        do {
            System.out.println("");
            System.out.println("1. Reservar Libro");
            System.out.println("2. Reservar Revista");
            System.out.println("0. Regresar");

            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            switch (respuesta){
                case "1":
                    respuesta = "0";
                    Servicio.filtrarLibrosDisponibles(UiMenu.getBiblioteca());
                    reservarLibro();
                    break;
                case "2":
                    respuesta = "0";
                    Servicio.filtrarRevistasDisponibles(UiMenu.getBiblioteca());
                    reservarRevista();
                    break;
                case "0":
                    UiMenu.showMenu();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while (!respuesta.equals("0"));
    }

    public static void reservarLibro(){
        Scanner sc = new Scanner(System.in);

        if(UiMenu.getUsuario().isMulta()) {
            System.out.println("Lo sentimos, no puede realizar esta accion porque tiene una multa");
        }else{

            mostrarEjemplaresLibro();
            System.out.println("0. Regresar");

            int resp_submenu = 0;
            do {
                System.out.println("");
                System.out.println("Cual quiere prestar?");
                resp_submenu = Integer.parseInt(sc.nextLine());
                if (resp_submenu > Servicio.getEjemplarLibroDisponibles().size() || resp_submenu < 0) {
                    System.out.println("Por favor escoja un número valido");
                } else if (resp_submenu == 0) {
                    showMenuReserva();
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
                            if(mes_reserva==2) { // condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { // Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion);
                                }
                                else {
                                    if (dias_devolucion > 31) {
                                        mes_reserva++;
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }

                            else if(mes_reserva < 12) {
                                if (dias_devolucion > 31) {
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else  {
                                if (dias_devolucion > 31) {
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                                }
                                else {
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }break;
                        case 2:
                            dias_devolucion = dia_reserva + 14;
                            if(mes_reserva==2) { // condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { // Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion);
                                }
                                else {
                                    if (dias_devolucion > 31) {
                                        mes_reserva++;
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }

                            else if(mes_reserva < 12) {
                                if (dias_devolucion > 31) {
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else  {
                                if (dias_devolucion > 31) {
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                                }
                                else {
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }break;
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
                            System.out.println("Usted ha cancelado la operacion");
                            UiMenu.showMenu();
                            break;
                    }
                    EjemplarLibro ejemplarLibro= Servicio.getEjemplarLibroDisponibles().get(resp_submenu - 1);
                    Reserva.generarReservaLibro(UiMenu.getUsuario(), ejemplarLibro, UiMenu.getBiblioteca(), fecha_reserva, fecha_devolucion);
                    System.out.println("Se ha realizado con exito su reserva del libro " + ejemplarLibro.getLibro().getNombre());
                    System.out.println("\n");

                    UiMenu.showMenu();
                    //Control para termiar el ciclo
                    resp_submenu = 0;
                }

            }while (resp_submenu!=0);
        }
    }

    public static void reservarRevista(){
        Scanner sc = new Scanner(System.in);

        if(UiMenu.getUsuario().isMulta()) {
            System.out.println("Lo sentimos, no puede realizar esta accion porque tiene una multa");
        }else{
            mostrarEjemplaresRevista();
            System.out.println("0. Regresar");
            int resp_submenu = 0;
            do {
                System.out.println("");
                System.out.println("Cual quiere reservar?");
                resp_submenu = Integer.parseInt(sc.nextLine());
                if (resp_submenu > Servicio.getEjemplarRevistaDisponibles().size() || resp_submenu < 0) {
                    System.out.println("Por favor escoja un número valido");
                } else if (resp_submenu == 0) {
                    showMenuReserva();
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
                            if(mes_reserva==2) { // condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { // Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion);
                                }
                                else {
                                    if (dias_devolucion > 31) {
                                        mes_reserva++;
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }

                            else if(mes_reserva < 12) {
                                if (dias_devolucion > 31) {
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else  {
                                if (dias_devolucion > 31) {
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                                }
                                else {
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }break;
                        case 2:
                            dias_devolucion = dia_reserva + 14;
                            if(mes_reserva==2) { // condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { // Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion);
                                }
                                else {
                                     if (dias_devolucion > 31) {
                                        mes_reserva++;
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }

                            else if(mes_reserva < 12) {
                                if (dias_devolucion > 31) {
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                            }
                            else  {
                                if (dias_devolucion > 31) {
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva);
                                }
                                else {
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion);
                                }
                            }break;
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
                            System.out.println("Usted ha cancelado la operación");
                            UiMenu.showMenu();
                            break;
                    }
                    EjemplarRevista ejemplarRevista = Servicio.getEjemplarRevistaDisponibles().get(resp_submenu - 1);
                    Reserva.generarReservaRevista(UiMenu.getUsuario(), ejemplarRevista, UiMenu.getBiblioteca(), fecha_reserva, fecha_devolucion);
                    System.out.println("Se ha realizado con exito su reserva de la revista " + ejemplarRevista.getRevista().getNombre() +
                            ". El id de esta operacion es " + ejemplarRevista.getEstadoEjemplar().getReserva().getTiquete().getId());
                    System.out.println("\n");

                    UiMenu.showMenu();
                    resp_submenu = 0;

                }
            }while (resp_submenu!=0);

        }

    }

    public static void mostrarEjemplaresLibro(){ //Recorre la lista de Ejemplares de Libro
        int i = 0;
        for(EjemplarLibro ejemplar: Servicio.getEjemplarLibroDisponibles()){
            System.out.println((i+1) +". "+ ejemplar.getLibro().getNombre() + ".  Codigo: " +ejemplar.getId());
            i++;
        }

    }

    public static void mostrarEjemplaresRevista(){ //Recorre la lista de Ejemplares de Revista
        int i = 0;
        for(EjemplarRevista ejemplar: Servicio.getEjemplarRevistaDisponibles()){
            System.out.println((i+1) +". "+ ejemplar.getRevista().getNombre() + ".  Codigo: " +ejemplar.getId());
            i++;
        }
    }
}
