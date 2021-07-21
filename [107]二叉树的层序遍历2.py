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

from collections import deque
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
        q = deque([root])  # 双端队列q，用于某一层存储节点
        while q:  # 对队列进行遍历
            size = len(q)
            level = []  # 用于存储某一层的遍历结果
            for _ in range(size):
                cur = q.popleft()  # 将节点弹出
                level.append(cur.val)  # 将节点值存入level中
                if cur.left:  # 若当前节点存在左右子节点，将其加入q中
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)  # 将某层的遍历结果添加至最终结果中
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
