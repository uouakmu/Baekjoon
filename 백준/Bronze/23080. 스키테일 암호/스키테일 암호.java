import java.util.Scanner;
 
public class Main {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);
        
        int k = sc.nextInt();
        char[] s = sc.next().toCharArray();
        
        for (int i = 0; i < s.length; i++) {
            if (i % k == 0) {
                System.out.print(s[i]);
            }
        }
 
    }
}