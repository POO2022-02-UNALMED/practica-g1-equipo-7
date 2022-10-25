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

            //Se almacena la respuesta del usuario
            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            switch (respuesta){
                case "1":
                    respuesta = "0";
                    Servicio.filtrarLibrosDisponibles(UiMenu.getBiblioteca()); //Filtra los libros disponibles (los que no se encuentran ya prestados o reservados)
                    reservarLibro(); //Abre el menu para reservar un libro 
                    break;
                case "2":
                    respuesta = "0";
                    Servicio.filtrarRevistasDisponibles(UiMenu.getBiblioteca()); //Filtra las revistas disponibles (las que no se encuentran ya prestadas o reservadas)
                    reservarRevista(); //Abre el menu para reservar una revista
                    break;
                case "0":
                    UiMenu.showMenu(); //Regresa al menu principal
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        }while (!respuesta.equals("0"));
    }

    public static void reservarLibro(){
        Scanner sc = new Scanner(System.in);

        if(UiMenu.getUsuario().isMulta()) { //Evalua si el usuario tiene una multa vigente
            System.out.println("Lo sentimos, no puede realizar esta accion porque tiene una multa");
        }else{

            mostrarEjemplaresLibro(); //Muestra los Libros disponibles
            System.out.println("0. Regresar");

            int resp_submenu = 0;
            do {
                System.out.println("");
                System.out.println("Cual quiere prestar?");
                resp_submenu = Integer.parseInt(sc.nextLine());

                if (resp_submenu > Servicio.getEjemplarLibroDisponibles().size() || resp_submenu < 0) { //Evalua que la respuesta del usuario este dentro del rango valido
                    System.out.println("Por favor escoja un número valido");

                } else if (resp_submenu == 0) {
                    showMenuReserva(); //Regresa al menu inicial de para realizar una reserva

                } else {
                    //Eleccion de las fechas
                    System.out.println("Para que dia lo quiere reservar? (1-30)");
                    int dia_reserva = Integer.parseInt(sc.nextLine());
                    System.out.println("Para que mes lo quiere reservar? (1-12)");
                    int mes_reserva = Integer.parseInt(sc.nextLine());

                    //Manejo de excepción
                    if (mes_reserva > 12){
                        mes_reserva = 12;
                    }
                    if (dia_reserva > 31){
                        dia_reserva = 31;
                    }

                    LocalDate fecha_reserva = LocalDate.of(2022, mes_reserva, dia_reserva); //Almacena el mes y el día que proporciono el usuario para hacer la reserva (Se toma el año vigente, en este caso '2022')
                    LocalDate fecha_devolucion = null;

                    int opcion;
                    do {
                        System.out.println("Cuanto tiempo lo va a reservar?");
                        System.out.println("""
                                            1. 7 dias
                                            2. 14 dias
                                            3. Un mes
                                            4. Cancelar""");

                        opcion = Integer.parseInt(sc.nextLine()); //Almacena la respuesta del usuario

                        if (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4){ //Evalua que la respuesta este dentro de un rango valido
                            System.out.println("Seleccione una de las opciones");
                        }

                    } while (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4);
                    switch (opcion) {
                        case 1:
                            int dias_devolucion = dia_reserva + 7;
                            if(mes_reserva==2) { //Condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { // Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion); //Almacena la fecha de devolución
                                }
                                else { 
                                    if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                        mes_reserva++; 
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución 
                                }
                            }

                            else if(mes_reserva < 12) {
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución 
                            }
                            else  { //Condicion para cuando el mes sea el '12' el año de la fecha de devolución se pase al año siguiente (tomando como año inicial el que aparece en 'fecha_reserva' y considerando que 'dias_devolución' es mayor a 31)
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva); //Almacena la fecha de devolución
                                }
                                else {
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                                }
                            }break;
                        case 2:
                            dias_devolucion = dia_reserva + 14;
                            if(mes_reserva==2) { //Condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { // Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion); //Almacena la fecha de devolución
                                }
                                else {
                                    if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                        mes_reserva++;
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                                }
                            }

                            else if(mes_reserva < 12) { 
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolucíon
                            }
                            else  { //Condicion para cuando el mes sea el '12' el año de la fecha de devolución se pase al año siguiente (tomando como año inicial el que aparece en 'fecha_reserva' y considerando que 'dias_devolución' es mayor a 31)
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva); //Almacena la fecha de devolución
                                }
                                else {
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                                }
                            }break;
                        case 3:
                            if(mes_reserva!=12){
                                fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dia_reserva); //Almacena la fecha de devolución
                            }
                            else{ //Al ser el mes el numero '12' se debe pasar al año siguiente y establecer el mes como el '1' para no tener incoherencias con el calendario
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva); //Almacena la fecha de devolución
                            }
                            break;
                        case 4:
                            System.out.println("Usted ha cancelado la operacion");
                            UiMenu.showMenu(); //Regresa al menu principal
                            break;
                    }
                    EjemplarLibro ejemplarLibro= Servicio.getEjemplarLibroDisponibles().get(resp_submenu - 1); //Se quita el libro seleccionado por el usuario de la lista de libros disponibles
                    Reserva.generarReservaLibro(UiMenu.getUsuario(), ejemplarLibro, UiMenu.getBiblioteca(), fecha_reserva, fecha_devolucion);
                    System.out.println("Se ha realizado con exito su reserva del libro " + ejemplarLibro.getLibro().getNombre());
                    System.out.println("\n");

                    UiMenu.showMenu(); //Regresa al menu principal
                    //Control para termiar el ciclo
                    resp_submenu = 0;
                }

            }while (resp_submenu!=0);
        }
    }

    public static void reservarRevista(){
        Scanner sc = new Scanner(System.in);

        if(UiMenu.getUsuario().isMulta()) { //Evalua si el usuario tiene una multa vigente
            System.out.println("Lo sentimos, no puede realizar esta accion porque tiene una multa");
        }else{
            mostrarEjemplaresRevista(); //Muestra las revistas disponibles
            System.out.println("0. Regresar");
            int resp_submenu = 0;
            do {
                System.out.println("");
                System.out.println("Cual quiere reservar?");
                resp_submenu = Integer.parseInt(sc.nextLine());

                if (resp_submenu > Servicio.getEjemplarRevistaDisponibles().size() || resp_submenu < 0) { //Evalua que la respuesta del usuario este dentro del rango valido
                    System.out.println("Por favor escoja un número valido");

                } else if (resp_submenu == 0) {
                    showMenuReserva(); //Regresa al menu inicial de para realizar una reserva

                } else {
                     //Eleccion de las fechas
                    System.out.println("Para que dia la quiere reservar? (1-30)");
                    int dia_reserva = Integer.parseInt(sc.nextLine());
                    System.out.println("Para que mes la quiere reservar? (1-12)");
                    int mes_reserva = Integer.parseInt(sc.nextLine());
                   
                    //Manejo de excepción
                    if (mes_reserva > 12){
                        mes_reserva = 12;
                    }
                    if (dia_reserva > 31){
                        dia_reserva = 31;
                    }

                    LocalDate fecha_reserva = LocalDate.of(2022, mes_reserva, dia_reserva); //Almacena el mes y el día que proporciono el usuario para hacer la reserva (Se toma el año vigente, en este caso '2022')
                    LocalDate fecha_devolucion = null;

                    int opcion;
                    do {
                        System.out.println("Cuanto tiempo lo va a reservar?");
                        System.out.println("""
                                            1. 7 dias
                                            2. 14 dias
                                            3. Un mes
                                            4. Cancelar""");

                        opcion = Integer.parseInt(sc.nextLine()); //Almacena la respuesta del usuario

                        if (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4){
                            System.out.println("Seleccione una de las opciones");
                        }

                    } while (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4);
                    switch (opcion) {
                        case 1:
                            int dias_devolucion = dia_reserva + 7;
                            if(mes_reserva==2) { //Condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { // Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion); //Almacena la fecha de devolución
                                }
                                else {
                                    if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                        mes_reserva++;
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                                }
                            }

                            else if(mes_reserva < 12) {
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                            }
                            else  { //Condicion para cuando el mes sea el '12' el año de la fecha de devolución se pase al año siguiente (tomando como año inicial el que aparece en 'fecha_reserva' y considerando que 'dias_devolución' es mayor a 31)
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva); //Almacena la fecha de devolución
                                }
                                else {
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                                }
                            }break;
                        case 2:
                            dias_devolucion = dia_reserva + 14;
                            if(mes_reserva==2) { //Condiciones especial para algunos meses del año
                                if (dias_devolucion == 29 || dias_devolucion == 30) { //Mes 2 (febrero), hacemos que la reserva quede para el mes siguiente
                                    dias_devolucion = 1;
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dias_devolucion); //Almacena la fecha de devolución
                                }
                                else {
                                     if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                        mes_reserva++;
                                        dias_devolucion = dias_devolucion - 30;};

                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                                }
                            }

                            else if(mes_reserva < 12) {
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva++;
                                    dias_devolucion = dias_devolucion - 30;
                                }
                                fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                            }
                            else  {
                                if (dias_devolucion > 31) { //Condicion para cuando 'dias_devolucion' sea mayor a '31' y se deba pasar al proximo mes, esto para poder almacenar la fecha de devolución de manera correcta y no tener incoherencias con el calendario
                                    mes_reserva = 1;
                                    dias_devolucion = dias_devolucion - 30;
                                    fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva); //Almacena la fecha de devolución
                                }
                                else { //Condicion para cuando el mes sea el '12' el año de la fecha de devolución se pase al año siguiente (tomando como año inicial el que aparece en 'fecha_reserva' y considerando que 'dias_devolución' es mayor a 31)
                                    fecha_devolucion = LocalDate.of(2022, mes_reserva, dias_devolucion); //Almacena la fecha de devolución
                                } 
                            }break;
                        case 3:
                            if(mes_reserva!=12){
                                fecha_devolucion = LocalDate.of(2022, mes_reserva + 1, dia_reserva); //Almacena la fecha de devolución
                            }
                            else{ //Al ser el mes el numero '12' se debe pasar al año siguiente y establecer el mes como el '1' para no tener incoherencias con el calendario
                                mes_reserva=1;
                                fecha_devolucion = LocalDate.of(2023, mes_reserva, dia_reserva); //Almacena la fecha de devolución
                            }
                            break;
                        case 4:
                            System.out.println("Usted ha cancelado la operación");
                            UiMenu.showMenu(); //Regresa al menu inicial
                            break;
                    }
                    EjemplarRevista ejemplarRevista = Servicio.getEjemplarRevistaDisponibles().get(resp_submenu - 1); //Se quita la revista seleccionada por el usuario de la lista de revistas disponibles
                    Reserva.generarReservaRevista(UiMenu.getUsuario(), ejemplarRevista, UiMenu.getBiblioteca(), fecha_reserva, fecha_devolucion);
                    System.out.println("Se ha realizado con exito su reserva de la revista " + ejemplarRevista.getRevista().getNombre() +
                            ". El id de esta operacion es " + ejemplarRevista.getEstadoEjemplar().getReserva().getTiquete().getId());
                    System.out.println("\n");

                    UiMenu.showMenu(); //Regresa al menu principal
                    resp_submenu = 0;
                    //Control para termiar el ciclo
                }
            }while (resp_submenu!=0);

        }

    }

    public static void mostrarEjemplaresLibro(){ //Recorre la lista de Ejemplares de Libro y se imprime cada uno con su respectivo nombre y codigo (Id)
        int i = 0;
        for(EjemplarLibro ejemplar: Servicio.getEjemplarLibroDisponibles()){
            System.out.println((i+1) +". "+ ejemplar.getLibro().getNombre() + ".  Codigo: " +ejemplar.getId());
            i++;
        }

    }

    public static void mostrarEjemplaresRevista(){ //Recorre la lista de Ejemplares de Revista y se imprime cada una con su respectivo nombre y codigo (Id)
        int i = 0;
        for(EjemplarRevista ejemplar: Servicio.getEjemplarRevistaDisponibles()){
            System.out.println((i+1) +". "+ ejemplar.getRevista().getNombre() + ".  Codigo: " +ejemplar.getId());
            i++;
        }
    }
}
