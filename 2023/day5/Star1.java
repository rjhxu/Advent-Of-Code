import java.io.*;
import java.util.*;

class Range {
    private final long start;
    private final long end;

    public Range(long start, long end) {
        this.start = start;
        this.end = end;
    }
    public long getStart() {
        return start;
    }

    public long getEnd() {
        return end;
    }
    public boolean inRange(long val) {
        return val>=start && val<end;
    }

    @Override
    public String toString() {
        return "(" + start + ", " + end + ")";
    }
}
public class Star1 {

    @SuppressWarnings("unchecked")
    public static HashMap<Range, Long>[] maps = new HashMap[7];
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new FileReader("2023/day5/input.txt"));
        //populate seeds
        long[] seeds = Arrays.stream(s.nextLine().substring(7).trim().split(" +")).mapToLong(Long::parseLong).toArray();  
        s.nextLine();
        for (int i = 0; i < 7; i++) {
            maps[i] = new HashMap<Range, Long>();
        }
        String line;
        for(int i =0; i<7; i++) {
            while (s.hasNextLine() && !(line = s.nextLine()).isEmpty()) {
                if(Character.isDigit(line.charAt(0))) {
                    String[] nums = line.trim().split(" +");
                    maps[i].put(
                        new Range(
                            Long.parseLong(nums[1]), 
                            Long.parseLong(nums[1])+Long.parseLong(nums[2])
                        ), 
                        Long.parseLong(nums[0])-Long.parseLong(nums[1])
                    );
                }
            }
        }
        for(int i = 0; i<seeds.length; i++) {

            for(int j =0; j<7; j++) {
                for(Range range : maps[j].keySet()){

                    if(range.inRange(seeds[i])) {
                        seeds[i]=seeds[i]+maps[j].get(range);
                        break;
                    }
                }
            }
        }
        Arrays.sort(seeds);
        System.out.println(seeds[0]);
        s.close();
    }
}
