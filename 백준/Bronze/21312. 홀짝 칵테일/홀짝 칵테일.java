import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[3];
        boolean odd =false;
        int value = 1;
        int value2 = 1;
        
        for(int i=0; i<3; i++){
            arr[i] = sc.nextInt();
            if(arr[i]%2==1){
                value *= arr[i];
                odd=true;
            } else {
                value2 *= arr[i];
            }
        }
        if(odd){
            System.out.println(value);
        } else {
            System.out.println(value2);
        }
    }
}