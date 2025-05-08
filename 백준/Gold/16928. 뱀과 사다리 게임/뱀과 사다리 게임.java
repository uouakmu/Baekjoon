import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	// 백준 16928
	// 주사위 숫자를 조종가능하다면, 최소 몇 번만에 도착?
	// 10*10
	// 1~100번 칸
	// 도착 칸이 사다리나 뱀이면, 따라감
	// 목표 : 1번 → 100번

	// bfs : 주사위 던지기, 사다리, 뱀 처리
	public static int bfs(int start, int[] ladders, int[] snakes) {
		boolean[] visited = new boolean[101]; // 1~100까지의 칸
		Queue<Integer> queue = new LinkedList<>(); // 큐 생성
		queue.offer(start); // 큐에 start 삽입
		visited[start] = true; // 입력된 start 부터 넣고 시작

		int moves = 0; // 이동 횟수

		while (!queue.isEmpty()) { // 큐가 살아있으면
			int size = queue.size(); // 큐 크기 기억

			for (int i = 0; i < size; i++) { // 큐 전체를 돈다
				int current = queue.poll();

				// 현재 지점이 100번이라면
				if (current == 100) {
					return moves; // 이동 횟수 반환
				}

				// 주사위 던지기
				for (int dice = 1; dice <= 6; dice++) {
					int next = current + dice;

					// 이동 가능한 지역이면
					if (next <= 100 && !visited[next]) {
						visited[next] = true; // 방문 처리

						// 사다리나 뱀이 있으면 이동
						if (ladders[next] != 0) {
							next = ladders[next];
						} else if (snakes[next] != 0) {
							next = snakes[next];
						}

						queue.offer(next); // 다음 방문지를 큐에 넣음
					}
				}
			}
			moves++; // 한 단계의 큐가 끝났으므로 이동횟수 증가
		}
		return -1; // 이동할 수 없는 경우
	}

	public static void main(String[] args) throws IOException {
		// 입력 받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]);
		int m = Integer.parseInt(input[1]);

		int[] ladders = new int[101];
		int[] snakes = new int[101];

		// 사다리 값 입력
		for (int i = 0; i < n; i++) {
			String[] ladder = br.readLine().split(" ");
			int start = Integer.parseInt(ladder[0]);
			int end = Integer.parseInt(ladder[1]);
			ladders[start] = end;
		}

		// 뱀 값 입력
		for (int i = 0; i < m; i++) {
			String[] snake = br.readLine().split(" ");
			int start = Integer.parseInt(snake[0]);
			int end = Integer.parseInt(snake[1]);
			snakes[start] = end;
		}
		System.out.println(bfs(1, ladders, snakes));
	}

}