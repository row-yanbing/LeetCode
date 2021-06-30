# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  判断你是否能够到达最后一个下标。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#
#
#  示例 2：
#
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 3 * 104
#  0 <= nums[i] <= 105
#
#  Related Topics 贪心 数组 动态规划
#  👍 1247 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):  # 遍历nums
            if farthest < i:  # 如果nums[i]之前的元素能达到的最远位置都不能到达i，则返回False
                return False
            farthest = max(farthest, nums[i] + i)  # 如果前面的元素能到达nums[i],则计算nums[i]能到达的最远位置
            if farthest >= len(nums) - 1:  # 如果最远位置能到达nums的最后一个元素，则返回True
                return True
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.canJump([2,3,1,1,4]))
print(solution.canJump([3,2,1,0,4]))
