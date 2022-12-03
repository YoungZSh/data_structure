import pandas as pd


class GraphStack:
    def __init__(self) -> None:
        self.list = []

    def push(self, G):
        self.list.append(G)
        return None

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    def top(self):
        return self.list[self.size() - 1]


class AdjVexNode:
    def __init__(self, adjvex=None, next=None) -> None:
        self.adjvex = adjvex
        self.next = next


class VexNode:
    def __init__(self) -> None:
        self.id = None
        self.credit = None
        self.indegree = 0
        self.fst_adjvex = None


class Graph:
    def __init__(self) -> None:
        self.term_num = None
        self.max_credits = None
        self.course_num = 0
        self.vex_list = []
        self.result = []
        self.arrangement = []

    def switch(self, id):
        pos = id.strip("C")
        return int(pos)

    def read_file(self):
        df_basic = pd.read_json(r"course_arrangement\basic_info.json")
        df_course = pd.read_csv(r"course_arrangement\course_info.csv", index_col=0)
        self.term_num = df_basic.iloc[0, 0]
        self.max_credits = df_basic.iloc[0, 1]
        self.course_num = df_basic.iloc[0, 2]
        self.vex_list = [VexNode() for _ in range(self.course_num)]
        for i in range(self.course_num):
            self.vex_list[i].id = df_course.iloc[i, 0]
            self.vex_list[i].credit = df_course.iloc[i, 1]
            pre = df_course.iloc[i, 2]
            if pre == pre:
                pre_course = pre.split(" ")
                for course in pre_course:
                    node = AdjVexNode(self.switch(course), self.vex_list[i].fst_adjvex)
                    self.vex_list[i].fst_adjvex = node
        for vex in self.vex_list:
            tmp = vex.fst_adjvex
            while True:
                if tmp != None:
                    self.vex_list[tmp.adjvex - 1].indegree += 1
                    tmp = tmp.next
                else:
                    break
        return None

    def top_sort(self):
        flag = 0
        S1 = GraphStack()
        S2 = GraphStack()
        self.read_file()
        while flag == 0:
            flag = 1
            for vex in self.vex_list:
                if vex.indegree == 0:
                    S1.push(vex)
                    vex.indegree -= 1
                    S2.push(vex.fst_adjvex)
                    flag = 0
            while S2.isEmpty() == False:
                p = S2.pop()
                while p != None:
                    self.vex_list[p.adjvex - 1].indegree -= 1
                    p = p.next
        if S1.size() < self.course_num:
            print("拓扑排序失败")
        for _ in range(S1.size()):
            self.result.append(S1.pop())

        return None

    def arrange(self, choice):
        if choice == 1:
            if self.course_num % self.term_num < self.term_num / 2:
                max_courses = self.course_num / self.term_num
            else:
                max_courses = self.course_num / self.term_num + 1
        else:
            max_courses = 9999
        arranged = []
        i = 0
        while len(arranged) < self.course_num:
            cur_credits = 0
            cur_arranged = []
            while len(cur_arranged) < max_courses and cur_credits < self.max_credits:
                if len(arranged) == self.course_num:
                    list = []
                    for _ in cur_arranged:
                        list.append(_.id)
                    self.arrangement.append(list)
                    return None
                p = self.result[i].fst_adjvex
                flag = False
                while p != None:
                    for course in cur_arranged:
                        if self.switch(course.id) == p.adjvex:
                            flag = True
                            break
                    if flag == True:
                        break
                    p = p.next
                if flag == False:
                    if (
                        len(cur_arranged) >= max_courses
                        or cur_credits + self.result[i].credit > self.max_credits
                    ):
                        break
                    cur_arranged.append(self.result[i])
                    arranged.append(self.result[i])
                    cur_credits += self.result[i].credit
                    i += 1
                else:
                    break
            list = []
            for _ in cur_arranged:
                list.append(_.id)
            self.arrangement.append(list)
        return None


"""
C1
C9
C2
C11
C4
C3
C10
C6
C5
C12
C8
C7
"""
