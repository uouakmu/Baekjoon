import java.util.*;
public class Main {
    static int num(int sum,int k){
        int room=sum%k;
        int c=0;
        if(room==0) c=sum/k;
        else c=(sum/k)+1;
        return c;
    }
    public static void main(String args[]) {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt(), k=s.nextInt();
        int boy[]=new int[6];
        int girl[]=new int[6];
        int count=0;
        for(int i=0;i<n;i++){
            int e=s.nextInt(), y=s.nextInt();
            if(e==0) girl[y-1]++;
            else boy[y-1]++;
        }
        int sum=0;
        for(int i=0;i<6;i+=2){
            if(i==0){
                sum=boy[i]+boy[i+1]+girl[i]+girl[i+1];
                count+=num(sum,k);
                
            } 
            else{
                sum=boy[i]+boy[i+1];
                count+=num(sum,k);
                sum=girl[i]+girl[i+1];
                count+=num(sum,k);
            }
        }
        System.out.print(count);
    }
}