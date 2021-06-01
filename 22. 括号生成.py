# 22. 括号生成
# 数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
#
# 提示：
#
# 1 <= n <= 8
#
# 方法二：回溯法
#
# 思路和算法
#
# 方法一还有改进的余地：我们可以只在序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。
# 我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
#
# 如果左括号数量不大于
# n
# n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。
#
from typing import List


class Solution:
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            # 括号是成对出现的，所有是两倍
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == '__main__':
    i1: int = 3
    instance = Solution()
    func = instance.generateParenthesis(i1)
    print(func)
