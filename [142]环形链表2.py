# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，po
# s 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
#
#  说明：不允许修改给定的链表。
#
#  进阶：
#
#
#  你是否可以使用 O(1) 空间解决此题？
#
#
#
#
#  示例 1：
#
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#  示例 2：
#
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#  示例 3：
#
#
#
#
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#
#
#
#
#  提示：
#
#
#  链表中节点的数目范围在范围 [0, 104] 内
#  -105 <= Node.val <= 105
#  pos 的值为 -1 或者链表中的一个有效索引
#
#  Related Topics 哈希表 链表 双指针
#  👍 1074 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast = slow = head
        while fast and fast.next:  # 利用快慢指针判断链表是否存在环路
            fast = fast.next.next
            slow = slow.next
            if fast == slow:  # 若存在环路，将慢指针指向头结点，快慢指针同速度前进，再次相遇时即为环的起点
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
# leetcode submit region end(Prohibit modification and deletion)
