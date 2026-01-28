import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String[] a = new String[5];
        String[] b = new String[5];
        int startTime = 0;
        int endTime = 0;

        for (int i = 0; i < 5; i++) {
            a[i] = st.nextToken();
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 5; i++) {
            b[i] = st.nextToken();
        }

        startTime = Integer.parseInt(a[4]) + Integer.parseInt(a[2])*60 + Integer.parseInt(a[0])*3600;
        endTime = Integer.parseInt(b[4]) + Integer.parseInt(b[2])*60 + Integer.parseInt(b[0])*3600;

        if (startTime > endTime) {
            System.out.println(endTime - startTime + 3600 * 24);
        } else {
            System.out.println(endTime - startTime);
        }
    }
}