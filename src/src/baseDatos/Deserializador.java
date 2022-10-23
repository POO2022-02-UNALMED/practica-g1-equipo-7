package baseDatos;

import gestorAplicacion.libreria.*;
import gestorAplicacion.servicios.Usuario;

import java.io.*;
import java.util.ArrayList;

public class Deserializador {
    private static File rutaTemp = new File("src\\src\\baseDatos\\temp");

    /**
     * Carga las listas de objetos que hay almacenados
     */
    public static void deserializar(Biblioteca biblioteca){
        File[] docs = rutaTemp.listFiles();
        FileInputStream fis;
        ObjectInputStream ois;

        for (File file : docs) {
            if (file.getAbsolutePath().contains("ejemplaresLibros")){
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    biblioteca.setEjemplaresLibros((ArrayList<EjemplarLibro>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("ejemplaresRevistas")) {
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    biblioteca.setEjemplaresRevistas((ArrayList<EjemplarRevista>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("libros")) {
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    biblioteca.setLibros((ArrayList<Libro>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("revistas")) {
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    biblioteca.setRevistas((ArrayList<Revista>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("usuarios")) {
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    biblioteca.setUsuarios((ArrayList<Usuario>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("historialLibrosUsados")) {
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    biblioteca.setHistorialLibrosUsados((ArrayList<Libro>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("historialRevistasUsadas")) {
                try {
                    fis = new FileInputStream(file);
                    ois = new ObjectInputStream(fis);
                    biblioteca.setHistorialRevistasUsadas((ArrayList<Revista>) ois.readObject());
                } catch (FileNotFoundException e){
                    e.printStackTrace();
                } catch (IOException e){
                    e.printStackTrace();
                } catch (ClassNotFoundException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
