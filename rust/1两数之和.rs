/*=======================================
* @FileName: [1].两数之和.rs
* @Description: 
* @Author: TonyLaw
* @Date: 2021-08-26 03:02:33 Thursday
* @Copyright:  © 2021 TonyLaw. All Rights reserved.
=========================================*/
/*=======================================
                (题目难度：简单)
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
=========================================*/

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::with_capacity(nums.len());

        for i in 0..nums.len() {
            if let Some(k) = map.get(&(target - nums[i])) {
                if *k != i {
                    return vec![*k as i32, i as i32];
                }
            }
            map.insert(nums[i], i);
        }
        panic!("not found")
    }
}

fn main() {
    let l1 = vec![2, 3, 4];
    let i1 = 6;
    let result = Solution::two_sum(l1, i1);
    println!("{:?}", result);
}