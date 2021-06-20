# 9. 回文数
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
#
#
#
# 示例 1：
#
# 输入：x = 121
# 输出：true
# 示例2：
#
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3：
#
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
# 示例 4：
#
# 输入：x = -101
# 输出：false
#
#
# 提示：
#
# -231<= x <= 231- 1
#
#
# 进阶：你能不将整数转为字符串来解决这个问题吗？
#


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        # 特殊情况：
        # 如上所述，当 x < 0 时，x 不是回文数。
        # 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # 则其第一位数字也应该是 0
        # 只有 0 满足这一属性
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverte_number: int = 0
        while x > reverte_number:
            reverte_number = reverte_number * 10 + x % 10
            x //= 10
        return x == reverte_number or x == reverte_number // 10


if __name__ == '__main__':
    n1: int = 12321
    instance = Solution()
    func = instance.isPalindrome(n1)
    print(func)
