import java.io.*;
import java.util.*;

public class day12020 
{
	public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new FileReader("input1.txt"));
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        String str = "";
        while(!str.equals("x"))
        {
            str = br.readLine();
            numbers.add(Integer.parseInt(str));
        }
        for(int j = 0; j<numbers.size(); j++)
        {
            int n = numbers.get(j);
            for(int i = 0; i<numbers.size(); i++)
            {
                int o = numbers.get(i);
                if(n + o == 2020)
                {
                    System.out.println(n);
                    System.out.println(o);
                    System.out.println(n*o);
                    br.close();
                    System.exit(0);
                }
            }
        }
	}

}