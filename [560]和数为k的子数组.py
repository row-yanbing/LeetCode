# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
#  示例 1 :
#
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#
#
#  说明 :
#
#
#  数组的长度为 [1, 20,000]。
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
#
#  Related Topics 数组 哈希表 前缀和
#  👍 965 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_sum = 0
        dic = {0: 1}  # 用于记录presum值对应出现次数
        for num in nums:
            pre_sum += num
            sub = pre_sum - k  # 目标值
            if sub in dic:  # 若dic中存在，则value值加1
                count += dic[sub]
            dic[pre_sum] = dic.get(pre_sum, 0) + 1  # 将pre_sum存入dic中
            '''
            dic.get(pre_sum, 0)
            在dic里查找pre_sum，如果有返回对应的value，反之返回0 
            '''
        return count


# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))
