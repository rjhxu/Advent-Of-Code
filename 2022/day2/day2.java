package day2;

import java.util.*;
import java.io.*;

public class day2
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
        s.close();
	}


    public static int check(char opp, char our)
    {
        if((our-0)-(opp-0)==24 || (our-0)-(opp-0)==21) {
            return 6;
        } else if((our-0)-(opp-0)==23) {
            return 3;
        }else {
            return 0;
        }
    }
	
}