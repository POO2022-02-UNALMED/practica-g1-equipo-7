package uiMain;

import gestorAplicacion.servicios.Reserva;

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
                JOptionPane.showMessageDialog(null, "Aun no realizas reservas");
                //System.out.println("Aun no realizas reservas");
                System.out.println("\n\n");
                UiMenu.showMenu();
                break;
            }

           // System.out.println("Selecciona la reserva que deseas cancelar");
            JOptionPane.showMessageDialog(null, "Selecciona la reserva que deseas cancelar");
            System.out.println("\n\n");
            //Ciclo para recorrer la lista de prestamos y mostrar las opciones para reservar
            for (int i = 0; i < reservas.size(); i++) {
                System.out.println((i+1) + ". Nombre: " + reservas.get(i).getTituloEscogido().getNombre() + " Fecha de reserva: " + reservas.get(i).getFechaReserva() + " Fecha de devolucion: " + reservas.get(i).getFechaDevolucion());
            }
            System.out.println("0. Regresar");
            System.out.println("\n\n");

            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            if (respuesta<0 || respuesta>reservas.size()){
                JOptionPane.showMessageDialog(null, "Por favor selecciona una de las opciones indicadas");
                //System.out.println("Por favor selecciona una de las opciones indicadas");

                continue;
            } else if(respuesta==0){
                UiMenu.showMenu();
                break;
            }else {
                //Logica de devolcuion, el -1 es por el indice inicial en 0
                cancelarReserva((respuesta-1));
                respuesta = 0;
            }
        }while(respuesta!=0);
    }

    private static void cancelarReserva(int indiceCancelarReserva){

    }
}
