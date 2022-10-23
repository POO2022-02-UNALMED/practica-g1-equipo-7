package baseDatos;

import gestorAplicacion.libreria.Biblioteca;

import java.io.*;

public class Serializador {
    private static File rutaTemp = new File("src\\src\\baseDatos\\temp");

    /**
     * Metodo para serialzar las listas que están en la clase Biblioteca
     */
    public static void serializar(Biblioteca biblioteca) {
        FileOutputStream fos;
        ObjectOutputStream oos;
        File[] docs = rutaTemp.listFiles();
        PrintWriter pw;

        //Con el for se borra el contenido de los archivos para evitar futuros problemas
        for (File file : docs) {
            try {
                //al pasarle como parametro al pw, la ruta del archivo, borra el contenido
                pw = new PrintWriter(file);
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        //Se escribe lo que debe ir en cada archivo segun lo que contiene biblioteca
        for (File file : docs) {
            if (file.getAbsolutePath().contains("ejemplaresLibros")) {
                try {
                    fos = new FileOutputStream(file);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(biblioteca.getEjemplaresLibros());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("ejemplaresRevistas")) {
                try {
                    fos = new FileOutputStream(file);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(biblioteca.getEjemplaresRevistas());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("libros")) {
                try {
                    fos = new FileOutputStream(file);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(biblioteca.getLibros());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("revistas")) {
                try {
                    fos = new FileOutputStream(file);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(biblioteca.getRevistas());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("usuarios")) {
                try {
                    fos = new FileOutputStream(file);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(biblioteca.getUsuarios());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("historialLibrosUsados")) {
                try {
                    fos = new FileOutputStream(file);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(biblioteca.getHistorialLibrosUsados());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            } else if (file.getAbsolutePath().contains("historialRevistasUsadas")) {
                try {
                    fos = new FileOutputStream(file);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(biblioteca.getHistorialRevistasUsadas());
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}