'''
author:mxt
desc:暴力破解，感觉烂烂的
time：2019/08/15
'''


class Solution:
    @classmethod
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ''
        substring_len_list = []
        for idx, val in enumerate(s):
            if val not in longest_substring:
                longest_substring += val
                if idx == len(s) - 1:
                    substring_len_list.append(len(longest_substring))
            else:
                substring_len_list.append(len(longest_substring))
                longest_substring = longest_substring[longest_substring.index(val) + 1:] + val
        max_len = 0
        if substring_len_list:
            max_len = max(substring_len_list)
        return max_len


if __name__ == '__main__':
    s = 'qqqwiopwaeredvs'
    s = ''
    print(Solution.lengthOfLongestSubstring(s))
