# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
#  现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i -
#  1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
#
#  求所能获得硬币的最大数量。
#
#
# 示例 1：
#
#
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
#  示例 2：
#
#
# 输入：nums = [1,5]
# 输出：10
#
#
#
#
#  提示：
#
#
#  n == nums.length
#  1 <= n <= 500
#  0 <= nums[i] <= 100
#
#  Related Topics 分治算法 动态规划
#  👍 740 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [0]*(n+2)
        points[0] = points[n+1] = 1
        points[1:n+1] = nums[:]
        dp = [[0]*(n+2) for _ in range(n+2)]
        for i in range(n, -1, -1):
            for j in range(i+1, n+2):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+points[i]*points[j]*points[k])
        return dp[0][n+1]


# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.maxCoins([3,1,5,8]))
print(solution.maxCoins([1,5]))
