package myMain;

public class operaciones {
    // Constantes
    public static final int PRECIO_POR_FRITO = 2500;
    public static final int PRECIO_POR_GASEOSA = 3000;
    public static final int SUELDO_FLACA = 40000;
    public static final int SUELDO_USUARIO = 40000;

    // Calcular el valor de las sobras de fritos
    public static int calcularValorFritos(int cantidad) {
        return cantidad * PRECIO_POR_FRITO;
    }

    // Calcular el valor de todas las gaseosas (Kola Roman, Postobon, 7Up)
    public static int calcularValorGaseosas(int[] gaseosas) {
        int totalCantidad = gaseosas[0] + gaseosas[1] + gaseosas[2];
        return totalCantidad * PRECIO_POR_GASEOSA;
    }
}
