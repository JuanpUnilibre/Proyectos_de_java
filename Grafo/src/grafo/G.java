package grafo;

import java.util.LinkedList;
import java.util.Queue;


public class G {
    int [] [] adja;
    boolean [] visited;
    
    public G(int [] [] adja){
        this.adja = adja;
        this.visited = new boolean[adja.length];
    }
    
    public void dfs(int v){
        System.out.println(v + ", ");
        visited[v] = true;

        for(int  i=0;i<visited.length; i++){
            if(adja[v][i] == 1 && !visited[i]){
                dfs(i);
            }
        }      
    }
    
    public void bfs(int v){
        visited = new boolean[visited.length];
        Queue<Integer> q = new LinkedList<>();
        q.add(v);
        visited[v] = true;

        while(!q.isEmpty()){
            v = q.remove();
            System.out.print("" + ", ");
            for(int i=0; i<visited.length;i++){
                if(adja[v][i] == 1 && !visited[i]){
                    q.add(i);
                    visited[i] = true;                   
                }
            }
        }
    }
}
