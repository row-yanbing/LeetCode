# 给定一个二叉树，找出其最小深度。
#
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
#  说明：叶子节点是指没有子节点的节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#
#
#
#
#  提示：
#
#
#  树中节点数的范围在 [0, 105] 内
#  -1000 <= Node.val <= 1000
#
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 523 👎 0
from collections import deque
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # 树生成代码
    def generate_tree(self, vals:List):
        if len(vals) == 0:
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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l = self.minDepth(root.left)  # 左子树的最小深度
        r = self.minDepth(root.right)  # 右子树的最小深度
        # 当左子树或右子树为空时，或者两者均为空时，l=0，或r=0，或者l=r=0，因此返回l+r+1
        if not (root.right and root.left):
            return l + r + 1
        # 当左右子树都不为空时，返回最小值+1
        return min(l, r) + 1
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
