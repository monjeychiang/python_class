# 檔案名稱：HW12-E.py
# 建立日期：2025/12/16
# 檔案說明：學生成績分析器（List of Dict、靜態方法、實體方法）
# 編寫者：monjeychiang


class Stats:
    @staticmethod
    def calculate_avg(scores):
        if not scores:
            return 0.0
        return sum(scores) / len(scores)


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        return Stats.calculate_avg(self.scores)


def main():
    command_count = int(input())
    students = {}

    for _ in range(command_count):
        parts = input().split()
        cmd = parts[0]
        name = parts[1]

        if cmd == "add":
            score = float(parts[2])
            if name not in students:
                students[name] = Student(name)
            students[name].add_score(score)
        elif cmd == "query":
            # 假設查詢前一定已新增過該學生
            avg = students[name].get_average()
            print(f"{name} Average: {avg:.1f}")


if __name__ == "__main__":
    main()
