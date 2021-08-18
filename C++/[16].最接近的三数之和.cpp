/*
 * @Author: TonyLaw
 * @Date: 2021-08-18 00:29:24
 * @LastEditTime: 2021-08-18 01:58:39
 * @LastEditors: Please set LastEditors
 * @Description: 1.0
 * @FilePath: /LeeCode/C++/[16].最接近的三数之和
 */
//

// [16].最接近的三数之和 （难度：中等）
//给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
//
//示例：
//
//输入：nums = [-1,2,1,-4], target = 1
//输出：2
//解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
// 
//提示：

//3 <= nums.length <= 10^3
//-10^3 <= nums[i] <= 10^3
// -10^4 <= target <= 10^4

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    static int threeSumClosest(vector<int> &nums, int target)
    {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int best = 1e7;

        // 根据差值的绝对值来更新答案
        auto update = [&](int cur)
        {
            if (abs(cur - target) < abs(best - target))
            {
                best = cur;
            }
        };

        // 枚举 a
        for (int i = 0; i < n; ++i)
        {
            // 保证和上一次枚举的元素不相等
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            // 使用双指针枚举 b 和 c
            int j = i + 1, k = n - 1; // 索引比长度小1，因为索引是从0开始的
            while (j < k)
            {
                int sum = nums[i] + nums[j] + nums[k];
                // 如果和为 target 直接返回答案
                if (sum == target)
                {
                    return target;
                }
                update(sum);
                if (sum > target)
                {
                    // 如果和大于 target ，移动 c 对应的指针k，让三数之和变小
                    int k0 = k - 1; // 先定义 c 指针的左边指针k0，到时候要覆盖 c 对应的指针k
                    // 向左移动到下一个不相等的元素
                    while (j < k0 && nums[k0] == nums[k])
                    { // 比较 c 和 c - 1指针的值是否一致
                        --k0;
                    }
                    k = k0; // 更新 k 指针的值，也就是 k 指针向左移动到的位置
                }
                else
                {
                    // 如果和小于 target ， 移动 b 对应的指针j
                    int j0 = j + 1; // 先定义 b 指针对应的指针j 的右边指针j0，到时候要覆盖 b 的对应指针j
                    // 向右移动到下一个不相等的元素
                    while (j0 < k && nums[j0] == nums[j])
                    {
                        ++j0;
                    }
                    j = j0; // 更新 j 指针的值，也就是 j 指针向右移动到的位置
                }
            }
        }
        return best;
    }
};

int main(int argc, char *argv[]) {
   vector<int> b({-1, 2, 1, -4});
   int i1 = 1;
   Solution::threeSumClosest(b, i1);
   cout << Solution::threeSumClosest(b, i1) << endl;
}