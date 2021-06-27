# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。
#
#  你可以认为每种硬币的数量是无限的。
#
#
#
#  示例 1：
#
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
#  示例 2：
#
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#  示例 4：
#
#
# 输入：coins = [1], amount = 1
# 输出：1
#
#
#  示例 5：
#
#
# 输入：coins = [1], amount = 2
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= coins.length <= 12
#  1 <= coins[i] <= 231 - 1
#  0 <= amount <= 104
#
#  Related Topics 动态规划
#  👍 1298 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
###解法一，递归

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = {}

        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = 10000
            if n in result:
                return result[n]

            else:
                for coin in coins:
                    subproblem = dp(n-coin)
                    if subproblem == -1:
                        continue
                    res = min(res, 1 + subproblem)
                result[n] = res if res != 10000 else -1
                return result[n]


        return dp(amount)

# leetcode submit region end(Prohibit modification and deletion)
####解法二，动态规划

#from typing import List
#
#
#class Solution:
#    def coinChange(self, coins: List[int], amount: int) -> int:
#        result = {}
#        result[0] = 0
#        for i in range(1, amount + 1):
#            result[i] = amount + 2
#            for coin in coins:
#                if i - coin < 0:
#                    continue
#                result[i] = min(result[i], 1 + result[i - coin])
#        if result[amount] == amount + 2:
#            return -1
#        else:
#            return result[amount]
#
solution = Solution()
print(solution.coinChange(coins=[1, 2, 5], amount=11))
