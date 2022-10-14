package uiMain;

import gestorAplicacion.libreria.Titulo;
import gestorAplicacion.servicios.Prestamo;
import gestorAplicacion.servicios.Usuario;

import java.util.ArrayList;
import java.util.Scanner;

public class UiMenuDevoluciones {
    public static void showMenuDevoluciones(){
        System.out.println(":: Devoluciones");


        int respuesta = 0;
        ArrayList<Prestamo> prestamos = UiMenu.getUsuario().getPrestamos();
        do {

            if(prestamos.size() == 0){
                System.out.println("\n\n");
                System.out.println("Aun no realizas prestamos");
                System.out.println("\n\n");
                UiMenu.showMenu();
                break;
            }

            System.out.println("Selecciona el titulo que deseas devolver");
            //Ciclo para recorrer la lista de prestamos y mostrar las opciones para devolver
            System.out.println("\n\n");
            for (int i = 0; i < prestamos.size(); i++) {
                System.out.println((i+1) + ". Nombre: " + prestamos.get(i).getTituloEscogido().getNombre() + " Autor: " + prestamos.get(i).getTituloEscogido().getAutor());
            }
            System.out.println("0. Regresar");
            System.out.println("\n\n");

            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            if (respuesta<0 || respuesta>prestamos.size()){
                System.out.println("Por favor selecciona una de las opciones indicadas");
                continue;
            } else if(respuesta==0){
                UiMenu.showMenu();
                break;
            }else {
                //Logica de devolcuion, el -1 es por el indice inicial en 0
                devolucion((respuesta-1));
                respuesta = 0;
            }
        }while (respuesta!=0);
    }

    private static void devolucion(int indiceTituloDevolucion){

    }
}
