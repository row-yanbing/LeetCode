# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。”
#
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#
#
#  示例 1:
#
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
#
#  示例 2:
#
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#
#
#
#  说明:
#
#
#  所有节点的值都是唯一的。
#  p、q 为不同节点且均存在于给定的二叉树中。
#
#
#  注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a
# -binary-tree/
#  Related Topics 树
#  👍 277 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: #如果root为空，或者root等于p，q其中之一，则直接返回root
            return root
        left = self.lowestCommonAncestor(root.left, p, q) #在左子树寻找
        right = self.lowestCommonAncestor(root.right, p, q) #在右子树寻找
        if not left:  #若左子树没有，则在右子树中
            return right
        if not right: #若右子树没有，则在左子树中
            return left
        if not left and not right:#如果都不在，则返回None（本题给出此种情况不存在）
            return None
        if left and right: #如果分别在左右子树中，则返回当前根节点
            return root #由于是后序遍历，最先返回的就是最近公共祖先
# leetcode submit region end(Prohibit modification and deletion)
