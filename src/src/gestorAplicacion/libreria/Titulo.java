package gestorAplicacion.libreria;

public abstract class Titulo {
    private String nombre;
    private String autor;
    private int ISBN;

    public Titulo(String nombre, String autor, int ISBN) {
        this.nombre = nombre;
        this.autor = autor;
        this.ISBN = ISBN;
    }

    public Titulo() {
    }
}