package DivideAndConquer;

import java.io.IOException; 
import java.io.BufferedReader; 
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n2630_색종이만들기 {
	static StringTokenizer st;
	static int[][] graph;
	static int[] colors = new int[2];
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = stoi(br.readLine());
		graph = new int[N][N];
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < N; j++) {
				graph[i][j] = stoi(st.nextToken());
			}
		}
		divide(0,0,N);
		System.out.println(colors[0]);
		System.out.println(colors[1]);
	}
	
	static void divide(int x, int y, int len) {
		if(len == 0) return;
		if(!isSame(x,y,len)) {
			len = len/2;
			divide(x,y,len);
			divide(x, y+len, len);
			divide(x+len,y,len);
			divide(x+len, y+len, len);
		}
	}
	
	static boolean isSame(int x, int y, int len) {
		int color = graph[x][y];
		for(int i = x; i < x+len; i++) {
			for(int j = y; j < y+len; j++) {
				if(color != graph[i][j]) {
					return false;
				}
			}
		}
		colors[color]++;
		return true;
	}

}
