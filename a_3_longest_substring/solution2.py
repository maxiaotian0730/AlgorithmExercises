'''
author:mxt
desc:滑动窗口，稍微优化下解法1的，
time：2019/08/15
'''

class Solution:
    @classmethod
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        longest_str = ''
        for i in s:
            if i not in longest_str:
                longest_str += i
            else:
                longest_str = longest_str[longest_str.index(i) + 1:] + i
            max_len = max_len if len(longest_str) < max_len else len(longest_str)
        return max_len


if __name__ == '__main__':
    s = 'qweqqwesd'
    print(Solution.lengthOfLongestSubstring(s))
