package uiMain;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int opcion;
        do {
            System.out.println("---- Bienvenido a JJ School -----");
            System.out.println("¿Qué desea hacer hoy?");
            System.out.println("1. Ver top 3 mejores estudiantes");
            System.out.println("2. Consultar la materia en la que peor van los estudiantes");
            System.out.println("3. Revisar el estado de alguno de los bloques");
            System.out.println("4. Verificar gastos e ingresos");
            System.out.println("5. Recibir un informe sobre un determinado grupo");
            System.out.println("6. Salir");
            opcion = entrada.nextInt();

            /*switch (opcion) {
                case 1:


            }*/
        }while(opcion != 6);

    }
}
