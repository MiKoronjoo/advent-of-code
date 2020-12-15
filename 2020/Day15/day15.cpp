#include <iostream>
#include <unordered_map>

#define LAST_TURN 30000000
std::unordered_map<int, int> mem;


int main() {
    mem.reserve(LAST_TURN);
    int n, i{};
    char _;
    while (std::cin >> n >> _)
        mem[n] = i++;
    mem[n] = i;
    int tmp, last = n;
    while (++i != LAST_TURN) {
        if (i == 2020)
            std::cout << last << '\n';
        auto itr = mem.find(last);
        tmp = last;
        if (itr == mem.end())
            last = 0;
        else
            last = i - 1 - itr->second;
        mem[tmp] = i - 1;
    }
    std::cout << last << '\n';
}