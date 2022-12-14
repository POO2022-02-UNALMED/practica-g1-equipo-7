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

            //Se guarda la respuesta del usuario
            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            /**
             * En los dos primeros casos del 'switch' la respuesta se hace 0 para evitar que después que se ejecute 
               el metodo del caso correspondiente se termine el programa, y en vez de eso, hacer que el ciclo vueva 
               a ejecutarse (en el caso 0 especificamente) y devuelva al usuario al menu principal
             */
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

    /**
     * Esta funcionalidad muestra los libros que se le recomiendan al usuario de acuerdo a su genero favorito
     * @param biblioteca Biblioteca que contendra los libros para aplicar el filtro
     * @param usuario Usuario al cual se le van a recomendar los libros
     */
    public static void recomendacionLibro(Biblioteca biblioteca, Usuario usuario){
        System.out.println("Estos son los libros que encontramos para ti: ");
        System.out.println("");

        usuario.encontrarGeneroFavorito(); //Metodo almacenado en la clase 'Usuario'
        ArrayList<Libro> librosMasSolicitados= Libro.masSolicitados(biblioteca, usuario.getGeneroFavorito()); //Lista almacenada en la clase 'Libro'

        for (int i = 0; i < 2; i++) { //Se recorre la lista 'librosMasSolicitados' y se va imprimiendo cada libro contenido en esta; con su respectivo nombre, autor y genero
            System.out.println("");
            System.out.println((i+1) + ". Libro: " + librosMasSolicitados.get(i).getNombre() + " Autor: " +
                    librosMasSolicitados.get(i).getAutor() + " Genero: " + librosMasSolicitados.get(i).getGenero());
        }

        UiMenu.showMenu(); //Regresa al menu principal
    }

    public static void recomendacionRevista(Biblioteca biblioteca, Usuario usuario){
        System.out.println("Estos son las revistas que encontramos para ti: ");
        System.out.println("");

        usuario.encontrarCategoriaFavorita(); //Metodo almacenado en la clase 'Usuario'
        ArrayList<Revista> revistasMasSolicitadas= Revista.masSolicitadas(biblioteca, usuario.getCategoriaFavorita());

        System.out.println(revistasMasSolicitadas.size());
        for (int i = 0; i < 2; i++) { //Se recorre la lista 'revistasMasSolicitadas' y se va imprimiendo cada resvista contenida en esta; con su respectivo nombre, autor y categoria
            System.out.println("");
            System.out.println((i+1) + ". Revista: " + revistasMasSolicitadas.get(i).getNombre() + " Autor: " +
                    revistasMasSolicitadas.get(i).getAutor() + " Categoria: " + revistasMasSolicitadas.get(i).getCategoria());
        }

        UiMenu.showMenu(); ////Regresa al menu principal
    }
}
