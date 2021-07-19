# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
#  你可以对一个单词进行如下三种操作：
#
#
#  插入一个字符
#  删除一个字符
#  替换一个字符
#
#
#
#
#  示例 1：
#
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
#  示例 2：
#
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#
#
#  提示：
#
#
#  0 <= word1.length, word2.length <= 500
#  word1 和 word2 由小写英文字母组成
#
#  Related Topics 字符串 动态规划
#  👍 1649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]  # 初始化memo[][],memo[i][j]表示word1[:i]和word2[:j]的最小编辑距离
        for j in range(len(word2)):  # 初始化memo[0][],表示word1只有0个字母时，最短编辑距离
            memo[0][j] = j
        for j in range(len(word1)):  # 初始化memo[][0],表示word2只有0个字母时，最短编辑距离
            memo[j][0] = j
        for i in range(1,len(word1)+1):  # 开始循环遍历
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:  # 注意，由于memo尺寸为n+1，所以索引要减少1
                    memo[i][j] = memo[i-1][j-1]  # 若word1和word2当前字符相同，则不用改变，当前memo[i][j]和memo[i-1][j-1]相同
                else:  # 否则，对word1进行操作，插入字符memo[i][j-1]，删除字符memo[i-1][j]，替换字符memo[i-1][j-1]
                    memo[i][j] = min(memo[i][j-1]+1, memo[i-1][j]+1, memo[i-1][j-1]+1)
        return memo[len(word1)][len(word2)]
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.minDistance("horse", "ros"))
print(solution.minDistance("intention", "execution"))
