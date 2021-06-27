# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
#  假设一个二叉搜索树具有如下特征：
#
#
#  节点的左子树只包含小于当前节点的数。
#  节点的右子树只包含大于当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#
#
#  示例 2:
#
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
#  Related Topics 树 深度优先搜索 递归
#  👍 1101 👎 0
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
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isvalidbst(root, float('-inf'), float('inf'))

    def isvalidbst(self, root, min, max):
        if not root or root.val is None: #注意要判定树为空，比较特殊，要么没有元素，要么根节点值为空
            return True
        mid = root.val
        if mid <= min or mid >= max:
            return False
        return self.isvalidbst(root.left, min, mid) and self.isvalidbst(root.right, mid, max)


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
treenode = TreeNode()
null = None
p1 = [2147483647]
p1_tree = treenode.generate_tree(p1)
p2 = [0, null, -1]
p2_tree = treenode.generate_tree(p2)

print(solution.isValidBST(p1_tree))
print(solution.isValidBST(p2_tree))
