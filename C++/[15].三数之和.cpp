//
// Created by Tony on 2021/8/12.
//
// [15].三数之和 （难度：中等）
// 给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
//
//注意：答案中不可以包含重复的三元组。
//
//
//
//示例 1：
//
//输入：nums = [-1,0,1,2,-1,-4]
//输出：[[-1,-1,2],[-1,0,1]]
//示例 2：
//
//输入：nums = []
//输出：[]
//示例 3：
//
//输入：nums = [0]
//输出：[]
//
//
//提示：
//
//0 <= nums.length <= 3000
//-105 <= nums[i] <= 105
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    [[maybe_unused]] static vector<vector<int>> threeSum(vector<int> &nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        // 枚举 a
        for (int first = 0; first < n; ++first) {
            cout << "index:" << first << "; value:" << nums[first] << endl;
            // 需要和上次枚举的数不同
            if (first > 0 && nums[first] == nums[first - 1]) { // 排除了first = 0的可能性，所以first - 1可以等于0
                continue;
            }
            // c 对应的指针初始指向数组的最右端
            int third = n - 1; // 索引要减1，因为索引是从0开始的
            int target = -nums[first]; // first 值取反就是 second + third的值
            // 枚举 b
            for (int second = first + 1; second < n; ++second) {
                // 需要和上次枚举的数不相同
                if (second > first + 1 && nums[second] == nums[second - 1]) {// 排除了second=first+1的可能性，seconde可以等于first
                    continue;
                }
                // 需要保证b的指针在 c 的指针的左侧
                while (second < third && nums[second] + nums[third] > target) {
                    --third;
                }

                // 随着指针重合，随着 b 后续的增加
                // 就不会有满足 a+b+c=0 并且 b < c 的 c 了，可以退出循环
                if (second == third) {
                    break;
                }
                if (nums[second] + nums[third] == target) {
                    ans.push_back({nums[first], nums[second], nums[third]});
                    cout << "a ->" << nums[first] << "; b->" << nums[second] << "; c->" << nums[third] << endl;
                }
            }
        }
        return ans;
    }
};

// int main(int argc, char *argv[]) {
//     vector<int> a({-1, 0, 1, 2, -1, -4});
//     for (const auto &i : a)
//         cout << i << " ->";
//     cout << endl;
//     Solution::threeSum(a);
//     for (const auto &i : a)  // 声明i为指针，可以对i进行操作，也可以不声明为指针
//         cout << i << " ->";
//     cout << endl;
//     for (int i = 0; i < a.size(); i++)
//         std::cout << "index:" << i << " ->" << a[i] << ";";
// }