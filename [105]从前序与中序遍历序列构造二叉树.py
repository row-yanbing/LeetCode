# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  Related Topics 树 数组 哈希表 分治算法 二叉树
#  👍 1089 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0]) #先序为根左右，故先确定根的位置
        idx = inorder.index(preorder[0]) #找到中序中root的位置，划分左右子树
        root.left = self.buildTree(preorder[1:1+idx],inorder[:idx]) #递归构建左右子树
        root.right = self.buildTree(preorder[1+idx:],inorder[idx+1:])
        return root
# leetcode submit region end(Prohibit modification and deletion)
