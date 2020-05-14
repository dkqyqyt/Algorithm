package DivideAndConquer;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n1992_쿼드트리 {
	static StringTokenizer st;
	static int[][] graph;
	static String ans = "";
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = stoi(br.readLine());
		graph = new int[N][N];
		
		for(int i = 0; i < N; i++) {
			String line = br.readLine();
			for(int j = 0; j < N; j++) {
				graph[i][j] = (int)(line.charAt(j));
			}
			
		}
		
		divide(0,0,N);
		System.out.println(ans);
	}
	
	static void divide(int x, int y, int len) {
		if(len == 0) return;
		if(!isSame(x,y,len)) {
			ans += '(';
			len = len/2;
			divide(x,y,len);
			divide(x,y+len,len);
			divide(x+len,y,len);
			divide(x+len,y+len,len);
			ans += ')';
		}
		
	}
	
	static boolean isSame(int x, int y, int len) {
		int num = graph[x][y];
		for(int i = x; i < x+len; i++) {
			for(int j = y;j < y+len; j++) {
				if(num != graph[i][j]) {
					return false;
				}
			}
		}
		ans += (char)num;
		return true;
	}

}
