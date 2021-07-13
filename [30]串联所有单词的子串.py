# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
#
#
#
#  示例 1：
#
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#
#
#  示例 2：
#
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 104
#  s 由小写英文字母组成
#  1 <= words.length <= 5000
#  1 <= words[i].length <= 30
#  words[i] 由小写英文字母组成
#
#  Related Topics 哈希表 字符串 滑动窗口
#  👍 499 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        dic = {}  #建立一个字典，用于存储words
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        length = len(words[0])*len(words) # words的总长度
        k = len(words[0])  # 每个单词的长度，也是每次搜索的步长
        if len(s) < length:  # 排除不合法的输入
            return []
        left = 0  # 滑动窗口的起始位置
        while left + length <= len(s):  # 当滑动窗口右端小于字符串长度时，进行搜索
            dic1 = dic.copy()  # 每次搜索要进行对比，出现改词，则减少1，注意要用copy，否则会改变原来的dic
            for i in range(left, left+length, k):  # 在滑动窗口内部进行搜索，搜索步长为k
                if s[i:i+k] not in dic1:  # 如果出现陌生词，则直接结束搜索
                    break
                else:
                    if dic1[s[i:i+k]] > 0:  # 若字典中该词出现的次数大于0，则减少1
                        dic1[s[i:i+k]] -= 1
                    else:  # 若字典中该词出现的次数小于0，则说明窗口中该词出现次数过多，则结束搜索
                        break
            else:  # 若搜索正常退出，则表明窗口内的字符串符合条件，将窗口起点加入结果
                res.append(left)
            left += 1  # 窗口向右滑动1，注意不能是k
        return res

# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))
print(solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]))
print(solution.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
