#include <iostream>
#include <vector>
#include <unordered_map>

#define LAST_TURN 30000000
std::vector<int> lst;
std::unordered_map<int, int> mem;


int main() {
    lst.reserve(LAST_TURN);
    int n;
    char _;
    while (std::cin >> n >> _)
        lst.push_back(n);
    lst.push_back(n);
    for (int i = 0; i < lst.size() - 1; i++)
        mem[lst[i]] = i;
    while (lst.size() != LAST_TURN) {
        int last = lst.back();
        auto itr = mem.find(last);
        if (itr == mem.end())
            lst.push_back(0);
        else
            lst.push_back(lst.size() - 1 - itr->second);
        mem[last] = lst.size() - 2;
    }
    std::cout << lst[2019] << '\n' << lst.back() << '\n';
}