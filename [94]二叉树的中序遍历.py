# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#  示例 4：
#
#
# 输入：root = [1,2]
# 输出：[2,1]
#
#
#  示例 5：
#
#
# 输入：root = [1,null,2]
# 输出：[1,2]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表
#  👍 996 👎 0

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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:  #遍历顺序为左-根-右，利用栈找到最左的叶子
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

# leetcode submit region end(Prohibit modification and deletion)


