package bst;

public class BST {

    public static void main(String[] args) {
        ArbolBinario a = new ArbolBinario();
        
        
        a.add(6);
        a.add(4);
        a.add(8);
        a.add(1);
        a.add(5);
        a.add(9);
        
        a.inorden();
        
        /*
        System.out.print("Los ancestros son ");
        a.ancestros(17);
        */ 
        
        
        /*
        a.inorden();
        System.out.println("");
        System.out.println("La altura del arbol es " + a.altura());   
        */
    }
}
