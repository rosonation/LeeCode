/*=======================================
* @FileName: [18].四数之和.cpp
* @Description: 从一个数组中找出和target相等的不重复的四元组
* @Author: TonyLaw
* @Date: 2021-08-21 16:17:07 Saturday
=========================================*/
/*=======================================
                (题目难度：中等)
给你一个由 n 个整数组成的数组 sums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [sums[a], sums[b], sums[c], sums[d]] ：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
sums[a] + sums[b] + sums[c] + sums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：sums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：sums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= sums.length <= 200
-109 <= sums[i] <= 109
-109 <= target <= 109

=========================================*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    static vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> quadruplets;
        if (nums.size() < 4) {
            return quadruplets;
        }
        sort(nums.begin(), nums.end());
        int length = nums.size();
        for (int i = 0; i < length - 3; ++i){
            if (i > 0 && nums[i] == nums[i - 1]) { // 如果元素相等就下一个
                continue;
            }
            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target){
                break; // 已经从小到大排了序的四个数字之和都大于 target ，说明没有符合要求的四元数组
            }
            if (nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target) { // 从小到大排序，如果第一个和最后面三个数相加都比 target 小，说明没有符合要求的四元数组
                continue; // 继续加大第一位数字，看看能否找到
            }
            for (int j = i + 1; j < length - 2; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) {
                    break;
                }
                if (nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target) {
                    continue;
                }
                int left = j + 1, right = length - 1;  // 定义双指针,第三和第四个数字,代表了最左边和最右边
                while (left < right) {  // 左指针要比有指针小，左右指针是逻辑上的概念，左右指针定义了左指针比右指针小
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target){
                        quadruplets.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[left] == nums[left + 1]) {
                            left++;  // 如果左指针和相邻的右数字相等，左指针向右移动一位
                        }
                        left++;  // 找到了一个让sum==target的第三个数字，还可能有其他第三个数字，所以继续向右移动左指针
                        while (left < right && nums[right] == nums[right - 1]) {
                            right--;  // 如果有指针和相邻的左数字相等，右指针向左移动一位
                        }
                        right--;  // 继续向左移动右指针，找让sum == target的第四个数字
                    } else if (sum < target)  {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return quadruplets;
    }
};

int main(int argc, char *argv[]) {
    vector<int> a({1, 0, -1, 0, -2, -1});
    int i2 = 0;
    Solution::fourSum(a, i2);
    for (auto &i : Solution::fourSum(a, i2)) {
        for (auto &j : i) {
            cout << j << " ->";
        }
    }
    cout << endl;
    return 0;
}