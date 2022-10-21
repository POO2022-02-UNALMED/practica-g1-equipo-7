package uiMain;

import gestorAplicacion.servicios.Reserva;
import gestorAplicacion.servicios.Tiquete;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Scanner;

public class UiMenuCancelarReserva {
    public static void showMenuCancelarReserva(){
        System.out.println(":: Cancelar Reserva");

        int respuesta = 0;
        ArrayList<Reserva> reservas= UiMenu.getUsuario().getReservas();
        do {

            if(reservas.size() == 0){
                System.out.println("\n\n");
                System.out.println("Aun no realizas reservas");
                System.out.println("\n\n");
                UiMenu.showMenu();
                break;
            }

            System.out.println("Selecciona la reserva que deseas cancelar");

            //Ciclo para recorrer la lista de prestamos y mostrar las opciones para reservar
            for (int i = 0; i < reservas.size(); i++) {
                System.out.println((i+1) + ". Nombre: " + reservas.get(i).getTituloEscogido().getNombre() + " Fecha de reserva: " +
                        reservas.get(i).getFechaReserva() + " Fecha de devolucion: " + reservas.get(i).getFechaDevolucion());
            }
            System.out.println("0. Regresar");
            System.out.println("");

            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            if (respuesta<0 || respuesta>reservas.size()){
                System.out.println("Por favor selecciona una de las opciones indicadas");

                continue;
            } else if(respuesta==0){
                UiMenu.showMenu();
                break;
            }else {
                //Logica de devolcuion, el -1 es por el indice inicial en 0
                cancelarReserva((respuesta-1));
                System.out.println("Se ha cancelado satisfactoriamebte la reserva");
                UiMenu.showMenu();
                respuesta = 0;
            }
        }while(respuesta!=0);
    }

    private static void cancelarReserva(int indiceCancelarReserva){
        Tiquete tiqueteVacio = null;
        Reserva reservaAEliminar = UiMenu.getUsuario().getReservas().get(indiceCancelarReserva);
        for (Tiquete tiquete: UiMenu.getUsuario().getTiquetes()){
            if (tiquete.getServicio().equals(reservaAEliminar)){
                tiqueteVacio = tiquete;
            }
        }
        UiMenu.getUsuario().getReservas().remove(reservaAEliminar);
        UiMenu.getUsuario().getTiquetes().remove(tiqueteVacio);
    }
}
