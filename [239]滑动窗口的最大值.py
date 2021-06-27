# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位
# 。
#
#  返回滑动窗口中的最大值。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#  示例 2：
#
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
#  示例 3：
#
#
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
#
#
#  示例 4：
#
#
# 输入：nums = [9,11], k = 2
# 输出：[11]
#
#
#  示例 5：
#
#
# 输入：nums = [4,-2], k = 2
# 输出：[4]
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 105
#  -104 <= nums[i] <= 104
#  1 <= k <= nums.length
#
#  Related Topics 队列 数组 Sliding Window Monotonic Queue Heap (Priority Queue)
#  👍 1044 👎 0
from typing import List
from collections import deque
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        que = deque()
        for i in range(len(nums)):
            while que and que[-1]<nums[i]:
                que.pop()
            que.append(nums[i])
            if i >= k-1:
                res.append(que[0])
                if nums[i-k+1] == que[0]:
                    que.popleft()
        return res
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
print(solution.maxSlidingWindow([1],1))
print(solution.maxSlidingWindow([1,-1],1))
print(solution.maxSlidingWindow([9,11],2))
print(solution.maxSlidingWindow([4,-2],2))
