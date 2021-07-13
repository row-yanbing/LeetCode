# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
#
#
#
#  示例 1：
#
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#
#
#  示例 2：
#
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#
#
#  示例 3：
#
#
# 输入：s = ""
# 输出：0
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 3 * 104
#  s[i] 为 '(' 或 ')'
#
#
#
#  Related Topics 栈 字符串 动态规划
#  👍 1366 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        stack = []  # 用于记录元素下标
        res = 0
        i = 0
        while i < len(s):  # 对s进行遍历
            if stack and s[i] == ')' and s[stack[-1]] == '(':  # 若栈非空，且s当前元素为右括号，且栈顶元素为左括号，则出栈
                stack.pop()
                res = max(res, i - (stack[-1] if stack else -1))  # 返回最大值
            else:
                stack.append(i)  # 其他情况，则直接将下标入栈
            i += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.longestValidParentheses("()"))
print(solution.longestValidParentheses(")()())"))
print(solution.longestValidParentheses(""))
