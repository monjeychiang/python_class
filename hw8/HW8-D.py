# 檔案名稱： HW8-D.py
# 建立日期： 2025/11/18
# 檔案說明： 統計班長選舉票數並按姓名排序輸出。
# 編輯者： monjeychiang

# 讀取選票總數 N
n = int(input())

# 建立一個空的字典來計票
votes = {}

# 迴圈讀取 N 張選票
for _ in range(n):
    # 讀取候選人姓名並移除前後多餘的空白/換行符
    name = input().strip()
    # 如果候選人已在字典中，票數加 1；否則新增候選人，票數設為 1
    votes[name] = votes.get(name, 0) + 1

# 取得所有候選人的姓名，並按照字母順序排序
sorted_candidates = sorted(votes.keys())

# 迴圈遍歷排序後的候選人名單
for candidate in sorted_candidates:
    # 印出每位候選人的姓名和得票數
    print(f"{candidate}: {votes[candidate]}")
