package Segment_Tree;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n11505_구간곱구하기 {
	static StringTokenizer st;
	
	static int modular = 1000000007;
	static int n,m,k;
	
	static long[] tree = new long[3000001];
	static int[] numbers;
	static int stoi(String s) { return Integer.parseInt(s); }
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		
		n = stoi(st.nextToken());
		m = stoi(st.nextToken());
		k = stoi(st.nextToken());
		
		numbers = new int[n];
		for(int i = 0; i < n; i++) {
			numbers[i] = stoi(br.readLine());
		}
		
		init(0,n-1,1);
//		for(int i = 1; i < 16; i++) {
//			System.out.print(i+" : ");
//			System.out.println(tree[i]);
//		}
		
		for(int i = 0; i < m + k; i++) {
//			for(int j = 1; j < 10; j++) {
//				System.out.print(j+" : ");
//				System.out.println(tree[j]);
//			}
			st = new StringTokenizer(br.readLine());
			int a = stoi(st.nextToken());
			int	b = stoi(st.nextToken());
			int c = stoi(st.nextToken());
			
			if(a == 1) {
				b--;
				numbers[b] = c;
				update(b,1,0,n-1,c);
			}else {
//				System.out.println(b+", "+c);
				long ans = multiply(b-1,c-1,1,0,n-1);
				System.out.println(ans);
			}
		}
	}
	
	static long init(int nodeL, int nodeR, int nodeNum) {
		if(nodeL == nodeR) {
			tree[nodeNum] = numbers[nodeL];
			return tree[nodeNum]%modular;
		}
		int mid = (nodeL+nodeR)/2;
		tree[nodeNum] = ((init(nodeL,mid,nodeNum*2)%modular) * (init(mid+1,nodeR,nodeNum*2+1)%modular))%modular;
		return tree[nodeNum];
	}
	
	static long multiply(int l, int r, int nodeNum, int nodeL, int nodeR) {
		if(l > nodeR || r < nodeL) {
			return 1;
		}
		if(l <= nodeL && r >= nodeR) {
//			System.out.println(nodeNum);
			return tree[nodeNum];
		}
		int mid = (nodeL + nodeR) / 2;
		return ((multiply(l,r,nodeNum*2,nodeL,mid)%modular) * (multiply(l,r,nodeNum*2+1,mid+1,nodeR)%modular))%modular;
	}
	
	static void update(int idx, int nodeNum, int nodeL, int nodeR, int newNum) {
		if(nodeL > idx || nodeR < idx) {
			return;
		}
		if(nodeL == nodeR) {
			tree[nodeNum] = newNum % modular;
		}
		if(nodeL != nodeR) {
			int mid = (nodeL + nodeR) / 2;
			update(idx,nodeNum*2,nodeL,mid,newNum);
			update(idx,nodeNum*2+1,mid+1,nodeR,newNum);
			
			tree[nodeNum] = ((tree[nodeNum*2])*(tree[nodeNum*2+1]))%modular;
		}
	}
}
