package uiMain;

import gestorAplicacion.libreria.*;
import gestorAplicacion.servicios.Prestamo;
import gestorAplicacion.servicios.Reserva;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Usuario;
import static gestorAplicacion.libreria.Libro.filtrarLibros;
import static gestorAplicacion.libreria.Revista.filtrarRevistas;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;



public class UiMenuBusqueda {
    public static void showMenuBusqueda() {
        System.out.println("");
        System.out.println(":: Consulta");
        System.out.println("");
        System.out.println("Que deseas consultar?");

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
                    showMenuBusqueda();
                    break;
                case "2":
                    respuesta = "0";
                    buscarRevista();
                    showMenuBusqueda();
                    break;
                case "3":
                    respuesta = "0";
                    consultarPrestamos();
                    showMenuBusqueda();
                    break;
                case "4":
                    respuesta = "0";
                    consultarReservas();
                    showMenuBusqueda();
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
        System.out.println("");
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
                    resultadoBusqueda = filtrarLibros("nombre", palabraClave, UiMenu.getBiblioteca());
                    break;
                case "2":
                    respuesta = "0";
                    System.out.println("Escribe el nombre del Autor del libro que buscas");
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarLibros("autor", palabraClave, UiMenu.getBiblioteca());
                    break;
                case "3":
                    respuesta = "0";
                    System.out.println("");
                    System.out.println("Selecciona el genero del libro que buscas");

                    //Se recorre el Enum para mostrar las opciones
                    int indice = 1;
                    for (GENERO genero: GENERO.values()) {
                        System.out.println(indice + ". " + genero);
                        indice++;
                    }
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarLibros("genero", palabraClave,UiMenu.getBiblioteca());

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
        System.out.println("");
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
                    resultadoBusqueda = filtrarRevistas("nombre", palabraClave, UiMenu.getBiblioteca());
                    break;
                case "2":
                    respuesta = "0";
                    System.out.println("");
                    System.out.println("Escribe el nombre del autor de la revista que buscas");
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarRevistas("autor", palabraClave, UiMenu.getBiblioteca());
                    break;
                case "3":
                    respuesta = "0";
                    System.out.println("");
                    System.out.println("Selecciona la categoria de la revista que buscas");

                    //Se recorre el Enum para mostrar las opciones
                    int indice = 1;
                    for (CATEGORIA categoria: CATEGORIA.values()) {
                        System.out.println(indice + ". " + categoria);
                        indice++;
                    }
                    palabraClave = String.valueOf(sc.nextLine());
                    resultadoBusqueda = filtrarRevistas("categoria", palabraClave, UiMenu.getBiblioteca());

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
        ArrayList<Prestamo> prestamos = UiMenu.getBiblioteca().getUsuario().getPrestamos();

        if (prestamos.size() == 0){
            System.out.println("");
            System.out.println("Aun no realizas prestamos");
            showMenuBusqueda();
        } else {
            System.out.println("");
            for (int i = 0; i < prestamos.size(); i++) {
                System.out.println((i+1) + ". " + prestamos.get(i));
            }
        }
    }

    private static void consultarReservas(){
        System.out.println("");
        System.out.println("::Mis Reservas");
        ArrayList<Reserva> reservas = UiMenu.getBiblioteca().getUsuario().getReservas();

        if (reservas.size() == 0){
            System.out.println("Aun no realizas reservas");
            showMenuBusqueda();
        } else {
            for (int i = 0; i < reservas.size(); i++) {
                System.out.println((i+1) + ". " + reservas.get(i));
            }
        }
    }




}