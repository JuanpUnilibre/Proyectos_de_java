package myMain;

import java.util.Scanner;

public class funciones {

    // Saludo inicial
    public static void saludar() {
        System.out.println("Buenos dias! Bienvenida al sistema de inventario de la tienda.");
    }

    // Pedir el nombre del usuario
    public static String pedirNombre(Scanner sc) {
        System.out.print("Por favor, ingrese su nombre: ");
        return sc.nextLine();
    }

    // Preludio con la informacion que necesita el programa
    public static void preludio(String nombre) {
        System.out.println("\nHola, " + nombre + "!");
        System.out.println("Este programa le ayudara a gestionar el inventario diario de:");
        System.out.println("- Empanadas");
        System.out.println("- Fritos");
        System.out.println("- Bebidas:");
        System.out.println("   * Jugos naturales (por jarra, no se cuentan sobras)");
        System.out.println("   * Gaseosas (Kola Roman, Postobon y 7Up)");
        System.out.println("Ademas calculara las ganancias y sueldos de los empleados.");
        System.out.println("-----------------------------------------------------------\n");
    }

    // Preguntar fritos de la noche anterior
    public static int pedirFritosAnoche(Scanner sc) {
        System.out.print("Ingrese cuantos fritos sobraron anoche: ");
        return sc.nextInt();
    }

    // Apartado especial: preguntar gaseosas
    public static int[] pedirGaseosasAnoche(Scanner sc) {
        int[] gaseosas = new int[3]; // [0]=Kola Roman, [1]=Postobon, [2]=7Up

        System.out.println("\nAhora ingrese cuantas gaseosas sobraron anoche:");
        System.out.print("Kola Roman: ");
        gaseosas[0] = sc.nextInt();

        System.out.print("Postobon: ");
        gaseosas[1] = sc.nextInt();

        System.out.print("7Up: ");
        gaseosas[2] = sc.nextInt();

        return gaseosas;
    }

    // Mostrar un pequeño resumen de gaseosas
    public static void mostrarResumenGaseosas(int[] gaseosas, int valorGaseosas) {
        System.out.println("\nResumen de gaseosas sobrantes:");
        System.out.println("- Kola Roman: " + gaseosas[0]);
        System.out.println("- Postobon: " + gaseosas[1]);
        System.out.println("- 7Up: " + gaseosas[2]);
        System.out.println("Valor total gaseosas sobrantes: $" + valorGaseosas);
    }
}


