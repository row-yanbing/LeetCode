# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
#  示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#  nums 中的所有元素 互不相同
#
#  Related Topics 位运算 数组 回溯算法
#  👍 1226 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(0, nums, [])
        return self.res

    def backtrack(self, index, nums, track): #回溯算法
        if index == len(nums): #结束条件
            self.res.append(track[:]) #注意，添加时要用[:]
            return
        track.append(nums[index]) #将nums[index]加入track
        self.backtrack(index+1, nums, track) #进行回溯
        track.pop() #撤销nums[index]
        self.backtrack(index+1, nums, track) # track不添加nums[index]，进行回溯

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.subsets([1,2,3]))
print(solution.subsets([0]))
