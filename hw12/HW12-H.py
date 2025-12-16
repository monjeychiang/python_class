# 檔案名稱：HW12-H.py
# 建立日期：2025/12/16
# 檔案說明：選課系統（時間衝突 Tuple、課程 Set、課程 Dict）
# 編寫者：monjeychiang


class Course:
    def __init__(self, course_id, day, time, capacity):
        self.course_id = course_id
        self.capacity = capacity
        self.students = set()
        self.schedule = (day, time)  # Tuple: (Day, Time)

    def is_full(self):
        return len(self.students) >= self.capacity

    def add_student(self, student_name):
        self.students.add(student_name)


class Student:
    def __init__(self, name):
        self.name = name
        self.my_courses = []  # List of Course objects

    def has_conflict(self, course):
        for c in self.my_courses:
            if c.schedule == course.schedule:
                return True
        return False

    def register(self, course):
        self.my_courses.append(course)


def register(student, course):
    if course.is_full():
        print("Full")
        return

    if student.has_conflict(course):
        print("Time Conflict")
        return

    course.add_student(student.name)
    student.register(course)
    print("Success")


def main():
    command_count = int(input())
    courses = {}
    students = {}

    for _ in range(command_count):
        parts = input().split()
        cmd = parts[0]

        if cmd == "add_course":
            course_id, day, time, capacity_str = parts[1], parts[2], parts[3], parts[4]
            courses[course_id] = Course(course_id, day, time, int(capacity_str))
        elif cmd == "register":
            student_name, course_id = parts[1], parts[2]
            course = courses.get(course_id)
            if course is None:
                continue  # 若課程不存在，題目未定義，直接忽略

            if student_name not in students:
                students[student_name] = Student(student_name)
            student = students[student_name]

            register(student, course)


if __name__ == "__main__":
    main()
