# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层序遍历结果：
#
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 904 👎 0

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def generate_tree(self,vals):
        if not vals:
            return None
        root = TreeNode(vals[0])
        q = deque([root])
        i = 1
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if i < len(vals) and vals[i]:
                    cur.left = TreeNode(vals[i])
                    q.append(cur.left)
                i += 1
                if i < len(vals) and vals[i]:
                    cur.right = TreeNode(vals[i])
                    q.append(cur.right)
                i += 1
        return root

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root]) #用于存储当前一层节点
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res
# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
treenode = TreeNode()
null = None
tree1 = treenode.generate_tree([3,9,20,null,null,15,7])
print(solution.levelOrder(tree1))