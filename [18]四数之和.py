# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
#  注意：答案中不可以包含重复的四元组。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
#  示例 2：
#
#
# 输入：nums = [], target = 0
# 输出：[]
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 200
#  -109 <= nums[i] <= 109
#  -109 <= target <= 109
#
#  Related Topics 数组 双指针 排序
#  👍 882 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        num = sorted(nums)
        return self.nsum(num, 4, target)

    def nsum(self,nums, n, target):
        if len(nums) < n or n < 2:
            return []
        res = []
        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:#将满足条件的元素组加入res
                    if [nums[left], nums[right]] not in res:#若res中有，则不添加
                        res.append([nums[left], nums[right]])
                    if nums[left] == nums[left+1] and left+1 < right: #若有相同元素，则跳过
                        left += 1
                    if nums[right] == nums[right-1] and left+1 < right:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            return res
        if n > 2:
            for index in range(len(nums)): #选择nums中的一个元素，进行递归
                if index > 0 and nums[index-1] == nums[index]: #若后一个元素与当前元素相同，则跳过
                    continue
                sub_res = self.nsum(nums[index+1:], n-1, target-nums[index]) #递归
                for j in range(len(sub_res)): #将num[index]加入到上一结果中，注意用内层用列表相加，不能用嵌套append
                    res.append(sub_res[j] + [nums[index]])
            return res

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.fourSum([4,-9,-2,-2,-7,9,9,5,10,-10,4,5,2,-4,-2,4,-9,5], -13))
print(solution.fourSum([], 0))
