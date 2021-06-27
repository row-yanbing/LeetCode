# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
#  示例:
#
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#  Related Topics 数组 回溯
#  👍 609 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.backtrack(n, k, 1, [])
        return self.res

    def backtrack(self, n, k, start, track): #回溯算法
        if len(track) == k: #满足条件，将路径添加进结果
            self.res.append(track[:]) #注意，此处track为list，添加时要用[:],否则容易出错
            return
        for i in range(start, n+1): #从start-n中选择一个数
            track.append(i) #将数添加至路径
            self.backtrack(n, k, i+1, track) #回溯
            track.pop() #将数从路径移除

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.combine(4,2))
print(solution.combine(1,1))
