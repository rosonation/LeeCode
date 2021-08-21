/*=======================================
* @FileName: [17].电话号码的字母组合.java
* @Description: 计算电话号码上9位数字的字母组合情况
* @Author: TonyLaw
* @Date: 2021-08-21 00:42:56 Saturday
=========================================*/

/*====================================

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 

提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

======================================*/
package com.rosonation.java;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;

class Solution17 {
    public static List<String> letterCombinations(String digits) {
        List<String> combinations = new ArrayList<String>();
        if (digits.length() == 0) {
            return combinations;
        }
        Map<Character, String> phoneMap = new HashMap<Character, String>(){{
            put('2', "abc");
            put('3', "def");
            put('4', "ghi");
            put('5', "jkl");
            put('6', "mno");
            put('7', "pqrs");
            put('8', "tuv");
            put('9', "wxyz");
        }};
        backtrack(combinations, phoneMap, digits, 0, new StringBuilder());  // 递归digits的索引 digits_index,索引都是默认从 0 开始的
        return combinations;
    }
        public static void backtrack(List<String> combinations, Map<Character, String> phoneMap, String digits, int digits_index, StringBuilder combination) {
            if (digits_index == digits.length()) {
                combinations.add(combination.toString());
            }
            else {
                char digit = digits.charAt(digits_index);
                String letters = phoneMap.get(digit);
                int lettersCount = letters.length();
                for (int letters_index = 0; letters_index < lettersCount; ++letters_index) {
                    combination.append(letters.charAt(letters_index));
                    backtrack(combinations, phoneMap, digits, digits_index + 1, combination); // digits_index + 1,遍历下一个索引，也就是指针移动
                    combination.deleteCharAt(digits_index);
                }
            }
        }
        public static void main(String[] args) {
            String s1 = "23";
            Solution17.letterCombinations(s1);
            System.out.println(Solution17.letterCombinations(s1));
        }
}