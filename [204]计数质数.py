# 统计所有小于非负整数 n 的质数的数量。
#
#
#
#  示例 1：
#
#  输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#  示例 2：
#
#  输入：n = 0
# 输出：0
#
#
#  示例 3：
#
#  输入：n = 1
# 输出：0
#
#
#
#
#  提示：
#
#
#  0 <= n <= 5 * 106
#
#  Related Topics 数组 数学 枚举 数论
#  👍 710 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrimes(self, n: int) -> int:
        que = [1]*(n+1)
        if n < 3:
            return 0
        que[0] = que[1] = que[2] = 0
        for i in range(2, int(n**0.5)+1):
            if que[i+1]:
                j = 2
                while j*i < n:
                    que[j*i+1] = 0
                    j += 1
        count = sum(que)
        return count
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.countPrimes(1500000))
