# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1：
#
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 300
#  grid[i][j] 的值为 '0' 或 '1'
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 1212 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # 若grid为空，则返回0
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):  # 遍历grid，找到'1'
            for j in range(n):
                if grid[i][j] == '1':  # 若找到'1'，则将其和其连通的区域变为'0'
                    count += 1  # 找到一个岛屿
                    self.dfs(grid, i, j)  # 寻找其连通区域，并将其置为'0'
        return count

    def dfs(self,board, i, j):  # 寻找board[i,j]='1'连通的其他'1'元素，并将其置为'0'
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != '1':
            return
        board[i][j] = '0'
        self.dfs(board, i-1, j)
        self.dfs(board, i+1, j)
        self.dfs(board, i, j-1)
        self.dfs(board, i, j+1)


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],
                           ["1","1","0","1","0"],
                           ["1","1","0","0","0"],
                           ["0","0","0","0","0"]]))

print(solution.numIslands([["1","1","0","0","0"],
                           ["1","1","0","0","0"],
                           ["0","0","1","0","0"],
                           ["0","0","0","1","1"]]))
