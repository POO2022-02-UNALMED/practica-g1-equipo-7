package uiMain;

import gestorAplicacion.libreria.*;
import gestorAplicacion.servicios.Servicio;
import gestorAplicacion.servicios.Usuario;

public class Inicializador {

    //Creacion de objetos

    Libro libro_soledad = new Libro("100 anios de soledad", "Gabriel Garcia Marquez", 373512323, GENERO.FANTASIA);
    Libro libro_noches = new Libro("Las mil y una noches", "Varios autores", 391212871, GENERO.CUENTO);
    Libro guerra_y_paz = new Libro("Guerra y paz", "Leon Tolstoi", 391212291, GENERO.HISTORICA);
    Libro orgullo = new Libro("Orgullo y prejuicio", "Jane Austen", 391219123, GENERO.NOVELA);
    Libro extranjero = new Libro("Extranjero", "Albert Camus", 221212871, GENERO.FILOSOFIA);
    Libro esperanzas = new Libro("Grandes esperanzas", "Charles Dickens", 981212871, GENERO.NOVELA);
    Libro el_hombre = new Libro("El hombre sin atributos", "Robert Musil", 398712871, GENERO.NOVELA);


    Revista revista_viernes = new Revista("Viernes", "El Universal", 323823999, CATEGORIA.ENTRETENIMIENTO);
    Revista revista_semana = new Revista("Revista Semana", "Semana", 278388654, CATEGORIA.ENTRETENIMIENTO);
    Revista revista_3 = new Revista(CATEGORIA.ENTRETENIMIENTO);
    Revista revista_4 = new Revista();
    Revista revista_5 = new Revista(CATEGORIA.POLITICA);


    EjemplarLibro EjLibro1 = new EjemplarLibro(29392, new EstadoEjemplar(false, false, false, null, null), libro_soledad);
    EjemplarLibro EjLibro2 = new EjemplarLibro(29299, new EstadoEjemplar(false, false, false, null, null), libro_noches);
    EjemplarLibro EjLibro3 = new EjemplarLibro(21299, new EstadoEjemplar(false, false, false, null, null), libro_noches);
    EjemplarLibro EjLibro4 = new EjemplarLibro(28765, new EstadoEjemplar(false, false, false, null, null), libro_soledad);
    EjemplarLibro EjLibro5 = new EjemplarLibro(20000, new EstadoEjemplar(false, false, false, null, null), guerra_y_paz);
    EjemplarLibro EjLibro6 = new EjemplarLibro(22341, new EstadoEjemplar(false, false, false, null, null), guerra_y_paz);
    EjemplarLibro EjLibro7 = new EjemplarLibro(12381, new EstadoEjemplar(false, false, false, null, null), orgullo);
    EjemplarLibro EjLibro8 = new EjemplarLibro(98231, new EstadoEjemplar(false, false, false, null, null), orgullo);
    EjemplarLibro EjLibro9 = new EjemplarLibro(90000, new EstadoEjemplar(false, false, false, null, null), extranjero);
    EjemplarLibro EjLibro10 = new EjemplarLibro(98231, new EstadoEjemplar(false, false, false, null, null), extranjero);
    EjemplarLibro EjLibro11 = new EjemplarLibro(98231, new EstadoEjemplar(false, false, false, null, null), extranjero);
    EjemplarLibro EjLibro12 = new EjemplarLibro(98231, new EstadoEjemplar(false, false, false, null, null), esperanzas);
    EjemplarLibro EjLibro13 = new EjemplarLibro(98221, new EstadoEjemplar(false, false, false, null, null), esperanzas);
    EjemplarLibro EjLibro14 = new EjemplarLibro(11152, new EstadoEjemplar(false, false, false, null, null), esperanzas);
    EjemplarLibro EjLibro15 = new EjemplarLibro(20191, new EstadoEjemplar(false, false, false, null, null), el_hombre);
    EjemplarLibro EjLibro16 = new EjemplarLibro(29371, new EstadoEjemplar(false, false, false, null, null), el_hombre);

