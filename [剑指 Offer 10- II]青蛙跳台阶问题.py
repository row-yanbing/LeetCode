#上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
#  示例 1： 
#  输入：n = 2
# 输出：2
#  示例 2： 
#  输入：n = 7
# 输出：21
#  示例 3： 
#
#  输入：n = 0
# 输出：1 
# 
#  提示： 
#  0 <= n <= 100 
#  注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/ 
# 
#
#  Related Topics 递归 
#  👍 74 👎 0
# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    
    def numWays(self, n: int) -> int:
    if n == 0
    return 1
    if n == 1
    return 1
    result=self.numWays(n-1)+self.numWays(n-2)

# leetcode submit region end(Prohibit modification and deletion)
print(Solution.numWays(0))
print(Solution.numWays(2))
print(Solution.numWays(7))
