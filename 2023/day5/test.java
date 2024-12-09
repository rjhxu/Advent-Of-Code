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

    public boolean overlaps(Range other) {
        return this.start < other.end && other.start < this.end;
    }

    @Override
    public String toString() {
        return "(" + start + ", " + end + ")";
    }
}

public class test {
    @SuppressWarnings("unchecked")
    public static List<Map.Entry<Range, Long>>[] maps = new ArrayList[7];

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("2023/day5/input1.txt"));

        // Parse seed ranges
        String[] seedRangeParts = reader.readLine().substring(7).trim().split(" +");
        List<Range> seedRanges = new ArrayList<>();
        for (int i = 0; i < seedRangeParts.length; i += 2) {
            long start = Long.parseLong(seedRangeParts[i]);
            long end = Long.parseLong(seedRangeParts[i + 1]);
            seedRanges.add(new Range(start, end));
        }

        reader.readLine(); // Skip the empty line

        // Initialize maps for each category
        for (int i = 0; i < 7; i++) {
            maps[i] = new ArrayList<>();
        }

        // Parse mappings
        String line;
        for (int i = 0; i < 7; i++) {
            while ((line = reader.readLine()) != null && !line.isEmpty()) {
                if (Character.isDigit(line.charAt(0))) {
                    String[] nums = line.trim().split(" +");
                    long destStart = Long.parseLong(nums[0]);
                    long srcStart = Long.parseLong(nums[1]);
                    long rangeLength = Long.parseLong(nums[2]);

                    Range sourceRange = new Range(srcStart, srcStart + rangeLength);
                    long offset = destStart - srcStart;
                    maps[i].add(new AbstractMap.SimpleEntry<>(sourceRange, offset));
                }
            }
        }

        // Process seed ranges through mappings
        for (int j = 0; j < 7; j++) {
            List<Range> newRanges = new ArrayList<>();
            for (Range seedRange : seedRanges) {
                for (Map.Entry<Range, Long> entry : maps[j]) {
                    Range mapRange = entry.getKey();
                    long offset = entry.getValue();

                    // Check if ranges overlap
                    if (seedRange.overlaps(mapRange)) {
                        long overlapStart = Math.max(seedRange.getStart(), mapRange.getStart());
                        long overlapEnd = Math.min(seedRange.getEnd(), mapRange.getEnd());

                        // Transform the overlapping range
                        newRanges.add(new Range(overlapStart + offset, overlapEnd + offset));
                    }
                }
            }
            seedRanges = newRanges;
        }

        // Find the lowest location
        long minLocation = Long.MAX_VALUE;
        for (Range range : seedRanges) {
            minLocation = Math.min(minLocation, range.getStart());
        }

        System.out.println(minLocation);
        reader.close();
    }
}