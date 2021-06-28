# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
#  Related Topics 树 深度优先搜索 
#  👍 720 👎 0

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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root.val is None:
            return 0
        l = self.maxDepth(root.left)  # 计算左子树的深度
        r = self.maxDepth(root.right)  # 计算右子树的深度
        return max(l, r) + 1

# leetcode submit region end(Prohibit modification and deletion)