import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		
		int i;
		for(i= 0; i < s.length() / 2; i++) {
			if(s.charAt(i)!= s.charAt(s.length() - i - 1)) {
				break;
			}
		}
		
		if(i != s.length() / 2) {
			System.out.println("false");
		}else {
			System.out.println("true");
		}
		sc.close();
	}
}