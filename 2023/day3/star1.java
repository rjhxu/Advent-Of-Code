

import java.util.*;
import java.io.*;

public class star1 {
    public static int sum  = 0;
    public static char[][] m = new char[140][140];
    static BufferedReader br;
    static StringTokenizer st;
    static String temp = "";
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(new FileInputStream("2023/day3/input.txt")));
        for(int i =0; i<140; i++) {
            String line = readLine();
            for(int j = 0; j<140; j++) {
                m[i][j]=line.charAt(j);
            }
        }
        for(int i = 0; i<140; i++) {
            for(int j = 0; j<140; j++) {
                if(m[i][j]!='.' && !Character.isDigit(m[i][j])) {
                    check(i+1, j, false);
                    check(i+1, j+1, false);
                    check(i+1, j-1, false);
                    check(i-1, j, false);
                    check(i-1, j+1, false);
                    check(i-1, j-1, false);
                    check(i, j+1, false);
                    check(i, j-1, false);
                }
            }
        }
        
        System.out.println(sum);
    }
    public static void check(int r, int c, boolean found) {
        if(r<0 || r>=140 || c<0 || c>=140 || (!found && !Character.isDigit(m[r][c]))) {
            return;
        }
        if(!Character.isDigit(m[r][c])) {
            read(r, c+1);
            return;
        }
        
        if(c==0 && Character.isDigit(m[r][c])) {
            read(r, c);
            return;
        }
        check(r, c-1, true);
    }
    public static void read(int r, int c) {
        if(!Character.isDigit(m[r][c])) {
            sum+=Integer.parseInt(temp);
            temp = "";
            return;
        }
        if(c==139) {
            temp+=m[r][c];
            m[r][c]='.';
            sum+=Integer.parseInt(temp);
            temp = "";
            return;
        }
        temp+=m[r][c];
        m[r][c]='.';
        read(r, c+1);
    }
    
    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }

    static long readLong() throws IOException {
        return Long.parseLong(next());
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }

    static double readDouble() throws IOException {
        return Double.parseDouble(next());
    }

    static char readCharacter() throws IOException {
        return next().charAt(0);
    }

    static String readLine() throws IOException {
        return br.readLine().trim();
    }
}
