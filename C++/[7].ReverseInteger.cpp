//
// Created by Tony on 2021/7/17.
//

class Automaton {
    string state = "start";
    unordered_map <string, vector<string>> table = {
            //'', '+-', number, other
            {"start",     {"start", "signed", "in_number", "end"}},
            {"signed",    {"end",   "end",    "in_number", "end"}},
            {"in_number", {"end",   "end",    "in_number", "end"}},
            {"end",       {"end",   "end",    "end",       "end"}}
    };

    int get_col(char c) {

    }
};