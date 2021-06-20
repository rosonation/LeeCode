# 16. 最接近的三数之和
# 给定一个包括n 个整数的数组nums和 一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。
# 返回这三个数的和。假定每组输入只存在唯一答案。
#
#
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
# 提示：
#
# 3 <= nums.length <= 10^3
# -10^3<= nums[i]<= 10^3
# -10^4<= target<= 10^4
#

from typing import List


class Solution:
    @staticmethod
    def threeSumClosest(nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举 a
        for i in range(n):
            # 保证和上次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target， 移动 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return best


if __name__ == '__main__':
    l1: List = [-1, 2, 1, -4]
    i1: int = 1
    instance = Solution()
    func = instance.threeSumClosest(l1, i1)
    print(func)
