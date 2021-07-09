# 编写一个函数来查找字符串数组中的最长公共前缀。
#
#  如果不存在公共前缀，返回空字符串 ""。
#
#
#
#  示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
#  示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
#  提示：
#
#
#  0 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] 仅由小写英文字母组成
#
#  Related Topics 字符串
#  👍 1673 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = min(strs) # 对字符串进行排序
        s2 = max(strs)
        l = min(len(s1), len(s2))
        i = 0
        while i < l:
            if s1[i] == s2[i]:
                i += 1
            else:
                break
        return s1[:i]

# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
