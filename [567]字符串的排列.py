# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
#  换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
#
#
#
#  示例 1：
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#  示例 2：
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
#  提示：
#
#
#  输入的字符串只包含小写字母
#  两个字符串的长度都在 [1, 10,000] 之间
#
#  Related Topics 双指针 Sliding Window
#  👍 358 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from collections import Counter
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_dic =Counter(s1)
        s2_list = list(s2)
        right = len(s1)
        while right <= len(s2):
            tmp_list = s2_list[left:right]
            tmp_dic = Counter(tmp_list)
            if tmp_dic == s1_dic:
                return True
            left += 1
            right = left + len(s1)
        return False
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.checkInclusion('ab',"eidbaooo"))
print(solution.checkInclusion('ab',"eidboaoo"))
