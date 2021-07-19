# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
#  你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#
#
#  示例 2：
#
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 200] 内
#  -100 <= Node.val <= 100
#  -200 <= x <= 200
#
#  Related Topics 链表 双指针
#  👍 423 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(0)  # 新建2个链表，将原链表分割成small和big两个
        p = small  # 将small的头传给p
        big = ListNode(0)
        q = big  # 将big链表头传给q
        move = head
        while move:  # 遍历原链表
            if move.val < x:  # 若链表元素小于x，则将元素添加到small中
                small.next = move
                small = small.next
            else:  # 若链表元素大于等于x，则将元素添加到big中
                big.next = move
                big = big.next
            move = move.next
        big.next = None  # 将big链表结尾截断
        small.next = q.next  # 将big链表添加到small链表尾部
        return p.next  # 返回small链表的头节点
# leetcode submit region end(Prohibit modification and deletion)
