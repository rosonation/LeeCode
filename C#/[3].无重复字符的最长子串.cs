/*=======================================
* @FileName: [3].无重复字符的最长子串.cs
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-06 01:20:44 Monday
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
using System;

namespace LeetCode
{
    public class Solution
    {
        public int LengthOfLongestSubstring(string s)
        {
            int[] last = new int[128];
            for (int i = 0; i < last.Length; ++i)
            {
                last[i] = -1;  // 初始化 变量 last
            }
            int left = -1;
            int ans = 0;
            for (int i = 0; i < s.Length; ++i)
            {
                // Console.Write("i:" + i + " ->");
                // Console.Write("s[" + i + "]:" + s[i] + " ->");
                // Console.Write("before set last[" +s[i] + "]:" + last[s[i]] + " ->");
                // Console.Write("before set left:" + left + " ->");
                left = Math.Max(left, last[s[i]]);  // left 是左指针， last[s[i]] 出现重复的字符的索引
                // Console.Write("after set left:" + left + " ->");
                last[s[i]] = i;  // 更新 last[s[i]] 的字符出现的索引位置
                // Console.Write("after set last[" +s[i] + "]:" + last[s[i]] + " ->");
                ans = Math.Max(ans, i - left);  // 取重复字符最大公约数（重复字符的最大长度） ， i是右指针， left是左指针，相差就是重复的字符长度
                // Console.WriteLine("ans:" + ans + " ->");
                // Console.WriteLine(last[s[0]] + " ->" + last[s[1]] + " ->" +last[s[2]] + " ->" +last[s[3]] + " ->" +last[s[4]] + " ->" +last[s[5]] + " ->" +last[s[6]] + " ->" +last[s[7]]);
            }
            return ans;
        }
    

        static void Main(string[] args)
        {
            string s1 = "abcabcbb";
            Solution so = new Solution();
            var target = so.LengthOfLongestSubstring(s1);
            Console.WriteLine(target);
        }
    }
}