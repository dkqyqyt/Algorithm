package DivideAndConquer;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n1780_종이의개수 {
	static StringTokenizer st;
	static int[][] graph;
	static int[] ans = new int[3];
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
		for(int i = 0; i < ans.length; i++) {
			System.out.println(ans[i]);
		}
	}
	
	static void divide(int x, int y, int len) {
		if(len == 0) return;
		if(!isSame(x,y,len)) {
			len = len/3;
			divide(x,y,len);
			divide(x,y+len,len);
			divide(x,y+len*2, len);
			divide(x+len,y,len);
			divide(x+len,y+len,len);
			divide(x+len,y+len*2,len);
			divide(x+len*2,y,len);
			divide(x+len*2,y+len,len);
			divide(x+len*2,y+len*2,len);
		}
	}
	
	static boolean isSame(int x, int y, int len) {
		int num = graph[x][y];
		for(int i = x; i < x+len; i++) {
			for(int j = y; j < y+len; j++) {
				if(num != graph[i][j]) return false;
			}
		}
		ans[num+1]++;
		return true;
	}

}
