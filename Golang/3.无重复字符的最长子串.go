/*=======================================
* @FileName: 3.无重复字符的最长子串.go
* @Description: 
* @Author: TonyLaw
* @Date: 2021-09-06 01:55:22 Monday
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
package main

import "fmt"


func lengthOfLongestSubstring(s string) int {
	// 哈希集合， 记录每个字符是否出现过
	m := map[byte]int{}  // 元素全部初始化为 0，m[0] = 0, (m[a])m[97] = 0, (m[b])m[98] = 0, (m[c])m[99] = 0...m[255] = 0
	// fmt.Println("m[97]:", m[97])
	// fmt.Println("m[98]:", m[98])
	// fmt.Println("m[99]:", m[99])
	// fmt.Println("m[255]:", m[255])
	n := len(s)
	// 右指针，初始值为 -1 ，相当于我们在字符的左边界的左侧， 还没有开始移动
	rk, ans := -1, 0
	for i := 0; i < n; i++ { // i 为左指针
		fmt.Println("i: ->", i, "                         :<left pointer location>")
		if i != 0 {
			fmt.Println("--------<left> pointer deletes the duplicate element(", string(s[rk + 1]), ") for Loop---------")
			// 左指针向右移动一格，移除一个左边字符
			fmt.Println("rk + 1:", rk + 1, ";i - 1:", i - 1)
			fmt.Println("s[i - 1] ->", string(s[i - 1]), "=", s[i - 1], "              :<left pointer key>")
			fmt.Println("delete before m[s[i - 1]] : ->", m[s[i - 1]])
			// delete(map,key), 如果key存在，删除成功,如果key不存在，删除失败
			delete(m, s[i - 1])  // s[i - 1] 是需要删除的键
			fmt.Println("delete after m[s[i - 1]] : ->", m[s[i - 1]], " :<delete key(", string(s[i - 1]), ") of map>")
		}
		fmt.Println("s[rk + 1]: ->", string(s[rk + 1]), "=", s[rk + 1], "            :<right pointer key>")
		fmt.Println("before m[s[rk + 1]]: ->", m[s[rk + 1]], "       :<original value>")
		fmt.Println("before rk + 1: ->", rk + 1, "             :<right pointer location>")
		loop := 0
		// map[key]=value ,如果key存在，就修改数据, 如果key不存在，就添加数据
		for rk + 1 < n && m[s[rk + 1]] == 0 { // 因为 rk初始值为 -1，所以 rk + 1就可以看成是 s 的索引0 开始，向右移动
			// 不断的移动右指针
			fmt.Println("========<right> pointer assign value to distinct element(", string(s[rk + 1]), ") of character for Loop=========")
			loop += 1
			fmt.Println("Loop: ", loop, "(m[", s[rk + 1], "]++)")
			m[s[rk + 1]]++  // The increment statement i++ adds 1 to i ; it’s equivalent to i += 1 which is in turn equivalent to i = i + 1 . There’s a corresponding decrement statement i– that subtracts 1. These are statements, not expressions as the y are in most languages in the C family, so j = i++ is illegal, and the y are postfix only, so –i is not legal either.
			fmt.Println("m[a]=m[97]:", m[97])
			fmt.Println("m[b]=m[98]:", m[98])
			fmt.Println("m[c]=m[99]:", m[99])
			fmt.Println("s[rk + 1]: ->", string(s[rk + 1]), "=", s[rk + 1], "     :<right pointer key>")
			fmt.Println("after m[s[rk + 1]]: ->", m[s[rk + 1]], " :<set key(",string(s[rk + 1]), ") values(", m[s[rk + 1]], ")>")
			rk++  // 和上面的代码顺序不能颠倒，因为rk影响上面的数据
			fmt.Println("after rk + 1: ->", rk + 1, "       :<right pointer move right>")
		}
		// 第 i 到 rk 个字符是一个极长的无重复字符子串
		fmt.Println("-------End loop (", i, ") <left> pointer logic-------------------")
		ans = max(ans, rk - i + 1)
	}
	fmt.Println("no delete key(b):", m[98])
	return ans
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	s1 := "pwwkew"
	var result = lengthOfLongestSubstring(s1)
	fmt.Println(result)
}

// output results
/* i: -> 0                       :<left pointer location>
s[rk + 1]: -> a = 97             :<right pointer key>
before m[s[rk + 1]]: -> 0        :<original value>
before rk + 1: -> 0              :<right pointer location>
========<right> pointer assign value to distinct element( a ) of character for Loop=========
Loop:  1 (m[ 97 ]++)      // Go中的i++比较特别，是语句，不是表达式，因此不能赋值给另外的变量。此外没有++i和--i
m[a]=m[97]: 1             // m[97]++相当于给 m[97] += 1 ，也就是 m[97]=m[97] + 1, 因为开头初始化m[97]=0, 所以 m[97] = 0 + 1
m[b]=m[98]: 0
m[c]=m[99]: 0
s[rk + 1]: -> a = 97      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( a ) values( 1 )>
after rk + 1: -> 1        :<right pointer move right>
========<right> pointer assign value to distinct element( b ) of character for Loop=========
Loop:  2 (m[ 98 ]++)
m[a]=m[97]: 1
m[b]=m[98]: 1             //m[98]++相当于给 m[98] += 1 ，也就是 m[98]=m[98] + 1, 因为开头初始化m[98]=0, 所以 m[98] = 0 + 1 
m[c]=m[99]: 0
s[rk + 1]: -> b = 98      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( b ) values( 1 )>
after rk + 1: -> 2        :<right pointer move right>
========<right> pointer assign value to distinct element( c ) of character for Loop=========
Loop:  3 (m[ 99 ]++)
m[a]=m[97]: 1
m[b]=m[98]: 1
m[c]=m[99]: 1             //m[99]++相当于给 m[99] += 1 ，也就是 m[99]=m[99] + 1, 因为开头初始化m[99]=0, 所以 m[99] = 0 + 1
s[rk + 1]: -> c = 99      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( c ) values( 1 )>
after rk + 1: -> 3        :<right pointer move right>
-------End loop ( 0 ) <left> pointer logic-------------------
i: -> 1                          :<left pointer location>
--------<left> pointer deletes the duplicate element( a ) for Loop---------
rk + 1: 3 ;i - 1: 0
s[i - 1] -> a = 97               :<left pointer key>
delete before m[s[i - 1]] : -> 1
delete after m[s[i - 1]] : -> 0  :<delete key( a ) of map>
s[rk + 1]: -> a = 97             :<right pointer key>
before m[s[rk + 1]]: -> 0        :<original value>
before rk + 1: -> 3              :<right pointer location>
========<right> pointer assign value to distinct element( a ) of character for Loop=========
Loop:  1 (m[ 97 ]++)
m[a]=m[97]: 1
m[b]=m[98]: 1
m[c]=m[99]: 1
s[rk + 1]: -> a = 97      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( a ) values( 1 )>
after rk + 1: -> 4        :<right pointer move right>
-------End loop ( 1 ) <left> pointer logic-------------------
i: -> 2                          :<left pointer location>
--------<left> pointer deletes the duplicate element( b ) for Loop---------
rk + 1: 4 ;i - 1: 1
s[i - 1] -> b = 98               :<left pointer key>
delete before m[s[i - 1]] : -> 1
delete after m[s[i - 1]] : -> 0  :<delete key( b ) of map>
s[rk + 1]: -> b = 98             :<right pointer key>
before m[s[rk + 1]]: -> 0        :<original value>
before rk + 1: -> 4              :<right pointer location>
========<right> pointer assign value to distinct element( b ) of character for Loop=========
Loop:  1 (m[ 98 ]++)
m[a]=m[97]: 1
m[b]=m[98]: 1
m[c]=m[99]: 1
s[rk + 1]: -> b = 98      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( b ) values( 1 )>
after rk + 1: -> 5        :<right pointer move right>
-------End loop ( 2 ) <left> pointer logic-------------------
i: -> 3                          :<left pointer location>
--------<left> pointer deletes the duplicate element( c ) for Loop---------
rk + 1: 5 ;i - 1: 2
s[i - 1] -> c = 99               :<left pointer key>
delete before m[s[i - 1]] : -> 1
delete after m[s[i - 1]] : -> 0  :<delete key( c ) of map>
s[rk + 1]: -> c = 99             :<right pointer key>
before m[s[rk + 1]]: -> 0        :<original value>
before rk + 1: -> 5              :<right pointer location>
========<right> pointer assign value to distinct element( c ) of character for Loop=========
Loop:  1 (m[ 99 ]++)
m[a]=m[97]: 1
m[b]=m[98]: 1
m[c]=m[99]: 1
s[rk + 1]: -> c = 99      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( c ) values( 1 )>
after rk + 1: -> 6        :<right pointer move right>
-------End loop ( 3 ) <left> pointer logic-------------------
i: -> 4                          :<left pointer location>
--------<left> pointer deletes the duplicate element( b ) for Loop---------
rk + 1: 6 ;i - 1: 3
s[i - 1] -> a = 97               :<left pointer key>
delete before m[s[i - 1]] : -> 1
delete after m[s[i - 1]] : -> 0  :<delete key( a ) of map>
s[rk + 1]: -> b = 98             :<right pointer key>
before m[s[rk + 1]]: -> 1        :<original value>
before rk + 1: -> 6              :<right pointer location>
-------End loop ( 4 ) <left> pointer logic-------------------
i: -> 5                          :<left pointer location>
--------<left> pointer deletes the duplicate element( b ) for Loop---------
rk + 1: 6 ;i - 1: 4
s[i - 1] -> b = 98               :<left pointer key>
delete before m[s[i - 1]] : -> 1
delete after m[s[i - 1]] : -> 0  :<delete key( b ) of map>
s[rk + 1]: -> b = 98             :<right pointer key>
before m[s[rk + 1]]: -> 0        :<original value>
before rk + 1: -> 6              :<right pointer location>
========<right> pointer assign value to distinct element( b ) of character for Loop=========
Loop:  1 (m[ 98 ]++)
m[a]=m[97]: 0
m[b]=m[98]: 1
m[c]=m[99]: 1
s[rk + 1]: -> b = 98      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( b ) values( 1 )>
after rk + 1: -> 7        :<right pointer move right>
-------End loop ( 5 ) <left> pointer logic-------------------
i: -> 6                          :<left pointer location>
--------<left> pointer deletes the duplicate element( b ) for Loop---------
rk + 1: 7 ;i - 1: 5
s[i - 1] -> c = 99               :<left pointer key>
delete before m[s[i - 1]] : -> 1
delete after m[s[i - 1]] : -> 0  :<delete key( c ) of map>
s[rk + 1]: -> b = 98             :<right pointer key>
before m[s[rk + 1]]: -> 1        :<original value>
before rk + 1: -> 7              :<right pointer location>
-------End loop ( 6 ) <left> pointer logic-------------------
i: -> 7                          :<left pointer location>
--------<left> pointer deletes the duplicate element( b ) for Loop---------
rk + 1: 7 ;i - 1: 6
s[i - 1] -> b = 98               :<left pointer key>
delete before m[s[i - 1]] : -> 1
delete after m[s[i - 1]] : -> 0  :<delete key( b ) of map>
s[rk + 1]: -> b = 98             :<right pointer key>
before m[s[rk + 1]]: -> 0        :<original value>
before rk + 1: -> 7              :<right pointer location>
========<right> pointer assign value to distinct element( b ) of character for Loop=========
Loop:  1 (m[ 98 ]++)
m[a]=m[97]: 0
m[b]=m[98]: 1
m[c]=m[99]: 0
s[rk + 1]: -> b = 98      :<right pointer key>
after m[s[rk + 1]]: -> 1  :<set key( b ) values( 1 )>
after rk + 1: -> 8        :<right pointer move right>
-------End loop ( 7 ) <left> pointer logic-------------------
no delete key(b): 1
3 */