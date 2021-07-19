# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 8
#  -10 <= nums[i] <= 10
#
#  Related Topics 数组 回溯
#  👍 734 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        track = []
        index = []
        self.backtrack(nums, index, track)
        return self.res

    def backtrack(self,nums, index, track): #用index记录被访问过的元素索引
        if len(track) == len(nums) and track not in self.res: #如果track长度达到，且不存在重复，则存入结果
            self.res.append(track[:])  # 注意要用复制[:]
            return
        for i in range(len(nums)):
            if i in index: #排除已访问的元素
                continue
            else:
                track.append(nums[i]) #将未访问的元素添加进路径
                index.append(i) #将访问的元素索引添加进index
                self.backtrack(nums, index, track)
                track.pop() #恢复路径
                index.pop() #弹出索引

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.permuteUnique([1,1,2]))
print(solution.permuteUnique([1,2,3]))
