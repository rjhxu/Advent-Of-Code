import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Scanner;

public class star2 {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner s = new Scanner(new FileReader("2023/day1/input.txt"));
        int sum = 0;
        String[] nums = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        HashMap<String, Integer> mp = new HashMap<>();
        mp.put("one", 1);
        mp.put("two", 2);
        mp.put("three", 3);
        mp.put("four", 4);
        mp.put("five", 5);
        mp.put("six", 6);
        mp.put("seven", 7);
        mp.put("eight", 8);
        mp.put("nine", 9);
        while(s.hasNextLine()) {
            int min = Integer.MAX_VALUE, max = 0;
            String first = "", last = "", line = s.nextLine();
            for(String i : nums) {
                if(line.indexOf(i)>-1 && line.indexOf(i)<=min) {
                    min = line.indexOf(i);
                    first = i;
                }
                if(line.lastIndexOf(i)>=max) {
                    max = line.lastIndexOf(i);
                    last = i;
                }
            }
            if(mp.containsKey(first)) {
                sum+=mp.get(first)*10;
            } else {
                sum+=Integer.parseInt(first)*10;
            }

            if(mp.containsKey(last)) {
                sum+=mp.get(last);
            } else {
                sum+=Integer.parseInt(last);
            }
        }
        System.out.println(sum);
        s.close();
    }
}
