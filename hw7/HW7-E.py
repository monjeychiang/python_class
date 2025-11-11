# 檔案名稱： hw7-E.py
# 建立日期： 2025/11/11
# 檔案說明： 建立一個班級分數排行榜，並依分數由高至低排序。
# 編輯者： monjeychiang

# 讀取學生人數
n = int(input())

# 儲存學生分數的串列
leaderboard = []

# 讀取每位學生的姓名和分數
for _ in range(n):
    line = input().split()
    name = line[0]
    score = int(line[1])
    leaderboard.append((score, name))

# 將排行榜依分數由高至低排序
leaderboard.sort(reverse=True)

# 依序印出排行榜上的姓名
for score, name in leaderboard:
    print(name)
