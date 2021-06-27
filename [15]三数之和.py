# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
#  示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 3000
#  -105 <= nums[i] <= 105
#
#  Related Topics 数组 双指针 排序
#  👍 3446 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        num = sorted(nums)
        return self.nsum(num, 3, 0)

    def nsum(self, nums, n, target):
        if n < 2 or len(nums) < n:
            return []
        res = []
        if n == 2:
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    if [nums[left],nums[right]] not in res:
                        res.append([nums[left], nums[right]])
                    while nums[left] == nums[left+1] and left+1 < right:
                        left += 1
                    while nums[right] == nums[right-1] and left+1 < right:
                        right -= 1
                    left += 1
                    right -= 1
            return res

        if n > 2:
            for index in range(len(nums)):
                if index > 0 and nums[index] == nums[index-1]:
                    continue
                sub_res = self.nsum(nums[index+1:], n-1,  target-nums[index])
                for j in range(len(sub_res)):
                    res.append(sub_res[j] + [nums[index]]) #注意，append返回None，故append内层只能使用list相加
            return res

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([0, 0, 0]))
print(solution.threeSum([]))
