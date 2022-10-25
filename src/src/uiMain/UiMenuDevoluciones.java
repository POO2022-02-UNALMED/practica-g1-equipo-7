package uiMain;

import gestorAplicacion.libreria.Biblioteca;
import gestorAplicacion.libreria.Titulo;
import gestorAplicacion.servicios.Prestamo;
import gestorAplicacion.servicios.Tiquete;
import gestorAplicacion.servicios.Usuario;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Se crea la variable 'respuesta' que va a ser la encargada de almacenar posteriormente la respuesta que 
   el usuario digite por pantalla y tambien se llama la lista de los prestamos realizos previamente por 
   este mismo (almacenada en la clase 'Prestamo')
 */
public class UiMenuDevoluciones {
    public static void showMenuDevoluciones(){
        System.out.println(":: Devoluciones");
        int respuesta = 0;
        ArrayList<Prestamo> prestamos = UiMenu.getUsuario().getPrestamos();
        do {

            //Se evalua que el tamaño de la lista 'prestamos' sea igual a '0' para confirmar que el usuario no ha realizado ningún prestamo
            if(prestamos.size() == 0){
                System.out.println("Aun no realizas prestamos");
                UiMenu.showMenu();
                break;
            }
            System.out.println("Selecciona el titulo que deseas devolver");

            //Ciclo para recorrer la lista de prestamos y mostrar las opciones para devolver
            System.out.println("");
            for (int i = 0; i < prestamos.size(); i++) {
                System.out.println((i+1) + ". Nombre: " + prestamos.get(i).getTituloEscogido().getNombre() + " Autor: " + prestamos.get(i).getTituloEscogido().getAutor());
            }
            System.out.println("0. Regresar");

            //Como se menciono antes, acá se almacenara la respuesta que digito por pantalla del usuario
            Scanner sc = new Scanner(System.in);
            respuesta = Integer.valueOf(sc.nextLine());

            //Se evalua que la respuesta del usuario esté dentro de límites de las opciones que puede escoger
            if (respuesta<0 || respuesta>prestamos.size()){
                System.out.println("Por favor selecciona una de las opciones indicadas");

                continue;

            } else if(respuesta==0){
                UiMenu.showMenu();
                break;

            }else {
                /**
                 * Logica de devolución, el -1 es por el indice inicial en 0
                 * Se llama al metodo 'devolucion' de la clase 'Prestamo'
                 */
                Prestamo.devolucion((respuesta-1), UiMenu.getBiblioteca(), UiMenu.getUsuario());
                System.out.println("Devolucion realizada satisfactoriamente");
                UiMenu.showMenu();
                respuesta = 0;
            }
        }while (respuesta!=0);
    }
}
