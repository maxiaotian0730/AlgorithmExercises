'''
author:mxt
desc:无算法应用，纯属Python暴力破解
time：2019/08/16
'''


class Solution(object):
    @classmethod
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_list = nums1 + nums2
        new_list.sort()
        # print(new_list)
        if len(new_list) == 1:
            return new_list[0]
        a, b = divmod(len(new_list), 2)
        # print(a,b)
        if not b:
            return (new_list[a - 1] + new_list[a]) / 2.0
        return new_list[a]


if __name__ == '__main__':
    num1 = [1, 4]
    num2 = [2, 3]
    print(Solution.findMedianSortedArrays(num1, num2))
