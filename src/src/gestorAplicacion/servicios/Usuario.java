package gestorAplicacion.servicios;

import gestorAplicacion.libreria.CATEGORIA;
import gestorAplicacion.libreria.GENERO;
import gestorAplicacion.libreria.Libro;
import gestorAplicacion.libreria.Revista;

import java.io.Serializable;
import java.util.*;

public class Usuario implements Serializable {
    private String nombre;
    private int id;
    private ArrayList<Prestamo> prestamos = new ArrayList<>();
    private ArrayList<Reserva> reservas = new ArrayList<>();
    private ArrayList<Tiquete> tiquetes = new ArrayList<>();
    private ArrayList<Libro> historialLibrosUsados = new ArrayList<>();
    private ArrayList<Revista> historialRevistasUsadas = new ArrayList<>();
    private boolean multa = false;
    private GENERO generoFavorito;
    private CATEGORIA categoriaFavorita;

    //constructor

    public Usuario(String nombre, int id) {
        this.nombre = nombre;
        this.id = id;
    }

    //getters y setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public ArrayList<Prestamo> getPrestamos() {
        return prestamos;
    }

    public void setPrestamos(ArrayList<Prestamo> prestamos) {
        this.prestamos = prestamos;
    }

    public ArrayList<Reserva> getReservas() {
        return reservas;
    }

    public void setReservas(ArrayList<Reserva> reservas) {
        this.reservas = reservas;
    }

    public ArrayList<Tiquete> getTiquetes() {
        return tiquetes;
    }

    public void setTiquetes(ArrayList<Tiquete> tiquetes) {
        this.tiquetes = tiquetes;
    }

    public boolean isMulta() {
        return multa;
    }

    public void setMulta(boolean multa) {
        this.multa = multa;
    }

    public GENERO getGeneroFavorito() {
        return generoFavorito;
    }

    public void setGeneroFavorito(GENERO generoFavorito) {
        this.generoFavorito = generoFavorito;
    }

    public ArrayList<Libro> getHistorialLibrosUsados() {
        return historialLibrosUsados;
    }

    public void setHistorialLibrosUsados(ArrayList<Libro> historialLibrosUsados) {
        this.historialLibrosUsados = historialLibrosUsados;
    }

    public ArrayList<Revista> getHistorialRevistasUsadas() {
        return historialRevistasUsadas;
    }

    public void setHistorialRevistasUsadas(ArrayList<Revista> historialRevistasUsadas) {
        this.historialRevistasUsadas = historialRevistasUsadas;
    }

    public CATEGORIA getCategoriaFavorita() {
        return categoriaFavorita;
    }

    public void setCategoriaFavorita(CATEGORIA categoriaFavorita) {
        this.categoriaFavorita = categoriaFavorita;
    }

    //metodos

    /**
     *
     */
    public void encontrarGeneroFavorito(){
        // hashmap para guardar la frecuencia de lectura de genero
        Map<GENERO, Integer> generosLeidos = new HashMap<GENERO, Integer>();
        GENERO generoFavorito = null;
        int maxLeido = 0;

        for (Libro libro : historialLibrosUsados) {
            Integer j = generosLeidos.get(libro.getGenero());
            generosLeidos.put(libro.getGenero(), (j == null) ? 1 : j + 1);
        }


        //se busca el genero favorito con el hashMap
        for (GENERO genero: generosLeidos.keySet()) {
            if(generosLeidos.get(genero)>maxLeido){
                generoFavorito = genero;
                maxLeido = generosLeidos.get(genero);
            }
        }
        setGeneroFavorito(generoFavorito);

    }

    public void encontrarCategoriaFavorita(){
        // hashmap para guardar la frecuencia de lectura de genero
        Map<CATEGORIA, Integer> categoriasLeidas = new HashMap<CATEGORIA, Integer>();
        CATEGORIA categoriaFavorita = null;
        int maxLeido = 0;

        for (Revista revista : historialRevistasUsadas) {
            Integer j = categoriasLeidas.get(revista.getCategoria());
            categoriasLeidas.put(revista.getCategoria(), (j == null) ? 1 : j + 1);
        }



        //se busca el genero favorito con el hashMap
        for (CATEGORIA categoria: categoriasLeidas.keySet()) {
            if(categoriasLeidas.get(categoria)>maxLeido){
                categoriaFavorita = categoria;
                maxLeido = categoriasLeidas.get(categoria);
            }
        }
        setCategoriaFavorita(categoriaFavorita);

    }
}
