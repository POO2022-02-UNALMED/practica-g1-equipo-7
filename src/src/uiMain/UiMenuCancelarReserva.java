package uiMain;

import gestorAplicacion.libreria.Biblioteca;
import gestorAplicacion.servicios.Reserva;
import gestorAplicacion.servicios.Tiquete;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Se crea la variable 'respuesta' que va a ser la encargada de almacenar posteriormente la respuesta que 
   el usuario digite por pantalla y tambien se llama la lista de las reservas realizas previamente por 
   este mismo (almacenada en la clase 'Reserva')
 */
public class UiMenuCancelarReserva {
    public static void showMenuCancelarReserva(){
        System.out.println(":: Cancelar Reserva");
        System.out.println("");
        int respuesta = 0;
        ArrayList<Reserva> reservas= UiMenu.getUsuario().getReservas();
        do {
        
            //Se evalua que el tamaño de la lista 'reservas' sea igual a '0' para confirmar que el usuario no ha realizado ninguna reserva
            if(reservas.size() == 0){
                System.out.println("");
                System.out.println("Aun no realizas reservas");
                System.out.println("");
                UiMenu.showMenu(); 
                break;
            }

            System.out.println("Selecciona la reserva que deseas cancelar");
            System.out.println("");

            //Ciclo para recorrer la lista de prestamos y mostrar las opciones para reservar
            for (int i = 0; i < reservas.size(); i++) {
                System.out.println((i+1) + ". Nombre: " + reservas.get(i).getTituloEscogido().getNombre() + " Fecha de reserva: " +
                        reservas.get(i).getFechaReserva() + " Fecha de devolucion: " + reservas.get(i).getFechaDevolucion());
            }
            System.out.println("0. Regresar");

            //Como se menciono antes, acá se almacenara la respuesta que digito por pantalla del usuario 
            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            //Se evalua que la respuesta del usuario esté dentro de límites de las opciones que puede escoger
            if (respuesta<0 || respuesta>reservas.size()){
                System.out.println("Por favor selecciona una de las opciones indicadas");

                continue;

            } else if(respuesta==0){
                UiMenu.showMenu();
                break;

            }else {
                /**
                 * Logica de devolución, el -1 es por el indice inicial en 0
                 * Se llama al metodo 'cancelarReserva' de la clase 'Reserva'
                 */
                Reserva.cancelarReserva((respuesta-1), UiMenu.getBiblioteca(), UiMenu.getUsuario());
                System.out.println("Se ha cancelado satisfactoriamebte la reserva");

                UiMenu.showMenu();
                respuesta = 0;
            }
        }while(respuesta!=0);
    }
}
