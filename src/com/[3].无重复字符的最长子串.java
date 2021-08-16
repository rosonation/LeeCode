// 3. 无重复字符的最长子串
// 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
//
//
//
//示例1:
//
//输入: s = "abcabcbb"
//输出: 3
//解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
//示例 2:
//
//输入: s = "bbbbb"
//输出: 1
//解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
//示例 3:
//
//输入: s = "pwwkew"
//输出: 3
//解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
//    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
//示例 4:
//
//输入: s = ""
//输出: 0
//


import java.util.HashSet;
import java.util.Set;

class Solution3 {
    public static int lengthOfLongestSubstring(String s) {
        // 哈希集合，备忘录记录每个字符是否出现过
        Set<Character> memo = new HashSet<>();
        int n = s.length();
        // 右指针， 初始值为-1，相当于我们在字符串的左边界的左侧， 还没有开始移动
        int rk = -1, ans = 0;
        for (int i = 0; i < n; ++i) {
            if (i != 0) {
                // 左指针右移一格， 移除一格字符
                memo.remove(s.charAt(i - 1));
            }
            while (rk + 1 < n && !memo.contains(s.charAt(rk + 1))) {
                // 不断移动右指针
                memo.add(s.charAt(rk + 1));
                ++rk;
            }
            // 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = Math.max(ans, rk - i + 1);
        }
        return ans;
    }

    public static void main(String[] args) {
        String s = "abcabcbb";
        Solution3.lengthOfLongestSubstring(s);
        System.out.println(Solution3.lengthOfLongestSubstring(s));
    }
}
