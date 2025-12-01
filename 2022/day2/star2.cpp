#include<fstream>
#include<iostream>
#include<string>

int choice(int opp, int you) {
    if(you==2) {
        return opp;
    }
    if (you==1)  { // lose
        return (opp+1)%3 + 1;
    }
    return opp%3 + 1;
}
int main() {
    std::ifstream input("input.txt");
    std::string line;
    int score = 0;
    char opp, you;
    while(getline(input, line)) {
        opp=line[0];
        you=line[2];
        score+=(you-88)*3;
        score+=choice(opp-64, you-87);
    }
    std::cout << score << std::endl;    
}