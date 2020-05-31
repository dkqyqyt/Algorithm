package Topological_Sort;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.LinkedList;

public class n2252_줄세우기 {
	static StringTokenizer st;
	
	static int n,m;
	
	static int[] indegree;
	static ArrayList<Integer>[] students;
	static LinkedList<Integer> que;
	static ArrayList<Integer> line;
	
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = stoi(st.nextToken());
		m = stoi(st.nextToken());
		
		indegree = new int[n+1];
		que = new LinkedList<Integer>();
		line = new ArrayList<Integer>();
		students = new ArrayList[n+1];
		for(int i = 1; i < n+1; i++) {
			students[i] = new ArrayList<Integer>();
		}
		
		for(int i = 0; i < m; i++) {
			String[] input = br.readLine().split(" ");
			int small = stoi(input[0]);
			int tall = stoi(input[1]);
			
			students[small].add(tall);
			indegree[tall]++;
		}
		init();
		lineup();
		
	}
	static void init() {
		for(int i = 1; i < n+1; i++) {
			if(indegree[i] == 0) {
				que.add(i);
			}
		}
	}
	
	static void lineup() {
		while(!que.isEmpty()) {
			int student = que.poll();
			System.out.print(student+ " ");
			
			for(int i = 0; i < students[student].size(); i++) {
				int taller = students[student].get(i);
				if(--indegree[taller] == 0) {
					que.add(taller);
				}
			}
		}
	}

}
