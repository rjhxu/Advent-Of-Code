package day5;
import java.io.*;

public class day5star2 {
    public static void main(String[] args) throws FileNotFoundException {

        int temp  = 0;
        long time = 49979494;
        long distance = 263153213781851l;
        for(int j = 0; j<time; j++) {
            if(distance <= j*(time-j)) {
                temp++;
            }
        }
        System.out.println(temp);
    }
}
