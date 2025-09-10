package myMain;

import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Saludo
        funciones.saludar();

        // 2. Nombre
        String nombreUsuario = funciones.pedirNombre(sc);

        // 3. Preludio
        funciones.preludio(nombreUsuario);

        // 4. Fritos sobrantes
        int fritosAnoche = funciones.pedirFritosAnoche(sc);
        int valorSobras = operaciones.calcularValorFritos(fritosAnoche);
        System.out.println("El valor de las sobras de fritos es: $" + valorSobras);

        // 5. Gaseosas sobrantes
        int[] gaseosas = funciones.pedirGaseosasAnoche(sc);
        int valorGaseosas = operaciones.calcularValorGaseosas(gaseosas);
        funciones.mostrarResumenGaseosas(gaseosas, valorGaseosas);

        sc.close();
    }
}

