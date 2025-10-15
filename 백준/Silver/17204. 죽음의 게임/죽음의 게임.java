import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int K = sc.nextInt();
        
        int[] students = new int[N];
        
        for(int i=0; i<N; i++) {
            students[i] = sc.nextInt();
        }
        
        boolean[] visited = new boolean[N];
        int current = 0;
        int steps = 0;
        
        while (!visited[current]) {
            if(current == K) {
                System.out.println(steps);
                return;
            }
            visited[current] = true;
            current = students[current];
            steps++;
        }
        System.out.println(-1);
    }
}