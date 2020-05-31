package DivideAndConquer;

import java.io.*;
import java.util.*;

public class n11401_이항계수3 {
	static StringTokenizer st;
	
	static int n,k;
	static final int MOD = 1000000007; 
	static int stoi(String s) {
		return Integer.parseInt(s);
	}
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = stoi(st.nextToken());
		k = stoi(st.nextToken());
		
		System.out.println(binomial(n,k));
	}
	
	static int binomial(int n, int k) {
		if(k == 1) {
			return n;
		}else if(n == k) {
			return 1;
		}
		return (binomial(n-1,k) + binomial(n-1,k-1))%MOD;
	}

}
