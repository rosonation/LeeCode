cmake_minimum_required(VERSION 3.20)
project(LeeCode)

set(CMAKE_CXX_STANDARD 14)
set(SOURCE_FILES 最长回文子串.cpp 最长回文子串.h)
include_directories(C++)

add_executable(LeeCode
        C++/1.twoSum.cpp
        C++/1.twoSum.hpp
        C++/2.addTwoNumbers.cpp
        C++/2.addTwoNumbers.hpp
        C++/3.无重复字符的最长子串.cpp
        C++/3.无重复字符的最长子串.hpp
        C++/4.寻找两个正序数组的中位数.cpp
        C++/4.寻找两个正序数组的中位数.hpp
        C++/最长回文子串.cpp
        C++/最长回文子串.h
        )
