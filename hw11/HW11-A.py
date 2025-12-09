# 檔案名稱：HW11-A.py
# 建立日期：2025/12/09
# 檔案說明：員工證號自動生成系統（類別屬性 vs 實體屬性）
# 編寫者：monjeychiang


class Employee:
    # 類別屬性：全公司共享的總員工數與下一個可用 ID
    total_employees = 0
    next_id = 1

    def __init__(self, name):
        # 實體屬性：每位員工各自的名字與 ID
        self.name = name
        self.id = Employee.next_id

        # 建立新員工時更新類別屬性
        Employee.total_employees += 1
        Employee.next_id += 1


# 讀取要建立的員工數量 N
n = int(input())

# 依序讀取 N 筆員工姓名並建立員工物件
for _ in range(n):
    name = input().strip()
    employee = Employee(name)
    # 每建立一位員工就輸出對應資訊
    print(f"{employee.name} ID: {employee.id}, Total Staff: {Employee.total_employees}")
