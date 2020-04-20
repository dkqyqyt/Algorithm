package DFS;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class n13023_ABCDE {
	static StringTokenizer st;
	static int N,M;
	static boolean answer;
	static boolean visit[];
	static ArrayList<Integer> graph[];
	static int stoi(String s) {return Integer.parseInt(s);}
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = stoi(st.nextToken());
		M = stoi(st.nextToken());
		graph = new ArrayList[N];
		visit = new boolean[N];
		
		for(int i = 0; i < N; i++) {
			graph[i] = new ArrayList<Integer>();
		}
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = stoi(st.nextToken());
			int b = stoi(st.nextToken());
			graph[a].add(b);
			graph[b].add(a);
		}
		
		for(int i = 0;i < M; i++) {
			if(answer) {
				break;
			}
			visit[i] = true;
			dfs(0,i);
			visit[i] = false;
		}
		if(answer) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}
		
	}
	
	static void dfs(int depth, int start) {
		if(depth == 4) {
			answer = true;
			return;
		}
		
		for(int next_node:graph[start]) {
			if(visit[next_node]) {continue;}
			
			visit[next_node] = true;
			dfs(depth+1,next_node);
			visit[next_node] = false;
		}
	}

}
