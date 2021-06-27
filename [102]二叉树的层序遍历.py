# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层序遍历结果：
#
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 904 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root] #用于存储当前一层节点
        que = [] #用于临时存储孩子节点
        while cur or que:
            tmp = [] #用于临时存储当前一层的节点根值
            for node in cur:
                tmp.append(node.val) #将节点的根值临时存起来
                if node.left: #如果存在孩子节点，则将其加入到que中临时存储，用于下一轮遍历
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp) #将一层的节点根值存入结果
            cur = que #cur指向下一层节点，即之前存储的孩子节点
            que = [] #将队列清空
        return res
# leetcode submit region end(Prohibit modification and deletion)
