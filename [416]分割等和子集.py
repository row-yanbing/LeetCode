# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
#
#  示例 2：
#
#
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 200
#  1 <= nums[i] <= 100
#
#  Related Topics 动态规划
#  👍 832 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = len(nums) + 1
        sums = int(sum(nums)/2)
        if sum(nums) % 2 == 1:  #如果和为奇数，则不能分
            return False
        dp = [[False]*(sums + 1) for _ in range(m)] #dp[i][j]表示前i个元素能否凑成j，i是从0至n，就从0至nums
        for i in range(m): #如果j等于0，说明背包满了，也就是存在这样的元素
            dp[i][0] = True
        for i in range(1, m):
            for j in range(1, sums + 1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[m-1][sums]
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.canPartition([1, 5, 11, 5]))
print(solution.canPartition([1, 2, 3, 5]))
