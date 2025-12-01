#include<fstream>
#include<iostream>
#include<string>

int main() {
    std::ifstream input("input.txt");
    std::string line;
    int score = 0;
    char opp, you;
    while(getline(input, line)) {
        opp=line[0];
        you=line[2];
        score+=you-87;
        if(you-opp==21 || you-opp==24) {
            score+=6;
        } else if (you-opp==23) {
            score+=3;
        } else {
            score+=0;
        }
    }
    
    std::cout << score << std::endl;    
}