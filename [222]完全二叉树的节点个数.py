# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#
#  完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层
# 为第 h 层，则该层包含 1~ 2h 个节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：0
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：1
#
#
#
#
#  提示：
#
#
#  树中节点的数目范围是[0, 5 * 104]
#  0 <= Node.val <= 5 * 104
#  题目数据保证输入的树是 完全二叉树
#
#
#
#
#  进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
#  Related Topics 树 二分查找
#  👍 500 👎 0

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def generate_tree(self, vals: List):
        if len(vals) != 0:
            root = TreeNode(vals[0])
            nodes = [root]
            count = 1
            while nodes and count < len(vals):
                node = nodes[0]
                node.left = TreeNode(vals[count])
                nodes.append(node.left)
                node.right = TreeNode(vals[count + 1]) if count + 1 < len(vals) else None
                nodes.append(node.right)
                count += 2
                nodes.pop(0)
            return root
        else:
            return None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = root
        r = root
        hl = 0
        hr = 0
        while l is not None:
            hl += 1
            l = l.left
        while r is not None:
            hr += 1
            r = r.right
        if hl == hr:
            return 2**hr - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
treenode = TreeNode()
print(solution.countNodes(treenode.generate_tree([1,2,3,4,5,6])))
print(solution.countNodes(treenode.generate_tree([1])))
print(solution.countNodes(treenode.generate_tree([])))