    EjemplarRevista ejRev1 = new EjemplarRevista(23812, new EstadoEjemplar(false, false, false, null, null), revista_4);
    EjemplarRevista ejRev2 = new EjemplarRevista(11111, new EstadoEjemplar(false, false, false, null, null), revista_viernes);
    EjemplarRevista ejRev3 = new EjemplarRevista(23411, new EstadoEjemplar(false, false, false, null, null), revista_semana);
    EjemplarRevista ejRev4 = new EjemplarRevista(12313, new EstadoEjemplar(false, false, false, null, null), revista_viernes);
    EjemplarRevista ejRev5 = new EjemplarRevista(43561, new EstadoEjemplar(false, false, false, null, null), revista_3);
    EjemplarRevista ejRev6 = new EjemplarRevista(32456, new EstadoEjemplar(false, false, false, null, null), revista_semana);
    EjemplarRevista ejRev7 = new EjemplarRevista(56611, new EstadoEjemplar(false, false, false, null, null), revista_viernes);
    EjemplarRevista ejRev8 = new EjemplarRevista(65467, new EstadoEjemplar(false, false, false, null, null), revista_3);
    EjemplarRevista ejRev9 = new EjemplarRevista(51231, new EstadoEjemplar(false, false, false, null, null), revista_semana);
    EjemplarRevista ejRev10 = new EjemplarRevista(54768, new EstadoEjemplar(false, false, false, null, null), revista_viernes);
    EjemplarRevista ejRev11 = new EjemplarRevista(25674, new EstadoEjemplar(false, false, false, null, null), revista_4);
    EjemplarRevista ejRev12 = new EjemplarRevista(43677, new EstadoEjemplar(false, false, false, null, null), revista_3);
    EjemplarRevista ejRev13 = new EjemplarRevista(23455, new EstadoEjemplar(false, false, false, null, null), revista_3);
    EjemplarRevista ejRev14 = new EjemplarRevista(19600, new EstadoEjemplar(false, false, false, null, null), revista_4);
    EjemplarRevista ejRev15 = new EjemplarRevista(11133, new EstadoEjemplar(false, false, false, null, null), revista_4);
    EjemplarRevista ejRev16 = new EjemplarRevista(44551, new EstadoEjemplar(false, false, false, null, null), revista_4);
    EjemplarRevista ejRev17 = new EjemplarRevista(23455, new EstadoEjemplar(false, false, false, null, null), revista_5);
    EjemplarRevista ejRev18 = new EjemplarRevista(24354, new EstadoEjemplar(false, false, false, null, null), revista_5);

    public void inicializar() {
        UiMenu.getBiblioteca().a??adirLibro(libro_soledad);
        UiMenu.getBiblioteca().a??adirLibro(libro_noches);
        UiMenu.getBiblioteca().a??adirLibro(guerra_y_paz);
        UiMenu.getBiblioteca().a??adirLibro(orgullo);
        UiMenu.getBiblioteca().a??adirLibro(extranjero);
        UiMenu.getBiblioteca().a??adirLibro(el_hombre);

        UiMenu.getBiblioteca().a??adirRevista(revista_viernes);
        UiMenu.getBiblioteca().a??adirRevista(revista_semana);
        UiMenu.getBiblioteca().a??adirRevista(revista_3);
        UiMenu.getBiblioteca().a??adirRevista(revista_4);
        UiMenu.getBiblioteca().a??adirRevista(revista_5);

        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro1);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro2);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro3);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro4);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro5);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro6);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro7);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro8);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro9);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro10);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro11);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro12);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro13);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro14);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro15);
        UiMenu.getBiblioteca().a??adirEjemplarLibro(EjLibro16);

        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev1);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev2);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev3);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev4);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev5);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev6);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev7);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev8);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev9);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev10);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev11);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev12);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev13);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev14);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev15);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev16);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev17);
        UiMenu.getBiblioteca().a??adirEjemplarRevista(ejRev18);

    }
}
