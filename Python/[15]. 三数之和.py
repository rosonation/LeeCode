# 15. 三数之和
# 给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
#
# 输入：nums = []
# 输出：[]
# 示例 3：
#
# 输入：nums = [0]
# 输出：[]
#
#
# 提示：
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#
#
from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上次枚举的数不一样
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上次枚举的数不一样
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a + b + c = 0 并且 b < c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


if __name__ == '__main__':
    l1: List = [-1, 0, 1, 2, -1, -4]
    instance = Solution()
    func = instance.threeSum(l1)
    print(func)
