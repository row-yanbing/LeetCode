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
        right = 0
        left = 0
        t_list = list(t)
        t_set = set(t_list)
        t_dic = {}
        for i in t_list:
            t_dic[i] = t_list.count(i)  #构建子字符串的字典，记录字符串元素和对应出现的频数
        count = len(t)   #记录子字符串的元素个数
        s_list = list(s)
        min_dic = {} #记录每次包含子字符串全部元素时，滑动窗口的长度及内容
        while right < len(s_list): #遍历字符串
            if s_list[right] in t_set: #若出现子字符串的元素，count和子字符串字典处理
                if t_dic[s_list[right]] > 0:
                    count = count - 1
                t_dic[s_list[right]] = t_dic[s_list[right]] - 1
                while count == 0:
                    windows_len = right - left + 1
                    min_dic[windows_len] = s_list[left:right+1]
                    if s_list[left] in t_set:
                        if t_dic[s_list[left]] == 0:
                            count = count + 1
                        t_dic[s_list[left]] = t_dic[s_list[left]] + 1
                    left = left + 1
            right = right + 1
        min_windows_len = sorted(min_dic)
        min_list = min_dic[min_windows_len[0]] if min_dic else []

        return "".join(min_list)

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
print(solution.minWindow("a", "a"))

