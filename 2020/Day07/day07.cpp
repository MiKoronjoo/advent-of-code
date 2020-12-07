#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>

std::map<std::string, bool> visited;
std::map<std::string, std::vector<std::string>> parents;
std::map<std::string, std::vector<std::pair<std::string, int>>> children;

int part1(const std::string &ch) {
    int res = 0;
    for (const auto &par: parents[ch])
        if (not visited[par]) {
            visited[par] = true;
            res += 1 + part1(par);
        }
    return res;
}

int part2(const std::string &par) {
    int res = 0;
    for (const auto &ch: children[par])
        res += ch.second + ch.second * part2(ch.first);
    return res;
}


int main() {
    std::string line, p1, p2, _, c1, c2;
    int n;
    while (std::getline(std::cin, line)) {
        std::stringstream ss;
        ss << line;
        ss >> p1 >> p2 >> _ >> _;
        p1 += " " + p2;
        visited[p1] = false;
        while (ss >> n >> c1 >> c2 >> _) {
            c1 += " " + c2;
            parents[c1].push_back(p1);
            children[p1].push_back({c1, n});
        }
    }
    std::string bag = "shiny gold";
    std::cout << part1(bag) << '\n' << part2(bag) << '\n';
    return 0;
}
