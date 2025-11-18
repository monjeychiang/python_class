# 檔案名稱： HW8-E.py
# 建立日期： 2025/11/18
# 檔案說明： 使用集合差集找出缺席的座位號碼。
# 編輯者： monjeychiang

# 建立一個包含所有應到座位號碼 (1到10) 的集合
all_seats = set(range(1, 11))

# 讀取已到賓客的數量 N
try:
    n = int(input())
except (ValueError, EOFError):
    n = 0

# 建立一個空的集合來儲存已到的賓客座位號碼
arrived_seats = set()

# 迴圈讀取 N 個已到的座位號碼
for _ in range(n):
    try:
        seat = int(input())
        arrived_seats.add(seat)
    except (ValueError, EOFError):
        break

# 使用集合的差集運算找出缺席的座位
absent_seats_set = all_seats - arrived_seats

# 將結果轉換為列表並由小到大排序
absent_seats_list = sorted(list(absent_seats_set))

# 輸出缺席的座位號碼列表
print(absent_seats_list)
