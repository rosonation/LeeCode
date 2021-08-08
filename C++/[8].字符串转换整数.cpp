//
// Created by Tony on 2021/8/8.
//

#include <iostream>
#include <cctype>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Automaton {
    string state = "start";
    unordered_map<string, vector<string>> table = {
            /* '', '+-', number, other */
            {"start",     {"start", "signed", "in_number", "end"}},
            {"signed",    {"end",   "end",    "in_number", "end"}},
            {"in_number", {"end",   "end",    "in_number", "end"}},
            {"end",       {"end",   "end",    "end",       "end"}}
    };

    static int get_col(char c) {
        if (isspace(c)) return 0;
        if (c == '+' or c == '-') return 1;
        if (isdigit(c)) return 2;
        return 3;
    }

public:
    int sign = 1;
    long long ans = 0;

    void get(char c) {
        state = table[state][get_col(c)];
        if (state == "in_number") {
            ans = ans * 10 + c - '0';
            ans = sign == 1 ? min(ans, (long long) INT_MAX) : min(ans, -(long long) INT_MIN);
        } else if (state == "signed") {
            sign = c == '+' ? 1 : -1;
        }
    }
};

class Solution {
public:
    static long long myAtoi(const string &str) {
        Automaton automaton;
        for (char c: str) {
            automaton.get(c);
        }
        return automaton.sign * automaton.ans;
    }
};

//int main(int argc, char *argv[]) {
//    const string s1 = "-91283472332";
//    Solution::myAtoi(s1);
//    cout << Solution::myAtoi(s1) << endl;
//}