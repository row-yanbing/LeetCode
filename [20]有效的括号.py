# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "()"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：s = "()[]{}"
# 输出：true
#
#
#  示例 3：
#
#
# 输入：s = "(]"
# 输出：false
#
#
#  示例 4：
#
#
# 输入：s = "([)]"
# 输出：false
#
#
#  示例 5：
#
#
# 输入：s = "{[]}"
# 输出：true
#
#
#
#  提示：
#
#
#  1 <= s.length <= 104
#  s 仅由括号 '()[]{}' 组成
#
#  Related Topics 栈 字符串
#  👍 2473 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[', '}':'{'}
        stack = []  # 用栈来存储字符串
        for char in s:  # 当遇到右括号时，和栈顶元素对比，若匹配，则弹出栈顶，否则直接返回False
            if stack and char in dic:
                if stack[-1] == dic[char]:
                    stack.pop()
                else:
                    return False
            else:  # 若遇到左括号或者栈为空，则直接入栈，
                stack.append(char)
        return not stack  # 当栈为空时，返回True
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))
print(solution.isValid("{[]}"))
