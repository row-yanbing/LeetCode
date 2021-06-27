# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
#  提示：
#
#
#  链表中节点数目为 n
#  1 <= n <= 500
#  -500 <= Node.val <= 500
#  1 <= left <= right <= n
#
#
#
#
#  进阶： 你可以使用一趟扫描完成反转吗？
#  Related Topics 链表
#  👍 930 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        dummy =ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and count < left: #定位到left位置
            pre = pre.next
            count += 1
        cur = pre.next #当pre指针到left前一个元素时，将cur指针指向left处元素
        tail = cur #将尾指针固定在left元素
        while cur and count <= right:
            nxt = cur.next #nxt指针随着cur指针往后滑动
            cur.next = pre.next #当移到left+1元素处，此时与left处(pre.next)的元素进行反转
            pre.next = cur #将pre指针指向交换过来的元素，以此类推，依次将后面left+2至right的元素移到pre.next处
            tail.next = nxt #将尾指针指向nxt
            cur = nxt #将cur指针后移
            count += 1
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
