# 翻转一棵二叉树。
#
#  示例：
#
#  输入：
#
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#  输出：
#
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#  备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
#  Related Topics 树
#  👍 891 👎 0
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def generate_tree(self, vals: List):
        if len(vals) != 0:
            root = TreeNode(vals[0])
            nodes = [root]
            count = 1
            while nodes and count < len(vals):
                node = nodes[0]
                node.left = TreeNode(vals[count])
                nodes.append(node.left)
                node.right = TreeNode(vals[count + 1]) if count + 1 < len(vals) else None
                nodes.append(node.right)
                count += 2
                nodes.pop(0)
            return root
        else:
            return None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
treenode = TreeNode()
print(solution.invertTree(treenode.generate_tree([4,2,7,1,3,6,9])))
