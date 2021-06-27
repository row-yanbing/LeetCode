# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#
#  '.' 匹配任意单个字符
#  '*' 匹配零个或多个前面的那一个元素
#
#
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#
#  示例 1：
#
#
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
#
#  示例 2:
#
#
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
#  示例 3：
#
#
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#  示例 4：
#
#
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#
#  示例 5：
#
#
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false
#
#
#
#  提示：
#
#
#  0 <= s.length <= 20
#  0 <= p.length <= 30
#  s 可能为空，且只包含从 a-z 的小写字母。
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#  保证每次出现字符 * 时，前面都匹配到有效的字符
#
#  Related Topics 字符串 动态规划 回溯算法
#  👍 2179 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dp(s, 0, p, 0)

    def dp(self, s: str, i: int, p: str, j: int) -> bool:
        m = len(s)
        n = len(p)
        if j == n:  #base case
            return i == m
        if i == m:
            if (n - j) % 2 == 1:  #若p剩余元素为奇数，则不能匹配
                return False
            for k in range(j, n-1, 2): #若剩余元素为x*成对出现，则可以匹配
                if p[k + 1] != "*":
                    return False
            return True
        memo = dict()  #用memo作为函数缓存
        if (i, j) in memo.keys():
            return memo[(i, j)]

        if s[i] == p[j] or p[j] == ".":
            if j < n-1 and p[j + 1] == "*": #选择匹配0次，或匹配n次
                res = self.dp(s, i, p, j + 2) or self.dp(s, i + 1, p, j)
            else:
                res = self.dp(s, i + 1, p, j + 1) #只能匹配一次
        else:
            if j < n-1 and p[j + 1] == '*':
                res = self.dp(s, i, p, j + 2)  # 匹配0次
            else:
                res = False
        memo[(i, j)] = res
        return res


# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.isMatch("aa", "a"))
print(solution.isMatch("a", ".*.."))
print(solution.isMatch("a", ".*"))
print(solution.isMatch("ab", ".*..c*"))
print(solution.isMatch("mississippi", "mis*is*p*."))
