/*=======================================
* @FileName: [18].四数之和.js
* @Description: 计算和 target 相等的不重复四元数组
* @Author: TonyLaw
* @Date: 2021-08-23 01:26:10 Monday
* @Copyright:  © 2021 TonyLaw. All rights reserved.
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
function fourSum(nums, target) {
  const quadruplets = []
  if (nums.length < 4) {
    return quadruplets
  }
  nums.sort((x, y) => x - y)
  const length = nums.length
  for (let i = 0; i < length - 3; ++i) {
    // 第一位数字必须是在倒数第四位的左边
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue
    }
    if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) {
      break // 从小到大排序后，最左面的连续四位数相加都比 target 大的话，说明没有四位数符合要求
    }
    if (nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target) {
      continue // 可以继续向右移动第一位数字找到四数之和等于 target 的
    }
    for (let j = i + 1; j < length - 2; ++j) {
      if (j > i + 1 && nums[j] === nums[j - 1]) {
        continue; // 有重复数字了
      }
      if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) {
        break; // 最左边的四数之和都比 target 大，后面没有比较的意义了，因为最左边的四数之和是 最小 的（排序后的）
      }
      if (nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target) {
        continue;
      }
      let left = j + 1, right = length - 1
      while (left < right) {
        const sum = nums[i] + nums[j] + nums[left] + nums[right];
        if (sum === target) {
          quadruplets.push([nums[i], nums[j], nums[left], nums[right]])
          while (left < right && nums[left] === nums[left + 1]) {
            left++; // 重复数字
          }
          left++; // 向右移动左指针
          while (left < right && nums[right] === nums[right - 1]) {
            right--
          }
          right--
        } else if (sum < target) {
          left++
        } else {
          right--
        }
      }
    }
  }
  return quadruplets;
}

let l1 = [-2, -1, -1, 1, 1, 2, 2]
let i1 = 0
fourSum(l1, i1)
console.log(fourSum(l1, i1))
