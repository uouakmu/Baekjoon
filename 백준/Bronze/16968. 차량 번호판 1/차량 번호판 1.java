import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] carN = sc.next().toCharArray();

        int ans = 1;

        for (int i = 0; i < carN.length; i++) {
            if (i == 0) {
                ans *= (carN[i] == 'c') ? 26 : 10;
            } else {
                if (carN[i] == carN[i - 1]) {
                    ans *= (carN[i] == 'c') ? 25 : 9;
                } else {
                    ans *= (carN[i] == 'c') ? 26 : 10;
                }
            }
        }

        System.out.println(ans);
    }
}