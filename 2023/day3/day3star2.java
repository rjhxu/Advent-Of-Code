import java.util.*;
import java.io.*;

public class day3star2 {
    public static int sum  = 0;
    public static char[][] m = new char[140][140];
    static BufferedReader br;
    static StringTokenizer st;
    public static int[] dirx =  {-1, 0, 1};
    public static int[] diry =  {-1, 0, 1};
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(new FileInputStream("input.txt")));
        for(int i =0; i<140; i++) {
            String line = readLine();
            for(int j = 0; j<140; j++) {
                m[i][j]=line.charAt(j);
            }
        }
        for(int i = 0; i<140; i++) {
            for(int j = 0; j<140; j++) {
                ArrayList<Integer> partnumbers = new ArrayList<>();

                if(m[i][j]=='*') {
                    for(int k = 0; k<3; k++) {
                        for(int l =0; l<3; l++) {
                            int ti = i+dirx[k];
                            int tj = j+diry[l];
                            if(check(ti, tj)){
                                partnumbers.add(start(ti,tj));
                            }
                        }
                    }
                    if(partnumbers.size()>1) {
                        sum+=partnumbers.get(0)*partnumbers.get(1);
                    }
                }
            }
        }
        
        System.out.println(sum);
    }
    public static boolean check(int r, int c) {
        if(r<0 || r>=140 || c<0 || c>=140 || !Character.isDigit(m[r][c])) {
            return false;
        }
        return true;
    }

    public static int start(int r, int c){
        if(!Character.isDigit(m[r][c])) {
            return read(r, c+1, "");
        }
        
        if(c==0 && Character.isDigit(m[r][c])) {
            return read(r, c, "");
        }
        return start(r, c-1);
    }
    public static int read(int r, int c, String temp) {
        if(!Character.isDigit(m[r][c])) {
            int num =Integer.parseInt(temp);
            return num;
        }
        if(c==139) {
            temp+=m[r][c];
            m[r][c]='.';
            int num =Integer.parseInt(temp);
            return num;
        }
        temp+=m[r][c];
        m[r][c]='.';
        return read(r, c+1, temp);
    }
    static String readLine() throws IOException {
        return br.readLine();
    }
}
