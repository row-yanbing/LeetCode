# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#
#
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
#  示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：[["Q"]]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 9
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
#
#
#
#  Related Topics 回溯算法
#  👍 900 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        self.backtrack(result, n, board, 0)
        return result

    def backtrack(self, result, n, board, row):
        if row == n:
            res = [''.join(line) for line in board]
            result.append(res)
            return

        for col in range(n):
            if not self.isvalid(n, board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(result, n, board, row + 1)
            board[row][col] = '.'

    def isvalid(self, n, board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i in range(row - 1, -1, -1):
            k = row - i
            col1 = col - k
            col2 = col + k
            if col1 >= 0 and board[i][col1] == 'Q':
                return False
            if col2 < n and board[i][(col + k)] == 'Q':
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.solveNQueens(1))
print(solution.solveNQueens(4))