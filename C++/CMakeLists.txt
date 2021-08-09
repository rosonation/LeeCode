cmake_minimum_required(VERSION 3.20)
#project name
project(LeeCode)
#set environment variable
set(CMAKE_CXX_STANDARD 20)

include_directories(.)
#add executable file
add_executable(C++
        [1].两数之和.cpp
        [2].两数相加.cpp
        [3].无重复字符的最长子串.cpp
        [4].寻找两个正序数组的中位数.cpp
        [6].Z字形变换.cpp
        [5].最长回文子串.cpp [7].整数反转.cpp [8].字符串转换整数.cpp [9].回文数.cpp [10].正则表达式匹配.cpp [11].盛最多水的容器.cpp)