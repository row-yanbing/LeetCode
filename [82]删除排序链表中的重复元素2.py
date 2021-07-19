# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
#
#  返回同样按升序排列的结果链表。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
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
#  Related Topics 链表 双指针
#  👍 660 👎 0


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)  # 建立一个哑结点
        dummy.next = head  # 将哑结点指向头结点
        pre = dummy  # 将慢指针指向哑结点
        cur = head  # 将快指针指向head节点
        while cur and cur.next:  # 遍历链表
            if cur.val == cur.next.val:  # 若存在重复元素
                while cur.next and cur.val == cur.next.val:  # 将重复的元素丢弃，直到遇到不重复的
                    cur.next = cur.next.next
                pre.next = cur.next  # 将pre指针的下一跳指向第一个不重复的元素
            else:  # 若不存在重复元素
                pre = cur  # 将cur节点指向dummy节点
            cur = cur.next  # cur指针后移
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
h = [1, 1, 1, 2, 3]
head = ListNode(h[0])
cur = head
for v in h[1:]:
    cur.next = ListNode(v)
    cur = cur.next

solution = Solution()
res = solution.deleteDuplicates(head)
while res:
    print(res)
    res = res.next
