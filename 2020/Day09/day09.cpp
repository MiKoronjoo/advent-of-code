#include <iostream>
#include <vector>

#define ull unsigned long long

int main() {
    std::vector<ull> nums;
    int prl = 25;
    ull invalid;
    while (std::cin >> invalid)
        nums.push_back(invalid);
    bool bf;
    for (int i = prl; i < nums.size(); i++) {
        bf = false;
        for (int j = i - prl; j < i; j++) {
            for (int k = i - prl; k < i; k++)
                if (nums[j] + nums[k] == nums[i]) {
                    bf = true;
                    break;
                }
            if (bf) break;
        }
        if (bf) continue;
        invalid = nums[i];
        break;
    }
    std::cout << invalid << '\n';
    int i = 0, j = 1;
    invalid -= nums[i] + nums[j];
    while (invalid) {
        if (invalid >= nums[j + 1])
            invalid -= nums[++j];
        else
            invalid += nums[i++];
    }
    ull min, max;
    min = max = nums[i];
    for (int k = i + 1; k <= j; k++) {
        min = std::min(min, nums[k]);
        max = std::max(max, nums[k]);
    }
    std::cout << min + max << '\n';
}