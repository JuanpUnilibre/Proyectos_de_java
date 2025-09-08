package bst;

public class ArbolBinario {
    Nodo raiz;
    
    /*
    public ArbolBinario() {
        raiz = new Nodo (20);
        
        raiz.izq = new Nodo(15);
        raiz.izq.izq = new Nodo (40);
        
        raiz.der = new Nodo(30);
        raiz.der.der = new Nodo(8);
    }
    */

    public void add( int dato ){
        raiz = add(raiz, dato);
    }

    private Nodo add( Nodo n, int dato ) {
        if( n == null ){
            n = new Nodo(dato);
        }
        else if( dato < n.dato ){
            n.izq = add(n.izq , dato);
                }
        else if( dato > n.dato ){
            n.der = add(n.der , dato);
                }
        return n;
    }
    
    public void inorden (){
        inorden(raiz);
    }
    
    private void inorden(Nodo n){
        if (n != null){
            inorden(n.izq);
            System.out.print(n.dato + ", ");
            inorden(n.der);
        }
    }
    
    public int altura(){
        return altura(raiz);
    }
    
    private int altura(Nodo n){
        if ( n == null ) return 0;
        else return Math.max(altura(n.izq), altura(n.der)) + 1 ;
    }
    
    public void ancestros(int dato){
        ancestros (raiz, dato);
    }
    
    private boolean ancestros( Nodo n, int dato){
        if( n==null ) return false;
        if( n.dato == dato ) return true;
        if( ancestros(n.izq, dato) || ancestros(n.der, dato) ){
            System.out.print( n.dato + ", " );
            return true;
        }
        return false;
    }
    
    public void brother(int dato) {
        Nodo b = brother(raiz, dato);
        if (b == null) System.out.println("El nodo " + dato + " no tiene hermano");
        else System.out.println("El hermano del Nodo " + dato + " es el " + b.dato);
    }
    
    private Nodo brother(Nodo n, int dato){
        if (n == null) return null;
        if (n.izq != null && n.izq.dato == dato) return n.der;
        if (n.der != null && n.der.dato == dato) return n.izq;
        
        Nodo n2 = brother(n.izq, dato);
        if( n2 != null ) return n2;
        return brother(n.der, dato);
    }
}
