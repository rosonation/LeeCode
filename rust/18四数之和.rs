/*=======================================
* @FileName: 18四数之和.rs
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-01 23:10:39 Wednesday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
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
struct Solution;

impl Solution {
    pub fn four_sum(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let len = nums.len();
        if len < 4 {return vec![]};
        let mut ret = vec![];
        nums.sort_unstable();
        for i in 0..len - 3 {
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target { break; } //剪枝
            if nums[i] + nums[len - 3] + nums[len - 2] + nums[len - 1] < target { continue; } // 剪枝
            
            if i > 0 && nums[i] == nums[i - 1] { continue; } // 剪枝
            for j in i+1..len-2 {
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target { break; } // 剪枝
                if nums[i] + nums[j] + nums[len - 2] + nums[len - 1] < target { continue; } // 剪枝

                if j > i + 1 && nums[j] == nums[j - 1] {continue; }  // 剪枝
                let (mut k, mut q) = (j + 1, len - 1);                
                loop {
                    if k >= q { break; }
                    if nums[i] + nums[j] + nums[k] + nums[k + 1] > target { break; } // 剪枝
                    if nums[i] + nums[j] + nums[q - 1] + nums[q] < target { break; } // 剪枝
                    if k > j + 1 && nums[k] == nums[k - 1] { k += 1; continue; } // 剪枝
                    if q > len - 1 && nums[q] == nums[k + 1] { q -= 1; continue; } // 剪枝
                    let sum = nums[i] + nums[j] + nums[k] + nums[q];
                    if sum == target {
                        ret.push(vec![nums[i], nums[j], nums[k], nums[q]]);
                        k += 1;
                    } else if sum > target { 
                        q -= 1;
                    } else {
                        k += 1;
                    }
                }
            }
        }                 
        return ret
    }
}

fn main() {
    let l1 = vec![1, 0, -1, 0, -2, 2];
    let n1 = 0;
    let result = Solution::four_sum(l1, n1);
    println!("{:?}", result);
}