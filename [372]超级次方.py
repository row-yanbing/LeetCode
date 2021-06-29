# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
#
#
#
#  示例 1：
#
#
# 输入：a = 2, b = [3]
# 输出：8
#
#
#  示例 2：
#
#
# 输入：a = 2, b = [1,0]
# 输出：1024
#
#
#  示例 3：
#
#
# 输入：a = 1, b = [4,3,3,8,5,2]
# 输出：1
#
#
#  示例 4：
#
#
# 输入：a = 2147483647, b = [2,0,0]
# 输出：1198
#
#
#
#
#  提示：
#
#
#  1 <= a <= 231 - 1
#  1 <= b.length <= 2000
#  0 <= b[i] <= 9
#  b 不含前导 0
#
#  Related Topics 数学 分治
#  👍 117 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        tmp = b.pop()  # 取b的末位元素
        ans1 = self.mypow(self.superPow(a, b), 10, 1337) #将a**b进行拆解，分为ans1和ans2两个子问题，同时进行取模，避免溢出
        ans2 = self.mypow(a, tmp, 1337)
        result = ans1 * ans2 % 1337 # 再次取模，避免溢出
        return result


    def mypow(self,a, b, k):
        res = 1
        i = 1
        while i <= b: #利用循环求a**b, 在过程中取模，避免溢出
            res = res * a % k
            i += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.superPow(2,[3]))
print(solution.superPow(2,[1, 0]))
print(solution.superPow(1,[4,3,3,8,5,2]))
print(solution.superPow(2147483647,[2,0,0]))
