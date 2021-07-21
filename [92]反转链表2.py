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
#  👍 955 👎 0

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def generate(self, vals: List):
        if not vals:
            return None
        head = ListNode(vals[0])
        cur = head
        for i in range(1, len(vals)):
            cur.next = ListNode(vals[i])
            cur = cur.next
        cur.next = None
        return head

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        count = 1
        pre = dummy
        if not head or not head.next:  # 如果链表非空或只有一个元素，则直接返回head
            return head
        while count < left:  # 找到left位置的前一个元素
            pre = pre.next
            count += 1
        cur = pre.next  # cur表示需要反转的元素
        tail = pre  # 将tail指针固定在left前一位置
        while cur.next and count < right:  # 遍历left至right之间的元素，利用头插法进行反转
            nxt = cur.next  # 储存cur的下一节点
            cur.next = nxt.next
            nxt.next = tail.next
            tail.next = nxt
            count += 1
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
listnode = ListNode()
l1 = listnode.generate([1,2,3,4,5])
k = solution.reverseBetween(l1,2,4)
while k:
    print(k.val)
    k = k.next

