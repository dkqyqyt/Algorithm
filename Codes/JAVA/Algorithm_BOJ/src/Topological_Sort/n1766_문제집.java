package Topological_Sort;

import java.io.*;
import java.util.*;

public class n1766_문제집 {
	static StringTokenizer st;
	
	static int n,m;
	
	static String[] input;
	static int[] indegree;
	static ArrayList<Integer>[] students;
	static PriorityQueue<Integer> que;
	
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		input = br.readLine().split(" ");
		n = stoi(input[0]);
		m = stoi(input[1]);
		
		indegree = new int[n+1];
		que = new PriorityQueue<Integer>();
		students = new ArrayList[n+1];
		for(int i = 0; i < n+1; i++) {
			students[i] = new ArrayList<Integer>();
		}
		
		for(int i = 0; i < m; i++) {
			input = br.readLine().split(" ");
			int a = stoi(input[0]);
			int b = stoi(input[1]);
			
			students[a].add(b);
			indegree[b]++;
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
			int stu = que.poll();
			System.out.print(stu + " ");
			
			for(int i = 0; i < students[stu].size(); i++) {
				int next = students[stu].get(i);
				if(--indegree[next] == 0) {
					que.add(next);
				}
			}
		}
	}
}
