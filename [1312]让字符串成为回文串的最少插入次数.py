# 给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
#
#  请你返回让 s 成为回文串的 最少操作次数 。
#
#  「回文串」是正读和反读都相同的字符串。
#
#
#
#  示例 1：
#
#
# 输入：s = "zzazz"
# 输出：0
# 解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
#
#
#  示例 2：
#
#
# 输入：s = "mbadm"
# 输出：2
# 解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
#
#
#  示例 3：
#
#
# 输入：s = "leetcode"
# 输出：5
# 解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
#
#
#  示例 4：
#
#
# 输入：s = "g"
# 输出：0
#
#
#  示例 5：
#
#
# 输入：s = "no"
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 500
#  s 中所有字符都是小写字母。
#
#  Related Topics 动态规划
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        dp = [[0]*n for _ in range(n)]  # dp[i][j]表示s[i,j]成为回文串的最小插入次数
        for i in range(n-2, -1, -1):  # 倒序遍历
            for j in range(i+1, n):
                if s[i] == s[j]:  # 若字符相等，则不用插入
                    dp[i][j] = dp[i+1][j-1]
                else:  # 若不相等，则在选择在i或者在j插入
                    dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1

        return dp[0][n-1]


# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.minInsertions("zzazz"))
print(solution.minInsertions("mbadm"))
print(solution.minInsertions("leetcode"))
print(solution.minInsertions("no"))

