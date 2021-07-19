# 给定两个二叉树，编写一个函数来检验它们是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  示例 1: 
# 
#  输入:       1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# 
# 输出: true 
# 
#  示例 2: 
# 
#  输入:      1          1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# 输出: false
#  
# 
#  示例 3: 
# 
#  输入:       1         1
#           / \       / \
#          2   1     1   2
# 
#         [1,2,1],   [1,1,2]
# 
# 输出: false
#  
#  Related Topics 树 深度优先搜索 
#  👍 487 👎
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # 树生成代码
    # def generate_tree(self, vals: List):
    #     if len(vals) == 0:
    #         return None
    #     que = []  # 定义队列
    #     root = []
    #     fill_left = True  # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
    #     for val in vals:
    #         node = TreeNode(val) if val else None  # 非空值返回节点类，否则返回 None
    #         if len(que) == 0:
    #             root = node  # 队列为空的话，用 root 记录根结点，用来返回
    #             que.append(node)
    #         elif fill_left:
    #             que[0].left = node
    #             fill_left = False  # 填充过左儿子后，改变记号状态
    #             if node:  # 非 None 值才进入队列
    #                 que.append(node)
    #         else:
    #             que[0].right = node
    #             if node:
    #                 que.append(node)
    #             que.pop(0)  # 填充完右儿子，弹出节点
    #             fill_left = True  #
    #     return root
    def generate_tree(self, vals: List):
        if not vals:
            return None
        root = TreeNode(vals[0])
        q = deque([root])
        i = 1
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if i < len(vals):
                    cur.left = TreeNode(vals[i])
                    q.append(cur.left)
                    i += 1
                if i < len(vals):
                    cur.right = TreeNode(vals[i])
                    q.append(cur.right)
                    i += 1
        return root


#  # 定义一个dfs打印中序遍历
#    def dfs(self, node):
#       if node is not None:
#           self.dfs(node.left)
#           print(node.val, end=' ')
#           self.dfs(node.right)
#    # 定义一个bfs打印层序遍历
#    def bfs(self, node):
#       que = []
#       que.append(node)
#       while que:
#           l = len(que)
#           for _ in range(l):
#               tmp = que.pop(0)
#               print(tmp.val, end=' ')
#               if tmp.left:
#                   que.append(tmp.left)
#               if tmp.right:
#                   que.append(tmp.right)
#           print('|', end=' ')
## test

# null = None
# vals = [3,9,20,null,null,15,7]
# vals = [3,9,20,null,null,15,7,8,9]
# tree1 = TreeNode.generate_tree(vals)
# tree2 = TreeNode.generate_tree(vals)
# print('中序遍历:')
# Btree.dfs(tree) # 9 3 15 20 7
# print('\n层序遍历:')
# Btree.bfs(tree) # 3 | 9 20 | 15 7 |


# leetcode submit region begin(Prohibit modification and deletion) # Definition for a binary tree node.

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# leetcode submit region end(Prohibit modification and deletion)
treeNode = TreeNode()
solution = Solution()
null = None
p1 = treeNode.generate_tree([1, 2, 2, null, 3, 4, null, null, null, 5])
p1 = treeNode.generate_tree([1, 2, 2, 3])
q1 = treeNode.generate_tree([1, 2, 2, 3])
p2 = treeNode.generate_tree([1, 2])
q2 = treeNode.generate_tree([1, null, 2])
p3 = treeNode.generate_tree([1, 1, 2])
q3 = treeNode.generate_tree([1, 2, 1])
print(solution.isSameTree(p1, q1))
print(solution.isSameTree(p2, q2))
print(solution.isSameTree(p3, q3))
