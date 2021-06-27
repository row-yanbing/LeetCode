# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
#
#
#
#  示例 1:
# 输入:
#
#  "bbbab"
#
#
#  输出:
#
#  4
#
#
#  一个可能的最长回文子序列为 "bbbb"。
#
#  示例 2:
# 输入:
#
#  "cbbd"
#
#
#  输出:
#
#  2
#
#
#  一个可能的最长回文子序列为 "bb"。
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 只包含小写英文字母
#
#  Related Topics 动态规划
#  👍 463 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)] #dp[i,j]表示s[i:j]的最大回文子序列
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-2, -1, -1): #由于最终要求s[0,n-1],所以采用倒序遍历
            for j in range(i+1, n): #i>j时，不存在这样的字符串，故s[i,j]为0
                if s[i] == s[j]:
                   dp[i][j] = dp[i+1][j-1] + 2 #注意dp[i][j]的前一问题是dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.longestPalindromeSubseq("bbbab"))
print(solution.longestPalindromeSubseq("cbbd"))
print(solution.longestPalindromeSubseq("bbbab"))
