# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#
#
#  示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
#  示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#  示例 3：
#
#
# 输入：s = "a"
# 输出："a"
#
#
#  示例 4：
#
#
# 输入：s = "ac"
# 输出："a"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 仅由数字和英文字母（大写和/或小写）组成
#
#  Related Topics 字符串 动态规划
#  👍 3777 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''  # 初始化结果为空字符串
        for i in range(len(s)):  # 遍历s，找到以s[i]或者是s[i,i+1]为中心的最长回文子串
            s1 = self.palindrom(s, i, i)
            s2 = self.palindrom(s, i, i + 1)
            if len(s1) > len(s2):
                res = s1 if len(s1) > len(res) else res  # 将当前结果与之前最长子串比较，取长者
            else:
                res = s2 if len(s2) > len(res) else res
        return res


    def palindrom(self, s, l, r):  # 返回以s[l,r]为中心的最长回文子串，当l=r时，中间只有一个元素
        while l >= 0 and r < len(s) and s[l] == s[r]: # 注意这行的精髓，先判断范围，再判断是否相等
            l -= 1
            r += 1
        return s[l+1:r]

# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("ac"))
