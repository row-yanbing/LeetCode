# 给你一个整数数组 nums 和一个整数 target 。
#
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
#
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
#
#
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
#
#  示例 2：
#
#
# 输入：nums = [1], target = 1
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 20
#  0 <= nums[i] <= 1000
#  0 <= sum(nums[i]) <= 1000
#  -1000 <= target <= 1000
#
#  Related Topics 深度优先搜索 动态规划
#  👍 809 👎 0

from typing import List, Any, Union


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = dict()

        if len(nums) == 0:
            return 0

        def dp(i, res): #前i个元素能凑成res的方法数
            if (i,res) in result:
                return result[(i, res)]
            if i == -1:
                if res == 0:
                    return 1
                return 0
            result[(i,res)] = dp(i-1, nums[i] + res) + dp(i-1, res -nums[i])
            return result[(i, res)]

        return dp(len(nums)-1, target)

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.findTargetSumWays([1,1,1,1,1], 3))
print(solution.findTargetSumWays([1], 1))
