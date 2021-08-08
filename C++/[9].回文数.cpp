//
// Created by Tony on 2021/8/8.
//
// [9].回文数
// 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
//
//回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
//
//
//
//示例 1：
//
//输入：x = 121
//输出：true
//示例2：
//
//输入：x = -121
//输出：false
//解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
//示例 3：
//
//输入：x = 10
//输出：false
//解释：从右向左读, 为 01 。因此它不是一个回文数。
//示例 4：
//
//输入：x = -101
//输出：false
//
//
//提示：
//
//-231<= x <= 231- 1
//
//
#include <iostream>
using namespace std;

class Solution {
public:
    static bool isPalindrome(int x) {
        // 特殊情况：
        // 如上所述 ，当 x < 0 时， x 不是回文数
        // 同样的， 如果数字的最后一位是0，为了使该数字为回文，则其第一位也必须为0
        // 只有0能满足这个条件
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        // 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        // 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        // 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == revertedNumber || x == revertedNumber / 10;
    }
};

//int main(int argc, char *argv[]) {
//    const int i1 = 123;
//    Solution::isPalindrome(i1);
//    cout << Solution::isPalindrome(i1) << endl;
//}