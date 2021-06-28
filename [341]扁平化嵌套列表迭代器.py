# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
#
#  列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
#
#
#
#  示例 1:
#
#  输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
#
#  示例 2:
#
#  输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
#
#  Related Topics 栈 树 深度优先搜索 设计 队列 迭代器
#  👍 345 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]  # 当前列表的各个元素（不用摊平）逆序放入栈中


    """
    在 Next()方法中，调用getInteger方法，并弹出栈顶元素：
    """
    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()

    """
    在 hasNext()方法中，访问（不弹出）栈顶元素，判断是否为 int：
    如果是 int 那么说明有下一个元素，返回 true；然后 next() 就会被调用，把栈顶的 int 弹出；
    如果是 list 需要把当前列表的各个元素（不用摊平）逆序放入栈中。
    如果栈为空，那么说明原始的嵌套列表已经访问结束了，返回 false。
    """
    def hasNext(self):
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()  # 先弹出该列表元素，再将该列表中的元素逆序添加进来
            self.stack.extend(cur.getList()[::-1])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# leetcode submit region end(Prohibit modification and deletion)
