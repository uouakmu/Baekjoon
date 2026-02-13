import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=0; i< n; i++){
            int m = sc.nextInt();
           if( m >= 300){
               System.out.print("1 ");
           }else if( m >= 275 && m < 300){
               System.out.print("2 ");
           }else if( m >=250 && m <275){
               System.out.print("3 ");
           }else if( m <250){
               System.out.print("4 ");
           }
        }
        sc.close();
    }
}