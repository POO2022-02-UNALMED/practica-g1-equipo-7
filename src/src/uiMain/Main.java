package uiMain;

import gestorAplicacion.libreria.*;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Usuario;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        //Creacion de objetos

        Libro libro_soledad = new Libro("100 años de Soledad", "Gabriel García Marquez", 373512323, "Comedia");
        Libro libro_noches = new Libro("Las mil y una noches", "Varios autores",391212871, "Cuento");

        Revista revista_viernes = new Revista("Viernes", "El Universal", 323823999, "Entretenimiento");
        Revista revista_semana = new Revista("Revista Semana", "Semana", 278388654, "Entretenimiento");

        EjemplarLibro EjLibro1 = new EjemplarLibro(29392,new EstadoEjemplar(false,false,false,null,null), libro_soledad);
        EjemplarLibro EjLibro2 = new EjemplarLibro(29299,new EstadoEjemplar(false,false,false,null,null), libro_soledad);
        EjemplarLibro EjLibro3 = new EjemplarLibro(21299,new EstadoEjemplar(false,false,false,null,null), libro_soledad);
        EjemplarLibro EjLibro4 = new EjemplarLibro(28765,new EstadoEjemplar(false,false,false,null,null), libro_soledad);
        EjemplarLibro EjLibro5 = new EjemplarLibro(20000,new EstadoEjemplar(false,false,false,null,null), libro_noches);
        EjemplarLibro EjLibro6 = new EjemplarLibro(22341,new EstadoEjemplar(false,false,false,null,null), libro_noches);
        EjemplarLibro EjLibro7 = new EjemplarLibro(12381,new EstadoEjemplar(false,false,false,null,null), libro_noches);
        EjemplarLibro EjLibro8 = new EjemplarLibro(98231,new EstadoEjemplar(false,false,false,null,null), libro_noches);

        EjemplarRevista ejRev1 = new EjemplarRevista(76544, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev2 = new EjemplarRevista(23281, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev3 = new EjemplarRevista(29834, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev4 = new EjemplarRevista(84369, new EstadoEjemplar(false,false,false,null,null),revista_viernes);
        EjemplarRevista ejRev5 = new EjemplarRevista(49085, new EstadoEjemplar(false,false,false,null,null),revista_semana);
        EjemplarRevista ejRev6 = new EjemplarRevista(35921, new EstadoEjemplar(false,false,false,null,null),revista_semana);
        EjemplarRevista ejRev7 = new EjemplarRevista(23811, new EstadoEjemplar(false,false,false,null,null),revista_semana);
        EjemplarRevista ejRev8 = new EjemplarRevista(29399, new EstadoEjemplar(false,false,false,null,null),revista_semana);

        Usuario usuario1 = new Usuario("Juan",208103);
        Servicio.ejemplarLibroDisponibles.add(EjLibro1);
        Servicio.ejemplarLibroDisponibles.add(EjLibro2);
        Servicio.ejemplarLibroDisponibles.add(EjLibro3);
        Servicio.ejemplarLibroDisponibles.add(EjLibro4);
        Servicio.ejemplarLibroDisponibles.add(EjLibro5);
        Servicio.ejemplarLibroDisponibles.add(EjLibro6);
        Servicio.ejemplarLibroDisponibles.add(EjLibro7);
        Servicio.ejemplarLibroDisponibles.add(EjLibro8);

        Servicio.ejemplarRevistaDisponibles.add(ejRev1);
        Servicio.ejemplarRevistaDisponibles.add(ejRev2);
        Servicio.ejemplarRevistaDisponibles.add(ejRev3);
        Servicio.ejemplarRevistaDisponibles.add(ejRev4);
        Servicio.ejemplarRevistaDisponibles.add(ejRev5);
        Servicio.ejemplarRevistaDisponibles.add(ejRev6);
        Servicio.ejemplarRevistaDisponibles.add(ejRev7);
        Servicio.ejemplarRevistaDisponibles.add(ejRev8);

    }
}
