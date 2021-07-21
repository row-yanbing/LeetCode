# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
#  本题中，一棵高度平衡二叉树定义为：
#
#
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：true
#
#
#
#
#  提示：
#
#
#  树中的节点数在范围 [0, 5000] 内
#  -104 <= node.val <= 104
#
#  related topics 树 深度优先搜索 二叉树
#  👍 713 👎 0


# leetcode submit region begin(prohibit modification and deletion)
# definition for a binary tree node.
# class treenode:
#     def __init__(self, val=0, left=none, right=none):
#         self.val = val
#         self.left = left
#         self.right = right
class solution:
    def isbalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        return self.isbalanced(root.left) and self.isbalanced(root.right)
        #如果左右子树高度差<=1，且左右子树都是平衡树，则为平衡树

    def depth(self, root) -> int:  # 计算树的高度
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

# leetcode submit region end(prohibit modification and deletion)
