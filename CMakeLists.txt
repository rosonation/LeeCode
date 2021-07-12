cmake_minimum_required(VERSION 3.20)
project(LeeCode)

set(CMAKE_CXX_STANDARD 14)

set(SOURCE_FILES
        C++/1.twoSum.hpp
        C++/1.twoSum.cpp
        C++/最长回文子串.cpp
        C++/最长回文子串.h)

include_directories(C++)

add_executable(LeeCode ${SOURCE_FILES})