# 檔案名稱： HW8-H.py
# 建立日期： 2025/11/18
# 檔案說明： 根據會員興趣進行分組與查詢。
# 編輯者： monjeychiang

# 讀取資料筆數 N
n = int(input())

# 建立一個空的字典來儲存興趣分組
interest_groups = {}

# 迴圈讀取 N 筆會員興趣資料
for _ in range(n):
    # 讀取一行，並用空格分割成姓名和興趣
    name, interest = input().strip().split()
    
    # 檢查興趣是否已在字典中
    if interest not in interest_groups:
        # 如果不在，為該興趣建立一個新的空集合
        interest_groups[interest] = set()
    
    # 將會員姓名加入對應興趣的集合中
    interest_groups[interest].add(name)

# 讀取查詢筆數 M
m = int(input())

# 迴圈讀取 M 筆查詢
for _ in range(m):
    # 讀取要查詢的興趣名稱
    query_interest = input().strip()
    
    # 從字典中找出對應的會員集合
    members_set = interest_groups.get(query_interest, set())
    
    # 將集合轉換為列表並按字母順序排序
    sorted_members = sorted(list(members_set))
    
    # 印出排序後的會員列表
    print(sorted_members)
