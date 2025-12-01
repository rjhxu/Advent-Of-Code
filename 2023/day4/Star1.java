import java.util.*;
import java.io.*;

public class Star1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new FileReader("2023/day4/input.txt"));
        int sum = 0;

        for(int i = 0; i<198; i++) {
            String line = s.nextLine();
            String[] win = line.substring(9, 40).trim().split(" +");
            String[] entry = line.substring(41).trim().split(" +");

            HashSet<String> winners = new HashSet<>(Arrays.asList(win));
            
            int wins =0;
            for (String en : entry) {
                if (winners.contains(en)) {
                    wins++;
                }
            }
            if(wins>0){
                sum+=Math.pow(2, wins-1);
            }
        }

        s.close();
        System.out.println(sum);
    }
}