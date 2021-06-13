# 18. 四数之和
# 给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，
# 使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。
#
# 注意：答案中不可以包含重复的四元组。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 示例 2：
#
# 输入：nums = [], target = 0
# 输出：[]
#
#
# 提示：
#
# 0 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109
#
#
from typing import List


class Solution:
    @staticmethod
    def fourSum(nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        quadruplets = list()
        if not nums or length < 4:
            return quadruplets

        # 枚举 a
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            # 枚举 b
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                # define c and d
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets


if __name__ == '__main__':
    l1: list = [1, 0, -1, 0, -2, 2]
    i1: int = 0
    instance = Solution()
    func = instance.fourSum(l1, i1)
    print(func)
