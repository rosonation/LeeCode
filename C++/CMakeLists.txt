cmake_minimum_required(VERSION 3.20)
project(LeeCode)

set(CMAKE_CXX_STANDARD 17)

include_directories(.)

add_executable(LeeCode
        1.twoSum.cpp
        2.addTwoNumbers.cpp
        3.无重复字符的最长子串.cpp
        4.寻找两个正序数组的中位数.cpp
        ZigZagConversion.cpp
        最长回文子串.cpp ReverseInteger.cpp)