# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
#  示例 1:
#
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
#
#
#  示例 2:
#
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#
#
#  注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
#  Related Topics 动态规划
#  👍 320 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums) #记录nums中第i个元素的最长子序列个数
        res = [1]*len(nums) #记录nums中能一步到nums[i]的元素个数
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] <= dp[j]:
                        dp[i] = dp[j] + 1
                        res[i] = res[j]
                    elif dp[i] == dp[j] + 1:
                        res[i] = res[j] + res[i]
        max_len = max(dp)
        result = 0
        for i, x in enumerate(res):
            if dp[i] == max_len:
                result = result + x
        return result



# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.findNumberOfLIS([1,2,4,3,5,4,7,2]))
print(solution.findNumberOfLIS([2,2,2,2,2]))
