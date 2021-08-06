# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成
# 了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon
# 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
#
#  在结果列表中，选择 字典序最小 的名字作为真实名字。
#
#
#
#  示例：
#
#
# 输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], syn
# onyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
# 输出：["John(27)","Chris(36)"]
#
#
#
#  提示：
#
#
#  names.length <= 100000
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 哈希表 字符串 计数
#  👍 44 👎 0


# leetcode submit region begin(Prohibit modification and deletion
from collections import defaultdict

class Unionfind(object):
    def __init__(self, names):
        self.parent = defaultdict(int)
        for name in names:
            self.parent[name] = name

    def union(self, a, b):
        if a not in self.parent:
            self.parent[a] = a
        if b not in self.parent:
            self.parent[b] = b
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a < root_b:
            self.parent[root_b] = root_a
        elif root_a > root_b:
            self.parent[root_a] = root_b

    def find_root(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        name = []
        name_freq = defaultdict(int)
        for k in names:
            a, b = k.split('(')
            name_freq[a] = int(b.strip(')'))
            name.append(a)
        uf = Unionfind(name)
        for k in synonyms:
            a, b = k.strip('(').strip(')').split(',')
            uf.union(a,b)
        res = {}
        for k,v in uf.parent.items():
            if v not in res:
                res[v] = name_freq[k]
            else:
                res[v] += name_freq[k]
        result = []
        for k, v in res.items():
            result.append(str(k)+'('+str(v)+')')
        return result
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
res = solution.trulyMostPopular(names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"],synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"])
print(res)