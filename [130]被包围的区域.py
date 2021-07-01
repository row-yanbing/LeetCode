# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#
#
#
#
#  示例 1：
#
#
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X"
# ,"X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#
#
#  示例 2：
#
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n == board[i].length
#  1 <= m, n <= 200
#  board[i][j] 为 'X' 或 'O'
#
#
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 557 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:  # 若区域为空，则直接返回None
            return
        m = len(board)
        n = len(board[0])
        if m < 3 or n < 3:  # 若board尺寸小于3，则直接返回None
            return
        '''
        找到与边界的'O'和与其相连通的'O'，并将他们标记为'#'，这些是不用变为'X'的元素，剩下的'O'都要变成'X'
        '''
        for i in range(m):  # 在第1列和最后1列的边界找到‘O’，并将其和与其连通的元素变为‘#’
            self.dfs(board, i, 0)
            self.dfs(board, i, n - 1)
        for j in range(n):  # 在第1行和最后1行的边界找到‘O’，并将其和与其相连通的元素变为‘#’
            self.dfs(board, 0, j)
            self.dfs(board, m - 1, j)
        '''
        遍历整个board，找到剩余的'O'，这些都需要变成'X'，顺便将之前变成'#'的变成'O'
        '''
        for i in range(m):  # 遍历整个board，将剩余的'O‘变为'X'，并将之前变为'#’的变为'O'
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    '''
    深度遍历，寻找'O'和其连通的'O'，并将其变成'#'
    '''

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return  # 处理边界
        board[i][j] = '#'
        self.dfs(board, i - 1, j)  # 向元素board[i,j]='O'的上下左右寻找与其连通的'O'
        self.dfs(board, i, j - 1)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j + 1)


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.solve(board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
print(solution.solve([["X"]]))
