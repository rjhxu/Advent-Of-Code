#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>

int main() {
    std::ifstream input("input.txt");
    std::string line;
    int sum = 0;
    while (getline(input, line)) {
        std::set<char> sack_one(line.begin(), line.end());
        getline(input, line);
        std::set<char> sack_two(line.begin(), line.end());
        getline(input, line);
        std::set<char> sack_three(line.begin(), line.end());
        std::set<char> common_chars;
        std::set_intersection(sack_one.begin(), sack_one.end(),
                              sack_two.begin(), sack_two.end(),
                              std::inserter(common_chars, common_chars.begin()));
        std::vector<char> final_common_chars;
        std::set_intersection(common_chars.begin(), common_chars.end(),
                              sack_three.begin(), sack_three.end(),
                              std::back_inserter(final_common_chars));
        for (char c : final_common_chars) {
            if (c >= 'a' && c <= 'z') {
                sum += (c - 'a' + 1);
            } else if (c >= 'A' && c <= 'Z') {
                sum += (c - 'A' + 27);
            }
        }
    }    
    std::cout << sum << std::endl;
}