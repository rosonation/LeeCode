/* =======================================
 * @FileName: [18].四数之和.swift
 * @Description: 找出和 target 相等的不重复四元数组
 * @Author: TonyLaw
 * @Date: 2021-08-22 23:22:09 Sunday
 * @Copyright:  © 2021 TonyLaw. All rights reserved.
 ========================================= */
class Solution {
    func fourSum(_ nums: [Int], _ target: Int) -> [[Int]] {
        guard nums.count >= 4 else {
            return []
        }
        let sorted = nums.sorted()
        let count = sorted.count
        var arr = [[Int]]()
        for i in 0 ..< count - 3 { // i 必须是小于第三个
            if i > 0, sorted[i] == sorted[i - 1] {
                continue // 出现了重复数字
            }
            guard sorted[i] + sorted[i + 1] + sorted[i + 2] + sorted[i + 3] <= target else {
                break // 最小的四位数都大于 target ，说明没有找到符合的四元数组
            }
            for j in i + 1 ..< count - 2 {
                if j > i + 1, sorted[j] == sorted[j - 1] { // j 最小是第二位数，所以和左边的数来比较
                    continue
                }
                guard sorted[i] + sorted[j] + sorted[count - 1] + sorted[count - 2] >= target else {
                    continue // 因为最左边两位数 加上 最右边两位数 都比 target 小了，说明没有找到符合要求的四元数组
                }
                guard sorted[i] + sorted[j] + sorted[j + 1] + sorted[j + 2] <= target else {
                    break
                }
                var left = j + 1, right = count - 1
                while left < right {
                    let sum = sorted[i] + sorted[j] + sorted[left] + sorted[right]
                    if sum == target {
                        arr.append([sorted[i], sorted[j], sorted[left], sorted[right]])
                        while left < right, sorted[left] == sorted[left + 1] { // 因为left 是从最左边向右移动，和它的右边比较大小
                            left += 1 // 遇到了重复的两个数字
                        }
                        while left < right, sorted[right] == sorted[right - 1] { // 因为right是从最右边向左移动，所以和左边的比较
                            right -= 1
                        }
                        left += 1
                        right -= 1
                    } else if sum > target {
                        right -= 1
                    } else if sum < target {
                        left += 1
                    }
                }
            }
        }
        return arr
    }
}

let a = [-5,-2,-4,-2,-5,-4,0,0]
let b: Int = -13
var c: [[Int]] = Solution().fourSum(a, b)
print(c)
