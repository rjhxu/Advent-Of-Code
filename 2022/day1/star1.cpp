#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string line;
    ifstream input("input.txt");
    int max = 0, cur = 0;
    while(getline(input, line)) {
        if(line.empty()) {
            max = max > cur ? max : cur;
            cur = 0;
        }
        else {
            cur+=stoi(line);
        }
    }
    max = max> cur ? max : cur;
    cout << max << endl;
}