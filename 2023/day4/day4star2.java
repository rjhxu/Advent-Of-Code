
import java.io.*;
import java.util.*;

public class day4star2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new FileReader("2023/day4/input.txt"));
        int[] freq = new int[198];
        Arrays.fill(freq, 1);
        int cards =0;
        for(int i = 0; i<198; i++) {
            cards++;
            String line = s.nextLine().trim();
            String[] winners = line.substring(9, 40).trim().split(" +");
            String[] entries = line.substring(41).trim().split(" +");
            //populating set of winning numbers
            HashSet<Integer> nums = new HashSet<>();
            for(int j =0; j<winners.length; j++) {
                nums.add(Integer.parseInt(winners[j]));
            }

            int numwins = 0;
                
            for(String a : entries) {
                if(nums.contains(Integer.parseInt(a))) {
                    numwins++;
                }
            }
            for(int j = i+1; j<= i+numwins; j++) {
                freq[j]+=freq[i];
            }
            cards+=freq[i]*numwins;
            
        }
        System.out.println(cards);

        s.close();
    }
}
