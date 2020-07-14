package BackTracking;

import java.io.*;
import java.util.*;

public class n3980_선발명단 {
	static StringTokenizer st;
	
	static int score, maxScore;
	
	static boolean[] batched;
	
	static int[][] ability;
	
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int TCs = stoi(br.readLine());
		
		for(int i = 0; i < TCs; i++) {
			score = 0;
			maxScore = 0;
			batched = new boolean[11];
			ability = new int[11][11];
			
			for(int j = 0; j < 11; j++) {
				st = new StringTokenizer(br.readLine());
				for(int k = 0; k < 11; k++) {
					ability[j][k] = stoi(st.nextToken());
				}
			}
			
			track(0,score);
			System.out.println(maxScore);
		}
	}
	
	static void track(int player, int score) {
		if(player == 11) {
			if(score > maxScore) {
				maxScore = score;
			}
			return;
		}
		
		for(int position = 0; position < 11; position++) {
			if(ability[player][position] == 0) continue;
			if(batched[position]) continue;
			
			batched[position] = true;
			track(player + 1, score + ability[player][position]);
			batched[position] = false;
		}
	}
}
