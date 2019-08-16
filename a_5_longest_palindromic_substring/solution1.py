'''
author:mxt
desc:无算法应用，纯属Python暴力破解,oj跑不过，存在超时
time：2019/08/17
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        if not str_len:
            return s
        longest_str = s[0]
        for i in range(str_len):
            for j in range(i + 1, str_len):
                temp_str = s[i:j + 1]
                if self.is_palindrome(temp_str):
                    longest_str = longest_str if len(longest_str) > len(temp_str) else temp_str
        return longest_str

    def is_palindrome(self, s):
        for i in range(int(len(s) / 2)):
            if s[i] is not s[len(s) - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    a = Solution()
    print(a.longestPalindrome('babad'))
