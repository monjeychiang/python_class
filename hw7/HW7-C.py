# 檔案名稱： hw7-C.py
# 建立日期： 2025/11/11
# 檔案說明： 根據指定的合格網域篩選電子郵件。
# 編輯者： monjeychiang

# 讀取合格網域
allowed_domain = input().strip()

# 讀取待檢查的電子郵件數量
n = int(input())

# 收集合格的電子郵件
valid_emails = []
for _ in range(n):
    email = input().strip()
    if email.endswith(allowed_domain):
        valid_emails.append(email)

# 印出合格的電子郵件串列
print(valid_emails)
