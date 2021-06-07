# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 1079 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None

    def generate_tree(self,vals):
        if len(vals) == 0:
            return None
        que = []
        root = []
        left_fill = True
        for val in vals:
            node = TreeNode(val) if val else None
            if len(que) == 0:
                root = node
                que.append(node)
            elif left_fill:
                que[0].left = node
                left_fill = False
                if node:
                    que.append(node)
            else:
                que[0].right = node
                if node:
                    que.append(node)
                que.pop(0)
                left_fill = True
        return root


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def dfs(right,left):
            if not right and not left:
                return True
            if not(right and left):
                return False
            if right.val != left.val:
                return False
            elif dfs(right.right,left.left) and dfs(right.left,left.right):
                return True
        return dfs(root.right,root.left)
# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
treenode = TreeNode()
null = None
a1 = [1,2,2,3,4,4,3]
a2 =[1,2,2,null,3,null,3]
tree1 = treenode.generate_tree(a1)
tree2 = treenode.generate_tree(a2)
print(solution.isSymmetric(tree1))
print(solution.isSymmetric(tree2))
