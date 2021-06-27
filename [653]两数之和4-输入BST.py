# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
#  案例 1:
#
#
# 输入:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# 输出: True
#
#
#
#
#  案例 2:
#
#
# 输入:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# 输出: False
#
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 哈希表 双指针 二叉树
#  👍 247 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []
        self.inordertra(root, res)#用中序遍历二叉搜索树，得到有序数组，再用双指针遍历
        left, right = 0, len(res)-1
        while left<right:
            if res[left] + res[right] < k:
                left += 1
            elif res[left] + res[right] > k:
                right -= 1
            else:
                return True
        return False

    def inordertra(self, root, track):#中序遍历得到有序数组
        if not root:
            return None
        self.inordertra(root.left, track)
        track.append(root.val)
        self.inordertra(root.right, track)
        return track
# leetcode submit region end(Prohibit modification and deletion)
