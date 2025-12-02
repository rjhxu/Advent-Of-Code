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
        std::string first_half = line.substr(0, line.size() / 2);
        std::string second_half = line.substr(line.size() / 2);
        std::set<char> chars_in_first(first_half.begin(), first_half.end());
        std::set<char> chars_in_second(second_half.begin(), second_half.end());
        std::vector<char> common_chars;
        std::set_intersection(chars_in_first.begin(), chars_in_first.end(),
                              chars_in_second.begin(), chars_in_second.end(),
                              std::back_inserter(common_chars));
        for (char c : common_chars) {
            if (c >= 'a' && c <= 'z') {
                sum += (c - 'a' + 1);
            } else if (c >= 'A' && c <= 'Z') {
                sum += (c - 'A' + 27);
            }
        }
    }    
    std::cout << sum << std::endl;
}