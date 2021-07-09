# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 9313 👎
#闫兵，2020年10月13日

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target-nums[i]
            if res in nums and nums.index(res) != i:  # 如果存在这样的数，并且该数字的索引不等于i，则是要找的数字
                return [i, nums.index(res)]
# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.twoSum([3,2,4], 6))
