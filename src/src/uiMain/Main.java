package uiMain;

import gestorAplicacion.libreria.*;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Usuario;

import java.time.LocalDate;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        //Creacion de objetos

        Libro libro_soledad = new Libro("100 anios de soledad", "Gabriel Garcia Marquez", 373512323, "Fantasia");
        Libro libro_noches = new Libro("Las mil y una noches", "Varios autores",391212871, "Cuento");
        Libro guerra_y_paz = new Libro("Guerra y paz", "Leon Tolstoi", 391212291, "Histórica");
        Libro orgullo = new Libro("Orgullo y prejuicio","Jane Austen",391219123,"Novela");
        Libro extranjero = new Libro("Extranjero", "Albert Camus",221212871,"Filosofia");
        Libro esperanzas = new Libro("Grandes esperanzas","Charles Dickens",981212871,"Novela");
        Libro el_hombre = new Libro("El hombre sin atributos","Robert Musil",398712871,"Novela");


        Revista revista_viernes = new Revista("Viernes", "El Universal", 323823999, "Entretenimiento");
        Revista revista_semana = new Revista("Revista Semana", "Semana", 278388654, "Entretenimiento");
        Revista revista_3 = new Revista("Entretenimiento");
        Revista revista_4 = new Revista();
        Revista revista_5 = new Revista("Politica");

        EjemplarLibro EjLibro1 = new EjemplarLibro(29392,new EstadoEjemplar(false,false,false,null,null), libro_soledad);
        EjemplarLibro EjLibro2 = new EjemplarLibro(29299,new EstadoEjemplar(false,false,false,null,null), libro_noches);
        EjemplarLibro EjLibro3 = new EjemplarLibro(21299,new EstadoEjemplar(false,false,false,null,null), libro_noches);
        EjemplarLibro EjLibro4 = new EjemplarLibro(28765,new EstadoEjemplar(false,false,false,null,null), libro_soledad);
        EjemplarLibro EjLibro5 = new EjemplarLibro(20000,new EstadoEjemplar(false,false,false,null,null), guerra_y_paz);
        EjemplarLibro EjLibro6 = new EjemplarLibro(22341,new EstadoEjemplar(false,false,false,null,null), guerra_y_paz);
        EjemplarLibro EjLibro7 = new EjemplarLibro(12381,new EstadoEjemplar(false,false,false,null,null), orgullo);
        EjemplarLibro EjLibro8 = new EjemplarLibro(98231,new EstadoEjemplar(false,false,false,null,null), orgullo);
        EjemplarLibro EjLibro9 = new EjemplarLibro(90000,new EstadoEjemplar(false,false,false,null,null), extranjero);
        EjemplarLibro EjLibro10 = new EjemplarLibro(98231,new EstadoEjemplar(false,false,false,null,null), extranjero);
        EjemplarLibro EjLibro11 = new EjemplarLibro(98231,new EstadoEjemplar(false,false,false,null,null), extranjero);
        EjemplarLibro EjLibro12 = new EjemplarLibro(98231,new EstadoEjemplar(false,false,false,null,null), esperanzas);
        EjemplarLibro EjLibro13 = new EjemplarLibro(98221,new EstadoEjemplar(false,false,false,null,null), esperanzas);
        EjemplarLibro EjLibro14 = new EjemplarLibro(11152,new EstadoEjemplar(false,false,false,null,null), esperanzas);
        EjemplarLibro EjLibro15 = new EjemplarLibro(20191,new EstadoEjemplar(false,false,false,null,null), el_hombre);
        EjemplarLibro EjLibro16 = new EjemplarLibro(29371,new EstadoEjemplar(false,false,false,null,null), el_hombre);

        EjemplarRevista ejRev1 = new EjemplarRevista(23812, new EstadoEjemplar(false,false,false,null,null),revista_4);
        EjemplarRevista ejRev2 = new EjemplarRevista(11111, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev3 = new EjemplarRevista(23411, new EstadoEjemplar(false,false,false,null,null),revista_semana);
        EjemplarRevista ejRev4 = new EjemplarRevista(12313, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev5 = new EjemplarRevista(43561, new EstadoEjemplar(false,false,false,null,null),revista_3);
        EjemplarRevista ejRev6 = new EjemplarRevista(32456, new EstadoEjemplar(false,false,false,null,null),revista_semana);
        EjemplarRevista ejRev7 = new EjemplarRevista(56611, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev8 = new EjemplarRevista(65467, new EstadoEjemplar(false,false,false,null,null),revista_3);
        EjemplarRevista ejRev9 = new EjemplarRevista(51231, new EstadoEjemplar(false,false,false,null,null),revista_semana);
        EjemplarRevista ejRev10 = new EjemplarRevista(54768, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev11 = new EjemplarRevista(25674, new EstadoEjemplar(false,false,false,null,null),revista_4);
        EjemplarRevista ejRev12 = new EjemplarRevista(43677, new EstadoEjemplar(false,false,false,null,null),revista_3);
        EjemplarRevista ejRev13 = new EjemplarRevista(23455, new EstadoEjemplar(false,false,false,null,null),revista_3);
        EjemplarRevista ejRev14 = new EjemplarRevista(19600, new EstadoEjemplar(false,false,false,null,null),revista_4);
        EjemplarRevista ejRev15 = new EjemplarRevista(11133, new EstadoEjemplar(false,false,false,null,null),revista_4);
        EjemplarRevista ejRev16 = new EjemplarRevista(44551, new EstadoEjemplar(false,false,false,null,null),revista_4);
        EjemplarRevista ejRev17 = new EjemplarRevista(23455, new EstadoEjemplar(false,false,false,null,null),revista_5);
        EjemplarRevista ejRev18 = new EjemplarRevista(24354, new EstadoEjemplar(false,false,false,null,null),revista_5);


        Servicio.ejemplarLibroDisponibles.add(EjLibro1);
        Servicio.ejemplarLibroDisponibles.add(EjLibro2);
        Servicio.ejemplarLibroDisponibles.add(EjLibro3);
        Servicio.ejemplarLibroDisponibles.add(EjLibro4);
        Servicio.ejemplarLibroDisponibles.add(EjLibro5);
        Servicio.ejemplarLibroDisponibles.add(EjLibro6);
        Servicio.ejemplarLibroDisponibles.add(EjLibro7);
        Servicio.ejemplarLibroDisponibles.add(EjLibro8);
        Servicio.ejemplarLibroDisponibles.add(EjLibro9);
        Servicio.ejemplarLibroDisponibles.add(EjLibro10);
        Servicio.ejemplarLibroDisponibles.add(EjLibro11);
        Servicio.ejemplarLibroDisponibles.add(EjLibro12);
        Servicio.ejemplarLibroDisponibles.add(EjLibro13);
        Servicio.ejemplarLibroDisponibles.add(EjLibro14);
        Servicio.ejemplarLibroDisponibles.add(EjLibro15);
        Servicio.ejemplarLibroDisponibles.add(EjLibro16);

        Servicio.ejemplarRevistaDisponibles.add(ejRev1);
        Servicio.ejemplarRevistaDisponibles.add(ejRev2);
        Servicio.ejemplarRevistaDisponibles.add(ejRev3);
        Servicio.ejemplarRevistaDisponibles.add(ejRev4);
        Servicio.ejemplarRevistaDisponibles.add(ejRev5);
        Servicio.ejemplarRevistaDisponibles.add(ejRev6);
        Servicio.ejemplarRevistaDisponibles.add(ejRev7);
        Servicio.ejemplarRevistaDisponibles.add(ejRev8);
        Servicio.ejemplarRevistaDisponibles.add(ejRev9);
        Servicio.ejemplarRevistaDisponibles.add(ejRev10);
        Servicio.ejemplarRevistaDisponibles.add(ejRev11);
        Servicio.ejemplarRevistaDisponibles.add(ejRev12);
        Servicio.ejemplarRevistaDisponibles.add(ejRev13);
        Servicio.ejemplarRevistaDisponibles.add(ejRev14);
        Servicio.ejemplarRevistaDisponibles.add(ejRev15);
        Servicio.ejemplarRevistaDisponibles.add(ejRev16);
        Servicio.ejemplarRevistaDisponibles.add(ejRev17);
        Servicio.ejemplarRevistaDisponibles.add(ejRev18);



        UiMenu.showMenu();

    }
}
