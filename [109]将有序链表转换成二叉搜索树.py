# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
#  示例:
#
#  给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  Related Topics 树 二叉搜索树 链表 分治 二叉树
#  👍 554 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        pre, slow, fast = None, head, head
        while fast and fast.next:  # 用快慢指针找到链表的中间节点
            fast = fast.next.next
            pre = slow  # 用pre指针记录中间节点前一节点
            slow = slow.next
        if pre:  # 将链表断开
            pre.next = None
        root = TreeNode(slow.val)  # 以中间节点为根节点建树
        if slow == fast:  # 子树建立完毕，返回根节点
            return root
        root.left = self.sortedListToBST(head)  # 递归建左子树
        root.right = self.sortedListToBST(slow.next)  # 递归建右子树
        return root  # 返回根节点

# leetcode submit region end(Prohibit modification and deletion)
