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
        que = [] # 定义队列
        root = []
        fill_left = True # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
        for val in vals:
            node = TreeNode(val) if val else None # 非空值返回节点类，否则返回 None
            if len(que)==0:
                root = node # 队列为空的话，用 root 记录根结点，用来返回
                que.append(node)
            elif fill_left:
                que[0].left = node
                fill_left = False # 填充过左儿子后，改变记号状态
                if node: # 非 None 值才进入队列
                    que.append(node)
            else:
                que[0].right = node
                if node:
                    que.append(node)
                que.pop(0) # 填充完右儿子，弹出节点
                fill_left = True #
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
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if root.right and not root.left:
            return r + 1
        if not root.right and root.left:
            return l + 1
        return min(l, r) + 1
# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
