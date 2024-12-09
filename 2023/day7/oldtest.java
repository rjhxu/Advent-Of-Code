package day7;
import java.util.*;
import java.io.*;

public class oldtest {
    public static void main(String[] args) throws FileNotFoundException {

        String[] hands = {"KKKKK", "AAAAA", "A1234", "K1234", "AAKK1", "KKAA1", "AAAKK", "KKKK1", "AAA12", "11AKJ"};
        Arrays.sort(hands, new sortCards());
        System.out.println(Arrays.toString(hands));
    }
}
class sortCards implements Comparator<String> {
    public int compare(String a, String b) {
        HashMap<Character, Integer> cardValue = new HashMap<>();
        cardValue.put('A', 14);
        cardValue.put('K', 13);
        cardValue.put('Q', 12);
        cardValue.put('J', 11);
        cardValue.put('T', 10);
        cardValue.put('9', 9);
        cardValue.put('8', 8);
        cardValue.put('7', 7);
        cardValue.put('6', 6);
        cardValue.put('5', 5);
        cardValue.put('4', 4);
        cardValue.put('3', 3);
        cardValue.put('2', 2);
        HashMap<Character, Integer> ac  = new HashMap<>();
        HashMap<Character, Integer> bc = new HashMap<>();
        int amax = 0;
        int bmax = 0;
        for(int i = 0; i<a.length(); i++) {
            if(ac.containsKey(a.charAt(i))) {
                ac.put(a.charAt(i), ac.get(a.charAt(i))+1);
                if(ac.get(a.charAt(i)) > amax) {
                    amax = ac.get(a.charAt(i));
                }
            } else {
                ac.put(a.charAt(i), 1);
                if(ac.get(a.charAt(i)) > amax) {
                    amax = ac.get(a.charAt(i));
                }
            }
            if(bc.containsKey(b.charAt(i))) {
                bc.put(b.charAt(i), bc.get(b.charAt(i))+1);
                if(bc.get(b.charAt(i)) > bmax) {
                    bmax = bc.get(b.charAt(i));
                }
            } else {
                bc.put(b.charAt(i), 1);
                if(bc.get(b.charAt(i)) > bmax) {
                    bmax = bc.get(b.charAt(i));
                }
            }
        }
        if(ac.size()!=bc.size()) {
            return ac.size()-bc.size();
        }
        if(ac.size()==2) {
            if(amax!=bmax) {
                return amax - bmax;
            }
            for(int i =0; i< a.length(); i++) {
                if(a.charAt(i)!=b.charAt(i)) {
                    return cardValue.get(a.charAt(i)) - cardValue.get(b.charAt(i));
                }
            }
        }
        if(ac.size()==3) {
             if(amax!=bmax) {
                return amax - bmax;
            }
            for(int i =0; i< a.length(); i++) {
                if(a.charAt(i)!=b.charAt(i)) {
                    return cardValue.get(a.charAt(i)) - cardValue.get(b.charAt(i));
                }
            }
        }
        for(int i =0; i< a.length(); i++) {
            if(a.charAt(i)!=b.charAt(i)) {
                return cardValue.get(a.charAt(i)) - cardValue.get(b.charAt(i));
            }
        }

        return 0;
    }
}