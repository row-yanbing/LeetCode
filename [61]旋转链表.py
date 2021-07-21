# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
#
#  示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 500] 内
#  -100 <= Node.val <= 100
#  0 <= k <= 2 * 109
#
#  Related Topics 链表 双指针
#  👍 586 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)  # 建立哑节点
        n = 0
        fast = head
        slow = head
        lenghth = head
        while lenghth.next:  # 计算链表的长度
            n += 1
            lenghth = lenghth.next
        count = k % n  # 计算需要移动的距离
        while count:  # 利用快慢指针移动，快指针比慢指针多走k%n步
            fast = fast.next
            count -= 1
        while fast.next:  # 让快指针到达链表尾部
            fast = fast.next
            slow = slow.next
        dummy.next = slow.next  # 将新的链表头添加至dummy上
        slow.next = None  # 截断链表
        fast.next = head  # 将头节点加入到链表尾部
        return dummy.next  # 返回新的链表头

# leetcode submit region end(Prohibit modification and deletion)
