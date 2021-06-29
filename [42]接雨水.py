# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
#  示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
#  提示：
#
#
#  n == height.length
#  0 <= n <= 3 * 104
#  0 <= height[i] <= 105
#
#  Related Topics 栈 数组 双指针 动态规划 单调栈
#  👍 2443 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 1: #若数组为空或只有一个元素，则返回0
            return 0
        ans = 0  #初始化左右指针，左右最大值
        left = 0
        right = len(height) - 1
        l_max = 0
        r_max = 0
        while left <= right: # 遍历数组
            l_max = max(l_max, height[left])  #找出左区间[0,left]的最大值
            r_max = max(r_max, height[right])  # 找出右区间的最大值
            if l_max < r_max:  # 利用左右两区间的最小值计算左右边界的元素能装的水量
                ans = ans + l_max - height[left]  # 若左边最大值小，则计算左边界元素的装水量
                left += 1 #指针右移
            else:
                ans = ans + r_max - height[right]  # 若右边值小，则计算右边界元素的装水量
                right -= 1  # 右边界左移
        return ans

# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trap([4,2,0,3,2,5]))
