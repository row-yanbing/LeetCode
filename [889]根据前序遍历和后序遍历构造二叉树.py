# 返回与给定的前序和后序遍历匹配的任何二叉树。
#
#  pre 和 post 遍历中的值是不同的正整数。
#
#
#
#  示例：
#
#  输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#
#
#
#
#  提示：
#
#
#  1 <= pre.length == post.length <= 30
#  pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
#  每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
#
#  Related Topics 树 数组 哈希表 分治 二叉树
#  👍 177 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post: # 若为空，则返回None
            return
        root = TreeNode(pre[0])  #将根节点放入
        if len(pre) == 1:  # 若只有一个元素，则直接返回根节点
            return root
        idx = post.index(pre[1]) #找到根节点索引值
        root.left = self.constructFromPrePost(pre[1:idx+2], post[:idx+1]) # 递归创建左子树
        root.right = self.constructFromPrePost(pre[idx+2:], post[idx+1:-1]) # 递归创建右子树
        return root
# leetcode submit region end(Prohibit modification and deletion)
