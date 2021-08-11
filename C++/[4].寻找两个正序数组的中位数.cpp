//
//  寻找两个正序数组的中位数 难度 困难  4193  收藏  分享 切换为英文 接收动态 反馈 寻找两个正序数组的中位数 难度 困难  4193  收藏  分享 切换为英文 接收动态 反馈 寻找两个正序数组的中位数.cpp
//  Run
//
//  Created by Tony on 2021/6/23.
//

#include <vector>
using namespace::std;

class Solution {
public:
    static double getKthElement(const vector<int> &nums1, const vector<int> &nums2, int k) {
        /* 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
         * 这里的 "/" 表示整除
         * nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
         * nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
         * 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
         * 这样 pivot 本身最大也只能是第 k-1 小的元素
         * 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
         * 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
         * 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
         */
        int m = int(nums1.size());
        int n = int(nums2.size());
        int index1 = 0, index2 = 0;
        
        while (true) {
            // 边界情况
            if (index1 == m) {
                return nums2[index2 + k - 1];
            }
            if (index2 == n) {
                return nums1[index1 + k - 1];
            }
            if (k == 1) {
                return min(nums1[index1], nums2[index2]);
            }
            
            // 正常情况
            int newIndex1 = min(index1 + k / 2 - 1, m - 1);
            int newIndex2 = min(index2 + k / 2 - 1, n - 1);
            int pivot1 = nums1[newIndex1];
            int pivot2 = nums2[newIndex2];
            if (pivot1 <= pivot2) {
                k -= newIndex1 - index1 + 1;
                index1 = newIndex1 + 1;
            } else {
                k -= newIndex2 - index2 + 1;
                index2 = newIndex2 + 1;
            }
        }
    }

    [[maybe_unused]] static double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
        int totalLength = int(nums1.size()) + int(nums2.size());
        if (totalLength % 2 == 1) {
            return getKthElement(nums1, nums2, (totalLength + 1) / 2);
        } else {
            return (getKthElement(nums1, nums2, totalLength / 2) + getKthElement(nums1,
                                                                                 nums2, totalLength / 2 + 1)) / 2.0;
        }
    }
};

//int main (int argc, char * args[]) {
//    int i1[] = {1, 3};
//    vector<int> v1(i1, i1 + 2);
//    int i2[] = {2,};
//    vector<int> v2(i2, i2 + 1);
//    Solution so;
//    so.findMedianSortedArrays(v1, v2);
//    cout << so.findMedianSortedArrays(v1, v2) << endl;
//}
//
