package N과M;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class N과M_6 {
	static StringTokenizer st;
	static int N,M;
	static ArrayList<Integer> numbers;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		numbers = new ArrayList<>();
		for(int i = 0; i < N; i++) {
			numbers.add(sc.nextInt());
		}
		Collections.sort(numbers);
		ArrayList<Integer> path = new ArrayList<>();
		track(0,path,-1);
	}
	
	static void track(int depth, ArrayList<Integer> path, int preIndex) {
		if(depth == M) {
			for(int num:path) {
				System.out.print(num+" ");
			}
			System.out.println();
			return;
		}
		
		for(int i = preIndex+1; i < numbers.size(); i++) {
			path.add(numbers.get(i));
			track(depth+1,path,i);
			path.remove(path.size()-1);
		}
	}

}
