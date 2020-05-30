package Topological_Sort;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.LinkedList;

public class n2623_음악프로그램 {
	static StringTokenizer st;
	static LinkedList<Integer> que;
	static ArrayList<Integer> answer;
	
	static int numOfSinger, numOfPD;
	
	static ArrayList<Integer>[] child;
	static int[] indegree;
	static boolean[] used;
	
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		numOfSinger = stoi(st.nextToken());
		numOfPD = stoi(st.nextToken());
		child = new ArrayList[numOfSinger+1];
		for(int i = 0; i < numOfSinger+1; i++) {
			child[i] = new ArrayList<Integer>();
		}
		indegree = new int[numOfSinger+1];
		used = new boolean[numOfSinger+1];
		answer = new ArrayList<Integer>();
		
		for(int i = 0; i < numOfPD; i++) {
			String[] input = br.readLine().split(" ");
			for(int j = 1; j < input.length-1; j++) {
				child[stoi(input[j])].add(stoi(input[j+1]));
				indegree[stoi(input[j+1])]++;
			}
		}
		que = new LinkedList<Integer>();
		for(int i = 1; i < numOfSinger+1; i++) {
			if(indegree[i] == 0) {
				que.push(i);
				used[i] = true;
			}
		}
		
		while(!que.isEmpty()) {
			int singer = que.pop();
//			System.out.println(singer);
			answer.add(singer);
			
			for(int i = 0; i < child[singer].size(); i++) {
				indegree[child[singer].get(i)]--;
			}
			
			for(int i = 1; i < numOfSinger+1; i++) {
				if(indegree[i] == 0 && !used[i]) {
					que.push(i);
					used[i] = true;
				}
			}
		}
		
		if(answer.size() == numOfSinger) {
			for(int i = 0; i < answer.size(); i++) {
				System.out.println(answer.get(i));
			}
		}else {
			System.out.println(0);
		}
	}

}
