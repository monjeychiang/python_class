# 檔案名稱： HW8-F.py
# 建立日期： 2025/11/18
# 檔案說明： 使用巢狀字典儲存及查詢學生成績。
# 編輯者： monjeychiang

# 讀取成績資料筆數 N
n = int(input())

# 建立一個空的巢狀字典來儲存成績
grades = {}

# 迴圈讀取 N 筆成績資料
for _ in range(n):
    # 讀取一行，並用空格分割成姓名、科目和成績
    name, subject, score_str = input().strip().split()
    score = int(score_str)
    
    # 檢查學生姓名是否已在外層字典中
    if name not in grades:
        # 如果不在，為該學生建立一個新的空字典
        grades[name] = {}
    
    # 將科目和成績存入對應學生的內層字典
    grades[name][subject] = score

# 讀取查詢筆數 M
m = int(input())

# 迴圈讀取 M 筆查詢
for _ in range(m):
    # 讀取要查詢的姓名和科目
    query_name, query_subject = input().strip().split()
    
    # 從巢狀字典中找出對應的成績並印出
    print(grades[query_name][query_subject])
