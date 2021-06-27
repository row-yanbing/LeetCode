# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 8
#
#  Related Topics 字符串 动态规划 回溯
#  👍 1846 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        track = []
        self.backtrack(n, n, track)
        return self.res

    def backtrack(self,left, right, track):
        if left < 0 or right < 0:
            return
        if left > right: #如果左括号剩余数目大于右括号剩余数目，则不合法
            return
        if left == 0 and right == 0: #如果左右括号数目相等且都等于0，则将结果路径添加至结果
            self.res.append(''.join(track))
            return
        track.append('(')  #做选择，加入‘('左括号，继续回溯
        self.backtrack(left-1, right, track) #左括号数目减少1
        track.pop()

        track.append(')') #加入')'右括号，做回溯
        self.backtrack(left, right-1, track) #右括号数目减少1
        track.pop()


# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(1))
