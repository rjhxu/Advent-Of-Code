#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>st
using namespace std;

int main() {
    string line;
    ifstream input("input.txt");
    int cur = 0;
    vector<int> v;
    while(getline(input, line)) {
        if(line.empty()) {
            v.push_back(cur);
            cur = 0;
        }
        else {
            cur+=stoi(line);
        }
    }
    v.push_back(cur);
    cur =0;
    sort(v.begin(), v.end(), greater<int>());
    
    for(int i =0; i<3; i++) {
        cur+=v[i];
    }
    cout << cur << endl;
}