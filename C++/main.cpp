//
//  main.cpp
//  test
//
//  Created by Tony on 2021/6/14.
//

#include "main.hpp"
#include "1.twoSum.cpp"
using namespace std;


int main(int argc, char *argv[]) {
    Solution so;
    int b[4] = {2, 7, 11, 15};
    vector<int> a(b,b+4);
    int target = 9;
    so.twoSum(a, target);
    printf("Done.\n");
}
