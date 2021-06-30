# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
#
#  注意:
#
#
#  可以认为区间的终点总是大于它的起点。
#  区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
#
#
#  示例 1:
#
#
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
#
# 输出: 1
#
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#
#
#  示例 2:
#
#
# 输入: [ [1,2], [1,2], [1,2] ]
#
# 输出: 2
#
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#
#
#  示例 3:
#
#
# 输入: [ [1,2], [2,3] ]
#
# 输出: 0
#
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#
#  Related Topics 贪心 数组 动态规划 排序
#  👍 439 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # 将intervals进行排序，以区间末尾元素升序排列
        count = 0
        last_end = intervals[0][1]  # 初始化前一区间的结尾元素
        for i in range(1, len(intervals)):  # 从第2个区间开始遍历
            start = intervals[i][0]  # 当前区间的起始元素
            if start >= last_end:  # 若无重叠，则将该区间末尾元素作为新的判断标准
                last_end = intervals[i][1]
            else:  # 若存在重叠，则计数加1
                count += 1
        return count

# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))
print(solution.eraseOverlapIntervals([ [1,2], [1,2], [1,2] ]))
print(solution.eraseOverlapIntervals([ [1,2], [2,3] ]))
