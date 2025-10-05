class GradeManager:
    def __init__(self):
        self.g = {}
    def add(self,name,score):
        self.g[name] = score
        print(f"已添加学生：{name},成绩：{score}")
    def remove(self,name):
        result = self.g.pop(name,None)
        if result is None:
            print("没这人")
        else:
            print(f"删除成功，这人成绩是:{result}")
    def update(self,name,score):
        if name in self.g:
            self.g[name] = score
            print(f"更新成功，{name}的新成绩是:{score}")
        else:
            print("更新失败，压根没这人")
    def average(self):
        if not self.g :
            print(0)
        else:
            total = sum(self.g.values())
            number = len(self.g.keys())
        print(f"你们学生的平均成绩为{total/number}")
    def max_min(self):
        if not self.g:
            print("没这人")
        else:
            max_scores  = max(self.g.values())
            min_scores = min(self.g.values())
            max_students = max(self.g, key=self.g.get)
            min_students = min(self.g, key=self.g.get)
            print(f"最高分学生是{max_students}，{max_scores}分")
            print(f"最低分学生是{min_students}，{min_scores}分")
gm = GradeManager()
gm.add("龟乌儿",591)
gm.add("柄",750)
gm.remove("张硕")
gm.update("sb",1)
gm.average()
gm.max_min()