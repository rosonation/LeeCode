cmake_minimum_required(VERSION 3.20)
#project name
project(LeeCode)
#set environment variable
set(CMAKE_CXX_STANDARD 17)

include_directories(.)
#add executable file
add_executable(LeeCode
        [1].twoSum.cpp
        [2].addTwoNumbers.cpp
        [3].无重复字符的最长子串.cpp
        [4].寻找两个正序数组的中位数.cpp
        [6].ZigZagConversion.cpp
        [5].最长回文子串.cpp [7].ReverseInteger.cpp)