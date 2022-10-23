package uiMain;

import gestorAplicacion.libreria.Biblioteca;
import gestorAplicacion.libreria.GENERO;
import gestorAplicacion.libreria.Libro;
import gestorAplicacion.libreria.Revista;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Usuario;

import java.util.ArrayList;
import java.util.Scanner;

public class UiMenuRecomendar {
    public static void showMenuRecomendar() {
        System.out.println(":: Recomendaciones");

        String respuesta = "0";
        do {
            System.out.println("");
            System.out.println("1. Recomendar Libro");
            System.out.println("2. Recomendar Revista");
            System.out.println("0. Regresar");


            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    recomendacionLibro(UiMenu.getBiblioteca(), UiMenu.getUsuario());
                    break;
                case "2":
                    respuesta = "0";
                    recomendacionRevista(UiMenu.getBiblioteca(), UiMenu.getUsuario());
                    break;
                case "0":
                    UiMenu.showMenu();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        } while (!respuesta.equals("0"));
    }

    public static void recomendacionLibro(Biblioteca biblioteca, Usuario usuario){
        System.out.println("Estos son los libros que encontramos para ti: ");
        System.out.println("");

        usuario.encontrarGeneroFavorito();
        ArrayList<Libro> librosMasSolicitados= Libro.masSolicitados(biblioteca, usuario.getGeneroFavorito());

        for (int i = 0; i < 3; i++) {
            System.out.println("");
            System.out.println((i+1) + ". Libro: " + librosMasSolicitados.get(i).getNombre() + " Autor: " +
                    librosMasSolicitados.get(i).getAutor() + " Genero: " + librosMasSolicitados.get(i).getGenero());
        }

        UiMenu.showMenu();
    }

    public static void recomendacionRevista(Biblioteca biblioteca, Usuario usuario){
        System.out.println("Estos son las revistas que encontramos para ti: ");
        System.out.println("");

        usuario.encontrarCategoriaFavorita();
        ArrayList<Revista> revistasMasSolicitadas= Revista.masSolicitadas(biblioteca, usuario.getCategoriaFavorita());

        System.out.println(revistasMasSolicitadas.size());
        for (int i = 0; i < 3; i++) {
            System.out.println("");

            System.out.println((i+1) + ". Revista: " + revistasMasSolicitadas.get(i).getNombre() + " Autor: " +
                    revistasMasSolicitadas.get(i).getAutor() + " Categoria: " + revistasMasSolicitadas.get(i).getCategoria());
        }

        UiMenu.showMenu();
    }
}
