/*=======================================
* @FileName: [1].两数之和.js
* @Description: 
* @Author: TonyLaw
* @Date: 2021-08-26 02:46:58 Thursday
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

// 哈希映射
var twoSum = function (nums, target) {
  let map = new Map()
  let len = nums.length
  for (let i = 0; i < len; ++i) {
    let key = target - nums[i]
    if (map.has(key)) {
      return [map.get(key), i]
    }
    map.set(nums[i], i)
  }
  throw Error("No two sum solution")
}

let l1 = [2, 7, 11, 15]
let i1 = 9
twoSum(l1, i1)
console.log(twoSum(l1, i1))