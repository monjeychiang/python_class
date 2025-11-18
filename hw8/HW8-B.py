# 檔案名稱： HW8-B.py
# 建立日期： 2025/11/18
# 檔案說明： 水果攤的快速價格查詢系統。
# 編輯者： monjeychiang

# 讀取 N，代表建立字典的資料筆數
n = int(input())

# 建立一個空的字典來儲存水果價格
prices = {}

# 迴圈讀取 N 筆水果資料
for _ in range(n):
    # 讀取一行，移除前後空白，並用空格分割成水果名稱和價格
    name, price = input().strip().split()
    # 將水果資料加入字典，價格轉為整數
    prices[name] = int(price)

# 讀取 M，代表查詢筆數
m = int(input())

# 迴圈讀取 M 筆查詢
for _ in range(m):
    # 讀取要查詢的水果名稱並移除前後多餘的空白/換行符
    fruit_to_lookup = input().strip()
    # 從字典中找出對應的價格並印出
    print(prices[fruit_to_lookup])
