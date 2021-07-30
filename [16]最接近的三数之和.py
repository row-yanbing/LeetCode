# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。
#
#
#
#  示例：
#
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
#
#
#  提示：
#
#
#  3 <= nums.length <= 10^3
#  -10^3 <= nums[i] <= 10^3
#  -10^4 <= target <= 10^4
#
#  Related Topics 数组 双指针 排序
#  👍 835 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        m = len(nums)
        num = sorted(nums)
        res = float('inf')
        for i in range(m):
            left = i + 1
            right = m - 1
            while left < right:
                tmp = num[i] + num[left] + num[right]
                res = tmp if abs(tmp - target) < abs(res - target) else res
                if tmp > target:
                    right -= 1
                else:
                    left += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1))
