package DFS_BFS;

import java.io.*;
import java.util.*;

public class n10282_해킹 {
	static int INF = 10000001;
	static StringTokenizer st;
	static int n,d,c;
	static int[] dist;
	static ArrayList<Integer> time[],node[];
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = stoi(br.readLine());
		
		for(int i = 0;i<tc;i++) {
			st = new StringTokenizer(br.readLine());
			
			n = stoi(st.nextToken());
			d = stoi(st.nextToken());
			c = stoi(st.nextToken());
			
			dist = new int[n+1];
			node = new ArrayList[n+1];
			time = new ArrayList[n+1];
			
			
			for(int j = 0;j<n+1;j++) {
				dist[j] = INF;
				node[j] = new ArrayList<>();
				time[j] = new ArrayList<>();
			}
			
			for(int j = 0;j<d;j++) {
				st= new StringTokenizer(br.readLine());
				
				int a,b,s;
				
				a = stoi(st.nextToken());
				b = stoi(st.nextToken());
				s = stoi(st.nextToken());
				
				node[b].add(a);
				time[b].add(s);
			}
			
			PriorityQueue<int[]> que = new PriorityQueue<>(new Comparator<int[]>() {
				public int compare(int[]a , int[] b) {
					return a[0]-b[0];
				}
			});
			
			dist[c] = 0;
			que.add(new int[] {0,c});
			
			while(!que.isEmpty()) {
				int start = que.peek()[1];
				int timee = que.peek()[0];
				que.poll();
				
				if(dist[start]<timee) {
					continue;
				}
				
				for(int j = 0;j<node[start].size();j++) {
					int end,distt;
					end = node[start].get(j);
					distt = time[start].get(j);
					if(timee+distt<dist[end]) {
						dist[end] = timee+distt;
						que.add(new int[] {dist[end],end});
					}
					
				}
			}
			int infected = 0;
			int totaltime = 0;
			for(int j = 0;j<dist.length;j++) {
				if(dist[j]<INF) {
					infected++;
					if(totaltime <dist[j]) {
						totaltime = dist[j];
					}
				}
			}
			
			System.out.println(infected+" "+totaltime);
		}
	}

}