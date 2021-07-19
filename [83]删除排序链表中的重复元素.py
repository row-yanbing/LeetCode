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
        slow = head  # 设置慢指针
        fast = head.next  # 设置快指针
        while fast:  # 遍历链表
            if fast.val != slow.val:  # 若不存在重复元素
                slow.next = fast  # 将慢指针的下一跳指向fast
                slow = slow.next  # 移动慢指针
            fast = fast.next  # 移动fast指针
        slow.next = None  # 将慢指针尾部截断
        return head
# leetcode submit region end(Prohibit modification and deletion)
