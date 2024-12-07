package day5;
import java.io.*;

public class day5 {
    public static void main(String[] args) throws FileNotFoundException {
        int sum = 1;
        int temp  = 0;
        int[] times = {49, 97, 94, 94};
        int[] distance = {263, 1532, 1378, 1851};
        for(int i = 0; i<4; i++) {
            for(int j = 0; j<times[i]; j++) {
                if(distance[i] <= j*(times[i]-j)) {
                    temp++;
                }
            }
            sum*=temp;
            temp = 0;
        }
        System.out.println(sum);
    }
}
