package grafo;

public class Grafo {
    public static void main(String[] args) {
        int [][] m = {
            {0,1,1,0,0,0,0,0}, //0
            {1,0,0,1,1,0,0,0}, //1
            {1,0,0,1,0,0,1,0}, //2
            {0,1,0,0,0,1,0,0}, //3
            {0,0,1,0,0,0,0,1}, //4
            {0,1,1,0,0,1,1,0}, //5
            
            
        };
        G g = new G(m);
        System.out.println("DFS: ");
        g.dfs(3);
        System.out.println("\nBFS: ");
        g.bfs(3);
    }
}
