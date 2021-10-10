/*=======================================
* @FileName: 4寻找两个正序数组的中位数.rs
* @Description: 
* @Author: TonyLaw
* @Date: 2021-10-11 00:06:58 Monday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
=========================================*/
/*=======================================
                (题目难度：困难)
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


=========================================*/
struct Solution;
use std::cmp::min;

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let min_left = (nums1.len() + nums2.len() + 1) / 2;
        let min_right = (nums1.len() + nums2.len() + 2) / 2;
        (find_k(&nums1, 0, &nums2, 0, min_left) + find_k(&nums1, 0, &nums2, 0, min_right)) as f64 / 2.0
    }
}

fn find_k(v1: &Vec<i32>, i: usize, v2: &Vec<i32>, j: usize, k: usize) -> i32 {
    // 当nums1 删除完， 则直接返回j + k - 1位置的数字，nums2 删完同理
    if i >= v1.len() {
        return v2[j + k - 1];
    }
    if j >= v2.len() {
        return v1[i + k - 1];
    }
    // 当k==1 时表示找最小的数字
    if k == 1 {
        return min(v1[i], v2[j]);
    }
    let max1 = if (i + k / 2 - 1) < v1.len() {v1[i + k/2 -1]} else {i32::MAX};
    let max2 = if (j + k/2 -1) < v2.len() {v2[j + k/2 -1]} else {i32::MAX};
    return if max1 > max2 {
        find_k(v1, i, v2, j + k/2, k - k/2)
    } else {
        find_k(v1, i + k/2, v2, j, k - k/2)
    };
} 

fn main() {
    let l1 = vec![1, 3];
    let l2 = vec![2];
    let result = Solution::find_median_sorted_arrays(l1, l2);
    println!("{:?}", result);
}