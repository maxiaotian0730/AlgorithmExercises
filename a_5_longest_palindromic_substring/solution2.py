class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not n:
            return s
        for i in range(n):
            start = 0
            end = n - i
            while end <= n:
                sub_string = s[start:end]
                if self.is_palindromic_string(sub_string):
                    return sub_string
                start += 1
                end += 1


    def is_palindromic_string(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    s= Solution()
    print(s.longestPalindrome("ab"))
