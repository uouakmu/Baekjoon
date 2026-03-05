import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());

        int hour = (a+b) % 12;
        if (hour % 12 == 0) {
            System.out.println(12);
        } else {
            System.out.println(hour);
        }
    }
}