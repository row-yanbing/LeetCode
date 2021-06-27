# 给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
#  例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其自底向上的层序遍历为：
#
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 448 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        que = []
        cur = [root]
        while cur or que:
            tmp = []
            for node in cur:
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp)
            cur = que
            que = []
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
