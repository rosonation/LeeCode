/*=======================================
* @FileName: [3].无重复字符的最长子串.swift
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-21 22:44:48 Tuesday
* @Copyright:  © 2021 TonyLaw. All Rights Reserved.
=========================================*/
/*=======================================
                (题目难度：中等)
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成


=========================================*/
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        if (s.count == 0) {
            return 0
        }
        var last = Array(repeating: -1, count: 128)
        var left = -1
        var ans = 0
        let unicode = s.unicodeScalars.map{Int($0.value)}
        for i in 0...(unicode.count - 1) {
            left = max(left, last[unicode[i]])
            last[unicode[i]] = i
            ans = max(ans, i - left)
        }
        return ans
    }
}

var s = "abcabcbb"
var result = Solution().lengthOfLongestSubstring(s)
print(result)