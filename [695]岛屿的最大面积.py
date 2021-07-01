# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
#
#  一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
#
#  找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
#
#
#
#  示例 1:
#
#  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
#
#  对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
#
#  示例 2:
#
#  [[0,0,0,0,0,0,0,0]]
#
#  对于上面这个给定的矩阵, 返回 0。
#
#
#
#  注意: 给定的矩阵grid 的长度和宽度都不超过 50。
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 502 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:  # 如果为空，则返回0
            return 0
        m = len(grid)
        n = len(grid[0])
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:  # 如果grid[i][j]=1，则求此块岛屿的面积
                    area = max(area, self.dfs(grid, i, j))
        return area  # 返回最大的岛屿面积

    def dfs(self, board, i, j):  # 当grid[i][j]为岛屿时，返回岛屿的面积
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j]:
            board[i][j] = 0  # 将统计过的部分置为0，并返回与当前连通的1有多少个，也即岛屿的面积
            return self.dfs(board, i-1, j) + self.dfs(board, i+1, j) + \
                   self.dfs(board, i, j-1) + self.dfs(board, i, j+1) + 1
        return 0
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
print(solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
