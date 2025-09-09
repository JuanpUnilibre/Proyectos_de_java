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
    
    //Gaseosa
    public static int calcularValorGaseosa(int cantidad_gaseosa){
        return cantidad_gaseosa;
    }

    // (Podemos añadir luego precios de gaseosas si toca calcular)
}
