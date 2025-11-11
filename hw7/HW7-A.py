# 檔案名稱： hw7-A.py
# 建立日期： 2025/11/11
# 檔案說明： 計算N天的總花費和平均花費。
# 編輯者： monjeychiang

# 取得天數
n = int(input())

expenses = []
for i in range(n):
    expense = int(input())
    expenses.append(expense)

# 計算總花費和平均花費
total_expense = sum(expenses)
average_expense = total_expense / n if n > 0 else 0

# 印出結果
print(f"Total: {total_expense}, Average: {average_expense:.2f}")
