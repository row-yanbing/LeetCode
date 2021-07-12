# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
#
#
#  示例 1：
#
#
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
#
#
#  示例 2：
#
#
# 输入：head = [], val = 1
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
#
#
#
#
#  提示：
#
#
#  列表中的节点数目在范围 [0, 104] 内
#  1 <= Node.val <= 50
#  0 <= val <= 50
#
#  Related Topics 递归 链表
#  👍 654 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            next_node = head.next
        else:
            next_node = head
        return next_node
# leetcode submit region end(Prohibit modification and deletion)
