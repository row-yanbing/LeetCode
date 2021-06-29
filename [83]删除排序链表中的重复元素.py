# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
#
#  返回同样按升序排列的结果链表。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,1,2]
# 输出：[1,2]
#
#
#  示例 2：
#
#
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
#
#
#
#
#  提示：
#
#
#  链表中节点数目在范围 [0, 300] 内
#  -100 <= Node.val <= 100
#  题目数据保证链表已经按升序排列
#
#  Related Topics 链表
#  👍 597 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow = head
        fast = head.next
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head
# leetcode submit region end(Prohibit modification and deletion)
