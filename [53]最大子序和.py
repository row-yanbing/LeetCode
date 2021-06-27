# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
#  示例 2：
#
#
# 输入：nums = [1]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：0
#
#
#  示例 4：
#
#
# 输入：nums = [-1]
# 输出：-1
#
#
#  示例 5：
#
#
# 输入：nums = [-100000]
# 输出：-100000
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 3 * 104
#  -105 <= nums[i] <= 105
#
#
#
#
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#  Related Topics 数组 分治算法 动态规划
#  👍 3302 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums) #dp数组用于记录结尾为nums[i]元素的最大数组和
        dp[0] = nums[0]
        i = 1
        while i < len(nums):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            i = i+1
        return max(dp)

# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([-1]))
print(solution.maxSubArray([0]))
print(solution.maxSubArray([-10000]))
print(solution.maxSubArray([1]))
