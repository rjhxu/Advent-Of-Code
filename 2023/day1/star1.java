package day1;


import java.util.*;
import java.io.*;

public class star1 {
    public static void main(String[] args) throws FileNotFoundException {

        Scanner s = new Scanner(new FileReader("2023/day1/input.txt"));
        int sum = 0;
        while(s.hasNextLine()){
            String line = s.nextLine();
            for(int i = 0; i<line.length(); i++){
                if(Character.isDigit(line.charAt(i))) {
                    sum+=10*Character.getNumericValue(line.charAt(i));
                    break;
                }
            }
            for(int i = line.length()-1; i>=0; i--) {
                if(Character.isDigit(line.charAt(i))) {
                    sum+=Character.getNumericValue(line.charAt(i));
                    break;
                }
            }
        }
        System.out.println(sum);
        s.close();
    }
}
