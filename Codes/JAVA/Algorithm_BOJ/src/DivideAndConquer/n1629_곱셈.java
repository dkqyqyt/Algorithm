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
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		System.out.println(division(A,B,C));
	}
	
	static long division(long a, long b, long c) {
//		System.out.println(a+" "+b+" "+c);
		a = a%c;
		if(b == 0) {
			return 1;
		}
		long temp = division(a,b/2,c)%c;
		if(b%2 == 1) {
			return (((temp*temp)%c)*a)%c;
		}else {
			return (temp*temp)%c;
		}
	}
}
 