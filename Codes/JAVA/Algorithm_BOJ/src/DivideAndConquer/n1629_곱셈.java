package DivideAndConquer;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n1629_곱셈 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		long A = Long.parseLong(st.nextToken());
		long B = Long.parseLong(st.nextToken());
		long C = Long.parseLong(st.nextToken());
		System.out.println(division(A,B,C));
	}
	
	static long division(long a, long b, long c) {
//		System.out.println(a+" "+b+" "+c);
		a = (long)(a%c);
		if(b == 0) {
			return 1;
		}
		long temp = (long)
		if(b%2 == 1) {
			return (a * Math.pow(division(a,(b-1)/2,c),2)) % c;
		}else {
			return (long)(Math.pow(division(a,b/2,c), 2) % c);
		}
	}
}
 