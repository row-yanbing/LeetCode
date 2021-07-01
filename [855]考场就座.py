# 在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。
#
#  当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，
# 那么学生就坐在 0 号座位上。)
#
#  返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位
# 置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。每次调用 ExamRoom.leave(p) 时都保证有学生坐在
# 座位 p 上。
#
#
#
#  示例：
#
#  输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[]
# ,[4],[]]
# 输出：[null,0,9,4,2,null,5]
# 解释：
# ExamRoom(10) -> null
# seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
# seat() -> 9，学生最后坐在 9 号座位上。
# seat() -> 4，学生最后坐在 4 号座位上。
# seat() -> 2，学生最后坐在 2 号座位上。
# leave(4) -> null
# seat() -> 5，学生最后坐在 5 号座位上。
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#  在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
#  保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。
#
#  Related Topics 设计 有序集合
#  👍 88 👎 0

import bisect
# leetcode submit region begin(Prohibit modification and deletion)
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []  # 有序数列，记录现有学生的位置

    def seat(self) -> int:
        if not self.students:  # 如果还没有学生，则让其作在第一个位置
            student = 0
        else:
            max_dist, student = self.students[0], 0  # 初始化最大间隔max_dist，学生入座位置
            for i, s in enumerate(self.students):  # 遍历之前的所有学生位置，找出现有间隔最远的
                if i:
                    pre = self.students[i-1]
                    d = (s - pre)//2  # 计算出学生i和即将安排在[i-1,i]之间学生的间隔，除以2表示将学生安排在[i-1,i]中间
                    if d > max_dist:  # 如果计算出的间隔大于之前的最大间隔，将学生安排在这两者中间
                        max_dist = d  # 更新最大间隔的值
                        student = pre + d  # 计算出将要安排的学生位置
            d = self.n - 1 - self.students[-1]  # 计算最后一个学生与最后一个位置的间隔
            if d > max_dist:  # 如果该间隔大于之前的最大间隔，则将学生安排到最后一个位置
                student = self.n - 1  # 将学生安排在最后一个位置
        bisect.insort(self.students, student)  # 将学生的位置按照顺序添加进有序数列中
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)   # 移除学生p



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
# leetcode submit region end(Prohibit modification and deletion)
