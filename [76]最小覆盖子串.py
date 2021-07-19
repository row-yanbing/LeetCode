# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
#  注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#  示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
#  示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
#
#
#  提示：
#
#
#  1 <= s.length, t.length <= 105
#  s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 双指针 字符串 Sliding Window
#  👍 1195 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dic = {}  # 建立字典，用于统计t中出现的字符
        for char in t:
            if char in t_dic:
                t_dic[char] += 1
            else:
                t_dic[char] = 1
        left = 0  # 用双指针
        count = len(t)  # 记录t中的字符总数
        right = 0
        windows = {}  # 结果字典，用于记录每个符合要求的子串
        while right < len(s):  # 遍历字符串s
            if s[right] in t_dic:  # 判断字符是否存在于t
                if t_dic[s[right]] > 0:  # 若该字符存在于t，且需要出现次数为正，则count数减少1
                    count -= 1
                t_dic[s[right]] -= 1  # 若该字符属于t，则字典中数目减少1
                while count == 0:  # 当count数为0，也即t中所有字符全部出现在s[left:right+1]中时，缩减left边界，直到找到最小字符串
                    if s[left] in t_dic:  # 若左边界字符在t中存在，则判断当前子字符串是否包含全部t的字符
                        if t_dic[s[left]] >= 0:  # 若字典中该字符需要出现次数不为负数，则count数加1
                            count += 1
                            windows_len = right - left + 1  # 此时该子字符串为当前包含t所有元素的子字符串，长度为
                            windows[windows_len] = s[left:right+1]  # 记录该子字符串的长度和子字符串记录，由于是唯一的，故key不存在冲突
                        t_dic[s[left]] += 1  # 将字典中该字符需要出现次数加1
                    left += 1  # 缩减左边界
            right += 1
        sort_win = sorted(windows)  # 将记录结果按字符串铲毒排序
        min_char = windows[sort_win[0]] if windows else ''
        return min_char

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.minWindow("ADOBECODEBANCABC", "ABC"))
print(solution.minWindow("a", "aa"))

