# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
#  假设你总是可以到达数组的最后一个位置。
#
#
#
#  示例 1:
#
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
#  示例 2:
#
#
# 输入: [2,3,0,1,4]
# 输出: 2
#
#
#
#
#  提示:
#
#
#  1 <= nums.length <= 1000
#  0 <= nums[i] <= 105
#
#  Related Topics 贪心 数组 动态规划
#  👍 1027 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        end = 0
        for i in range(n-1):  # 遍历终点前的每个元素
            farthest = max(farthest, nums[i]+i)  # 计算前i+1个元素跳的最远距离
            if end == i:  # 如果在指针i到达上次跳的最远处，则开始进行下一跳
                jumps += 1  # 跳的次数加1
                end = farthest  # 将end指针指到下一跳的最远处，也即在end处元素之前，所有元素能到的最远处
        return jumps
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.jump([2,3,1,1,4]))
print(solution.jump([2,3,0,1,4]))
