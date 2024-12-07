package day2;

import java.util.*;
import java.io.*;

public class day2part2
{   
	public static void main(String[] args) throws IOException
    {
		Scanner s = new Scanner(new File("day2/input.txt"));
        int points = 0;
        while(s.hasNextLine())
        {
            String line = s.nextLine();
            char opp = line.charAt(0);
            char our = line.charAt(2);
            points+=check(opp, our);
            switch(our)
            {
                case 'X':
                    points+=1;
                    break;
                case 'Y':
                    points+=2;
                    break;
                case 'Z':
                    points+=3;
                    break;
            }
        }
        System.out.println(points);
	}


    public static int check(char opp, char our)
    {
        switch(opp)
        {
            case 'A':
                return 0;
            case 'B':
                return 0;
            case 'C':
                return 0;
            default:
                return 0;
        }


    }
	
}