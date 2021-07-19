# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
#  示例 3：
#
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 6
#  -10 <= nums[i] <= 10
#  nums 中的所有整数 互不相同
#
#  Related Topics 数组 回溯
#  👍 1422 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, [])
        return self.res

    def backtrack(self,nums, track):
        if len(track) == len(nums): #终止条件，路径长度等于nums长度
            self.res.append(track[:])  # 注意要用track[:]，否则出错
            return
        for i in range(len(nums)): #从0开始，每次取nums中的一个数
            if nums[i] in track: #若数字在路径中，则跳过，取下一个数
                continue
            track.append(nums[i])
            self.backtrack(nums, track)
            track.pop()

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.permute([1,2,3]))
print(solution.permute([1]))
print(solution.permute([0,1]))
