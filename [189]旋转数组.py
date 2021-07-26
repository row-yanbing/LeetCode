# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#
#
#  进阶：
#
#
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#  你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#
#
#
#
#  示例 1:
#
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 104
#  -231 <= nums[i] <= 231 - 1
#  0 <= k <= 105
#
#
#
#
#  Related Topics 数组 数学 双指针
#  👍 1037 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        if m == 1:
            return
        if k >= m:
            k = k % m
        nums[:m-k] = self.reverse(nums[:m-k])  # 三次反转数组，第一次反转k左右两边的子数组
        nums[m-k:] = self.reverse(nums[m-k:])  # 反转另一边的子数组
        self.reverse(nums)  # 反转整个数组

    def reverse(self, nums):  # 对数组进行反转
        if len(nums) == 1:
            return nums
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7], 3))
