package day2;

import java.util.*;
import java.io.*;

public class star1 {
    public static int sum  = 0;
    public static HashMap<String, Integer> mp = new HashMap<>();
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new FileReader("2023/day2/input.txt"));
        mp.put("blue", 14);
        mp.put("green", 13);
        mp.put("red", 12);
        for(int i =1; i<101; i++) {
            String[] temp = in.nextLine().split(":");
            String line = temp[1].trim();
            check(line, i);
        }
        System.out.println(sum);
        in.close();
    }
    public static void check(String str, int id) {
        String[] arr1 = str.split(";");
        for(int i =0; i<arr1.length; i++) {
            String[] arr2 = arr1[i].split(",");
            for(int j = 0; j<arr2.length; j++) {
                String[] arr3 = arr2[j].trim().split(" ");
                if(Integer.parseInt(arr3[0]) > mp.get(arr3[1])) {
                    return;
                }
            }
        }
        sum+=id;
    }
}
