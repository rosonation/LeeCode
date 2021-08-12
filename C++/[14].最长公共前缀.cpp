//
// Created by Tony on 2021/8/12.
//
// [14].最长公共前缀（难度：简单）
// 编写一个函数来查找字符串数组中的最长公共前缀。
//
//如果不存在公共前缀，返回空字符串""。
//
//
//
//示例 1：
//
//输入：strs = ["flower","flow","flight"]
//输出："fl"
//示例 2：
//
//输入：strs = ["dog","racecar","car"]
//输出：""
//解释：输入不存在公共前缀。
//
//
//提示：
//
//1 <= strs.length <= 200
//0 <= strs[i].length <= 200
//strs[i] 仅由小写英文字母组成
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    static string longestCommonPrefix(vector<string> &strs) {
        if (!strs.size()) {
            return "";
        }
        string prefix = strs[0];  // 数组第一字符串
        int count = strs.size();  // 统计数组的元素总数,从0开始的话，循环就不能<=，只能是<,++i的意思是先加再使用，也就是i是1开始的
        for (int i = 0; i < count; ++i) {
            prefix = longestCommonPrefix(prefix, strs[i]); // 调用相同名字，不同参数的函数
            if (!prefix.size()) {  // 如果prefix的公共前缀为空就中断
                break;
            }
        }
        return prefix;   // 返回公共前缀
    }

    static string longestCommonPrefix(const string &str1, const string &str2) {
        int length = min(str1.size(), str2.size());  // 最长公共前缀肯定是以最短的那个字符串长度为计算单位
        int index = 0;  // 用来存储索引下标
        // 字符相等就说明找到了公共字符，继续增加索引下标，就是模拟了扫描，索引从0 -> length - 1
        while (index < length && str1[index] == str2[index]) {
            ++index;
        }
        return str1.substr(0, index);  // 公共前缀就是随便选择一个字符串来或者从01到index的值
    }
};

//int main(int argc, char *argv[]) {
//    vector<string> a = {"flower", "flow", "flight"};
//    Solution::longestCommonPrefix(a);
//    cout << Solution::longestCommonPrefix(a) << endl;
//}