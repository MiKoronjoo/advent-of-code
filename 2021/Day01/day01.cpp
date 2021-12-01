#include <iostream>
#include <vector>

std::vector<int> nums;

int main() {
    int temp, ans1 = 0, ans2 = 0;
    while (std::cin >> temp)
        nums.push_back(temp);
    for (int i = 0; i < nums.size() - 1; i++) {
        ans1 += nums[i] < nums[i + 1];
        ans2 += (i + 3 < nums.size()) and (nums[i] + nums[i + 1] + nums[i + 2] < nums[i + 1] + nums[i + 2] + nums[i + 3]);
    }
    std::cout << ans1 << '\n' << ans2 << '\n';
}
