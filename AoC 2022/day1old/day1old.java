package day1old;
import java.io.*;
import java.util.*;

public class day1old 
{
	public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
		int sum = 0;
        ArrayList<Integer> elves = new ArrayList<Integer>();
        while(true)
        {
            String line = br.readLine();
            if(line.equals("")) {
                elves.add(sum);
                sum=0;
            } else if(line.equals("x")) {
                break;
            } else {
                sum+=Integer.parseInt(line);
            }
        }
        Collections.sort(elves);
        System.out.println(elves.get(elves.size()-1)+elves.get(elves.size()-2)+elves.get(elves.size()-3));
        br.close();
	}

}