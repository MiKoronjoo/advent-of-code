#include <iostream>
#include <string>

int main() {
    int a, b, res1{}, res2{};
    char let, _;
    std::string pass;
    while (std::cin >> a >> _ >> b >> let >> _ >> pass) {
        int count = 0;
        for (char c : pass)
            count += c == let;
        res1 += a <= count and count <= b
        res2 += pass[a - 1] == let xor pass[b - 1] == let
    }
    std::cout << res1 << '\n' << res2 << '\n';
    return 0;
}
