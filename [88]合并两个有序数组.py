# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nu
# ms2 的元素。
#
#
#
#  示例 1：
#
#
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#
#
#  示例 2：
#
#
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  nums1.length == m + n
#  nums2.length == n
#  0 <= m, n <= 200
#  1 <= m + n <= 200
#  -109 <= nums1[i], nums2[i] <= 109
#
#  Related Topics 数组 双指针 排序
#  👍 981 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n -1
        while m > 0 and n > 0:  # 当nums1和nums2中都有元素时，将两者的末尾元素进行对比
            if nums1[m-1] > nums2[n-1]: #将大的元素从后往前添加至nums1
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k = k-1
        nums1[:n] = nums2[:n]  # 若nums2还剩n个元素，则直接将其添加至nums1中
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(solution.merge([1],1,[],0))
