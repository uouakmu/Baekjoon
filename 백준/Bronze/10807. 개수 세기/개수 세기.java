import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int ans = 0;
		int n = sc.nextInt();
		int[] nums = new int[n];
		
		for (int i=0; i<n; i++) {
			nums[i] = sc.nextInt();
		}
		int v = sc.nextInt();
		
		for (int i=0; i<n; i++) {
			if(nums[i] == v) {
				ans++;
			}
		}
		System.out.println(ans);		
	}
}