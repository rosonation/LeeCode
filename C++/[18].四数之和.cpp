/*=======================================
* @FileName: [18].四数之和.cpp
* @Description: 从一个数组中找出和target相等的不重复的四元组
* @Author: TonyLaw
* @Date: 2021-08-21 16:17:07 Saturday
=========================================*/
/*=======================================
                (题目难度：中等)
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] ：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

=========================================*/
#include <iostream>
#include <List>
#include <Integer>
using namespace std;

class Solution {
public:
    static List<List<Integer>> fourSum(int[] sums, int targets) {
        
    }
};

int main(int argc, char *argv[]) {
    int[] i1 = {1, 0, -1, 0, -2, -1};
    int i2 = 0;
    Solution::fourSum(i1, i2);
    cout << Solution::fourSum(i1, i2) << endl;
    return 0;
}
