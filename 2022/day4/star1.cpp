#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
int main() 
{
    std::ifstream input("input.txt");
    std::string line;
    int sum = 0, a, b, x, y;
    while(getline(input, line)) 
    {
        std::stringstream ss(line);
        char c;
        ss >> a >> c >> b >> c >> x >> c >> y;

        sum+=(a<=x && b>=y) || (x<=a && y>=b);

    }
    std::cout << sum << std::endl;
}