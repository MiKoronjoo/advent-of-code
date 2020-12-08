#include <utility>
#include <iostream>
#include <string>
#include <vector>

struct Line {
    std::string opr;
    int arg;
    bool visited = false;

    Line(std::string opr, int arg) : opr(std::move(opr)), arg(arg) {}
};

std::vector<Line> lines;

int rec(int i = 0, int acc = 0, bool use = false) {
    if (i >= lines.size())
        return acc;
    if (lines[i].visited)
        return 0;
    int res, tmp;
    lines[i].visited = true;
    if (lines[i].opr == "acc")
        res = rec(i + 1, acc + lines[i].arg, use);
    else if (lines[i].opr == "nop") {
        tmp = rec(i + 1, acc, use);
        res = tmp ? tmp : (not use ? rec(i + lines[i].arg, acc, true) : 0);
    } else {
        tmp = rec(i + lines[i].arg, acc, use);
        res = tmp ? tmp : (not use ? rec(i + 1, acc, true) : 0);
    }
    lines[i].visited = false;
    return res;
}

int main() {
    std::string opr;
    int arg, acc{}, i{};
    while (std::cin >> opr >> arg)
        lines.emplace_back(opr, arg);
    while (not lines[i].visited) {
        lines[i].visited = true;
        if (lines[i].opr == "acc") {
            acc += lines[i].arg;
            i++;
        } else if (lines[i].opr == "nop")
            i++;
        else
            i += lines[i].arg;
    }
    for (auto &line: lines)
        line.visited = false;
    std::cout << acc << '\n' << rec() << '\n';
}