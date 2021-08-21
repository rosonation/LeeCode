/*=======================================
* @FileName: [17].电话号码的字母组合.cpp
* @Description: 显示电话号码上面数字的字母组合有哪些，建议使用回溯算法
* @Author: TonyLaw
* @Date: 2021-08-21 11:55:32 Saturday
=========================================*/
/*=======================================
                (题目难度：中等)
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

=========================================*/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    static vector<string> letterCombinations(string digits)
    {
        vector<string> combinations;
        if (digits.empty())
        {
            return combinations;
        }
        unordered_map<char, string> phoneMap{
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"},
        };
        string combination;
        backtrack(combinations, phoneMap, digits, 0, combination);
        return combinations;
    }
    static void backtrack(vector<string>& combinations, const unordered_map<char, string>& phoneMap, const string& digits, int digits_index, string& combination){
        if (digits_index == digits.length()) {
            combinations.push_back(combination);
        } else {
            char digit = digits[digits_index];
            const string& letters = phoneMap.at(digit);
            for(auto &letter : letters)
            {
                combination.push_back(letter);
                backtrack(combinations, phoneMap, digits, digits_index, combination);
                combination.pop_back();
            }
        }
    }
};

int main(int argc, char *argv[])
{
    string s1 = "23";
    Solution::letterCombinations(s1);
    for (auto &i : Solution::letterCombinations(s1))
    {
        cout << i << " ->";
    }
    cout << "hello";
    return 0;
}
