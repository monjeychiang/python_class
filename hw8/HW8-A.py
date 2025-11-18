# 檔案名稱： HW8-A.py
# 建立日期： 2025/11/18
# 檔案說明： 使用 Set (集合) 的特性，計算出總共會有多少位「不重複」的賓客會來參加。
# 編輯者： monjeychiang

# 讀取總共有 N 筆報名資料
n = int(input())

# 建立一個空的 set 來儲存不重複的賓客姓名
guests = set()

# 迴圈讀取 N 個姓名
for _ in range(n):
    # 讀取一個姓名並移除前後多餘的空白
    name = input().strip()
    # 將姓名加入 set，重複的姓名會被自動忽略
    guests.add(name)

# 輸出不重複的賓客總數
print(f"Unique guests: {len(guests)}")
