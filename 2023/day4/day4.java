import java.util.*;
import java.io.*;

public class day4 {
    @SuppressWarnings("unused")
    public static void main(String[] args) throws FileNotFoundException {

        Scanner s = new Scanner(new FileReader("input.txt"));
        int sum = 0;
        for(int i =0; i<198; i++) {
            String line = s.nextLine();
            String[] win = line.substring(9,40).trim().split(" +");
            String[] entry = line.substring(41).trim().split(" +");
            //create and populate hashset for winning numbers
            HashSet<Integer> winners = new HashSet<>();
            for(int j = 0; j<win.length; j++) {
                winners.add(Integer.parseInt(win[j]));
            }
        }
        s.close();
    }
}
