package uiMain;

import gestorAplicacion.libreria.Ejemplar;
import gestorAplicacion.libreria.Libro;
import gestorAplicacion.libreria.Revista;
import gestorAplicacion.libreria.Titulo;
import gestorAplicacion.servicios.Prestamo;
import gestorAplicacion.servicios.Reserva;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Usuario;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;

public class UiMenuBusqueda {
    public static void showMenuBusqueda() {
        System.out.println("");
        System.out.println(":: Consulta");
        System.out.println("Que deseas consultar?");
        //System.out.println("Que deseas consultar?");

        String respuesta = "0";
        do {
            System.out.println("");
            System.out.println("1. Buscar Libro");
            System.out.println("2. Buscar Revista");
            System.out.println("3. Mis Prestamos");
            System.out.println("4. Mis Reservas");
            System.out.println("0. Regresar");


            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    buscarLibro();
                    break;
                case "2":
                    respuesta = "0";
                    buscarRevista();
                    break;
                case "3":
                    respuesta = "0";
                    consultarPrestamos();
                    break;
                case "4":
                    respuesta = "0";
                    consultarReservas();
                    break;
                case "0":
                    UiMenu.showMenu();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");

            }
        } while (!respuesta.equals("0"));
    }

    private static void buscarLibro() {
        System.out.println("");
        System.out.println("::Buscar Libro");
        System.out.println("Que filtro deseas usar?");

        String respuesta = "0";
        String palabraClave;
        ArrayList<Libro> resultadoBusqueda = new ArrayList<>();
        do {
            System.out.println("");
            System.out.println("1. Nombre");
            System.out.println("2. Autor");
            System.out.println("3. Genero");
            System.out.println("0. Regresar");


            Scanner sc = new Scanner(System.in);
             respuesta =  sc.nextLine();
            //respuesta = Integer.valueOf(sc.nextLine());

            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    System.out.println("Escribe el nombre del libro que buscas");
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarLibros("nombre", palabraClave);
                    break;
                case "2":
                    respuesta = "0";
                    System.out.println("Escribe el nombre del Autor del libro que buscas");
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarLibros("autor", palabraClave);
                    break;
                case "3":
                    respuesta = "0";
                    System.out.println("Escribe el genero del libro que buscas");
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarLibros("genero", palabraClave);
                    break;
                case "0":
                    respuesta = "0";
                    showMenuBusqueda();
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        } while (!respuesta.equals("0"));

        if (resultadoBusqueda.size() == 0){
            System.out.println("No se encontraron resultados");
            UiMenu.showMenu();
        }else {
            System.out.println("::Resultado de los libros encontrados");
            System.out.println("");
            for (int i = 0; i < resultadoBusqueda.size(); i++) {
                System.out.println((i+1) + ". " + resultadoBusqueda.get(i));
            }
        }
    }

    private static void buscarRevista(){
        System.out.println("");
        System.out.println("::Buscar Revista");
        System.out.println("Que filtro deseas usar?");

        String respuesta = "0";
        String palabraClave;
        ArrayList<Revista> resultadoBusqueda = new ArrayList<>();
        do {
            System.out.println("");
            System.out.println("1. Nombre");
            System.out.println("2. Autor");
            System.out.println("3. Categoria");
            System.out.println("0. Regresar");


            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    System.out.println("");
                    System.out.println("Escribe el nombre de la revista que buscas");

                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarRevistas("nombre", palabraClave);
                    break;
                case "2":
                    respuesta = "0";
                    System.out.println("");
                    System.out.println("Escribe el nombre del autor de la revista que buscas");
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarRevistas("autor", palabraClave);
                    break;
                case "3":
                    respuesta = "0";
                    System.out.println("");
                    System.out.println("Escribe la categoria de la revista que buscas");
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarRevistas("categoria", palabraClave);
                    break;
                case "0":
                    showMenuBusqueda();
                    break;
                default:
                   System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        } while (!respuesta.equals("0"));


        if (resultadoBusqueda.size() == 0){
            System.out.println("No se encontraron resultados");
        }else{
            System.out.println("::Resultado de las revistas encontradas");
            System.out.println("");
            for (int i = 0; i < resultadoBusqueda.size(); i++) {

                System.out.println((i+1) + ". " + resultadoBusqueda.get(i));
            }
        }
    }

    private static void consultarPrestamos(){
        System.out.println("");
        System.out.println("::Mis Prestamos");
        ArrayList<Prestamo> prestamos = UiMenu.getUsuario().getPrestamos();

        if (prestamos.size() == 0){
            System.out.println("");
            System.out.println("Aun no realizas prestamos");
            showMenuBusqueda();
        } else {
            System.out.println("");
            for (int i = 0; i < prestamos.size(); i++) {
                System.out.println((i+1) + ". " + prestamos.get(i));
            }
            showMenuBusqueda();
        }
    }

    private static void consultarReservas(){
        System.out.println("");
        System.out.println("::Mis Reservas");
        ArrayList<Reserva> reservas = UiMenu.getUsuario().getReservas();

        if (reservas.size() == 0){
            System.out.println("Aun no realizas reservas");
            showMenuBusqueda();
        } else {
            for (int i = 0; i < reservas.size(); i++) {
                System.out.println((i+1) + ". " + reservas.get(i));
            }
            showMenuBusqueda();
        }
    }

    /**
     * Esta funcion se encarga de filtrar los libros creados de la clase libros según el filtro pasado como parametro
     * @param filtro
     * @param palabra
     * @return
     */
    private static ArrayList<Libro> filtrarLibros(String filtro, String palabra) {
        ArrayList<Libro> resultadosBusqueda = new ArrayList<>();
        palabra = palabra.toLowerCase();

        switch (filtro) {
            case "nombre":
                for (Libro libro:Libro.getLibros()) {
                    if (libro.getNombre().toLowerCase().contains(palabra)){resultadosBusqueda.add(libro);}
                }
                break;
            case "autor":
                for (Libro libro:Libro.getLibros()) {
                    if (libro.getAutor().toLowerCase().contains(palabra)){resultadosBusqueda.add(libro);}
                }
                break;
            case "genero":
                for (Libro libro:Libro.getLibros()) {
                    if (libro.getGenero().toLowerCase().contains(palabra)){resultadosBusqueda.add(libro);}
                }
                break;
        }

        return resultadosBusqueda;
    }

    private static ArrayList<Revista> filtrarRevistas(String filtro, String palabra){
        ArrayList<Revista> resultadosBusqueda = new ArrayList<>();
        palabra = palabra.toLowerCase();

        switch (filtro) {
            case "nombre":
                for (Revista revista:Revista.getRevistas()) {
                    if (revista.getNombre().toLowerCase().contains(palabra)){resultadosBusqueda.add(revista);}
                }
                break;
            case "autor":
                for (Revista revista:Revista.getRevistas()) {
                    if (revista.getAutor().toLowerCase().contains(palabra)){resultadosBusqueda.add(revista);}
                }
                break;
            case "categoria":
                for (Revista revista:Revista.getRevistas()) {
                    if (revista.getCategoria().toLowerCase().contains(palabra)){resultadosBusqueda.add(revista);}
                }
                break;
        }

        return resultadosBusqueda;
    }
}