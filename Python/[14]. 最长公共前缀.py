# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串""。
#
#
#
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
# 提示：
#
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
#
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    @staticmethod
    def lcp(str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


if __name__ == '__main__':
    l1: List = ["flower", "flow", "flight"]
    instance = Solution()
    func = instance.longestCommonPrefix(l1)
    print(func)
