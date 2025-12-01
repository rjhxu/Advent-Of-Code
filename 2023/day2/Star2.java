import java.util.*;
import java.io.*;

public class Star2 {
    public static long sum  = 0;
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new FileReader("2023/day2/input.txt"));
        for(int i =1; i<101; i++) {
            String[] temp = in.nextLine().split(":");
            String line = temp[1].trim();
            check(line);
        }
        System.out.println(sum);
        in.close();
    }
    public static void check(String str) {
        int bm = 0, gm = 0, rm = 0;
        String[] arr1 = str.split(";");
        for(int i =0; i<arr1.length; i++) {
            String[] arr2 = arr1[i].split(",");
            for(int j = 0; j<arr2.length; j++) {
                String[] arr3 = arr2[j].trim().split(" ");
                switch(arr3[1].charAt(0)) {
                    case 'b':
                        if(Integer.parseInt(arr3[0])>bm) {bm=Integer.parseInt(arr3[0]);}
                        break;
                    case 'g':
                        if(Integer.parseInt(arr3[0])>gm) {gm=Integer.parseInt(arr3[0]);}
                        break;
                    case 'r':
                        if(Integer.parseInt(arr3[0])>rm) {rm=Integer.parseInt(arr3[0]);}
                        break;
                }
            }
        }
        sum+=(bm*gm*rm);
    }
}