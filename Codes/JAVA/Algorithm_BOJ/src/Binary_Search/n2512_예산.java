package Binary_Search;

import java.io.*;
import java.util.*;

public class n2512_예산 {
	static StringTokenizer st;
	static int ans, n, totalLimit, limit, maxLimit;
	static int[] budgets;
	
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// input
		n = stoi(br.readLine());
		budgets = new int[n];
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			int budget = stoi(st.nextToken());
			if(budget > maxLimit) {
				maxLimit = budget;
			}
			budgets[i] = budget;
		}
		totalLimit = stoi(br.readLine());
		
		binarySearch(0,maxLimit);
		System.out.println(ans);
	}
	
	static void binarySearch(int l, int r) {
		if(l > r) {
			return;
		}
		int pivot = (l+r)/2;
		if(pivot < ans) {
			return;
		}
		int totalBudget = 0;
		
		for(int i = 0; i < budgets.length; i++) {
			int budget = budgets[i];
			if(budget < pivot) {
				totalBudget += budget;
			}else {
				totalBudget += pivot;
			}
		}
		
		if(totalBudget > totalLimit) {
			binarySearch(l,pivot-1);
		}else {
			ans = pivot;
			binarySearch(pivot+1,r);
		}
	}

}
