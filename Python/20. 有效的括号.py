# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 示例 1：
#
# 输入：s = "()"
# 输出：true
# 示例2：
#
# 输入：s = "()[]{}"
# 输出：true
# 示例3：
#
# 输入：s = "(]"
# 输出：false
# 示例4：
#
# 输入：s = "([)]"
# 输出：false
# 示例5：
#
# 输入：s = "{[]}"
# 输出：true
#
#
# 提示：
#
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成
#
#

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


if __name__ == '__main__':
    s1: str = "([])"
    instance = Solution()
    func = instance.isValid(s1)
    print(func)
