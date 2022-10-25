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

            //Se almacena la respuesta del usuario
            Scanner sc = new Scanner(System.in);
            respuesta = sc.nextLine();

            /**
             * El condicional multiple recibe la respuesta del usuario y en los cuatro primeros casos se le 
               da el valor de '0' a la variable 'respuesta' para que se ejecute nuevamente el ciclo en el
               caso '0', lo cual hace que después de hacer la busqueda pertinente el programa no finalice 
               y se abra nuevamente el menu inicial  
             */
            switch (respuesta) {
                case "1":
                    respuesta = "0";
                    buscarLibro(); //Se abre el menu para buscar un libro
                    showMenuBusqueda(); 
                    break;
                case "2":
                    respuesta = "0";
                    buscarRevista(); //Se abre el menu para buscar una revista
                    showMenuBusqueda(); 
                    break;
                case "3":
                    respuesta = "0";
                    consultarPrestamos(); //Se abre el menu para consultar un prestamo
                    showMenuBusqueda(); 
                    break;
                case "4":
                    respuesta = "0";
                    consultarReservas(); //Se abre el menu para consultar una reserva
                    showMenuBusqueda(); 
                    break;
                case "0":
                    UiMenu.showMenu(); //Se abre el menu general de busquedas
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

            /**
             * El condicional multiple recibe la respuesta del usuario y realiza la busqueda de acuerdo al
               filtro que este selcciono (los cuales son 'Nombre', 'Autor' y 'Genero' respectivamente) y la
               y la palabra clave que digito por pantalla. Después de esto se crea una lista llamada 
               'resultadoBusqueda' con los resultados encontrados
             */
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
                    showMenuBusqueda(); //Abre el menu inicial
                    break;
                default:
                    System.out.println("Por favor selecciona una de las opciones indicadas");
            }
        } while (!respuesta.equals("0"));

        /**
         * Se evalua que el tamaño de la lista 'resultadoBusqueda' sea igual a '0' para verificar que no se 
           encontraron resultados con el filtro y la palabra clave correspondientes
         */
        if (resultadoBusqueda.size() == 0){
            System.out.println("No se encontraron resultados");
            UiMenu.showMenu();
        }else {
            System.out.println("::Resultado de los libros encontrados"); 
            System.out.println("");
            for (int i = 0; i < resultadoBusqueda.size(); i++) { //Se recorre la lista y se van imprimiendo cada uno de los resultados de la busqueda
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

            /**
             * El condicional multiple recibe la respuesta del usuario y realiza la busqueda de acuerdo al
               filtro que este selcciono (los cuales son 'Nombre', 'Autor' y 'Categoria' respectivamente) y la
               y la palabra clave que digito por pantalla. Después de esto se crea una lista llamada 
               'resultadoBusqueda' con los resultados encontrados
             */
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

        /**
         * Se evalua que el tamaño de la lista 'resultadoBusqueda' sea igual a '0' para verificar que no se 
           encontraron resultados con el filtro y la palabra clave correspondientes
         */
        if (resultadoBusqueda.size() == 0){
            System.out.println("No se encontraron resultados");
        }else{
            System.out.println("::Resultado de las revistas encontradas");
            System.out.println("");
            for (int i = 0; i < resultadoBusqueda.size(); i++) { //Se recorre la lista y se van imprimiendo cada uno de los resultados de la busqueda
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
            for (int i = 0; i < prestamos.size(); i++) { //Se recorre la lista 'prestamos' (almacenada en la clase 'Prestamo') y se van imprimiendo cada uno de los elementos que conforman a esta
                System.out.println((i+1) + ". " + prestamos.get(i));
            }
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
            for (int i = 0; i < reservas.size(); i++) { //Se recorre la lista 'reservas' (almacenada en la clase 'Reserva') y se van imprimiendo cada uno de los elementos que conforman a esta
                System.out.println((i+1) + ". " + reservas.get(i));
            }
        }
    }




}