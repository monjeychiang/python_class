# 檔案名稱： HW1-D.py
# 建立日期： 2025/09/23
# 檔案說明： 讀取2個整數(a, b), 先算出兩數總和(sum)，最後輸出 a+b=sum。
# 編輯者： monjeychiang

# 讀取使用者輸入的兩個整數
a1_str, b1_str = input().split()

# 將字串轉換為整數
a1 = int(a1_str)
b1 = int(b1_str)

# 計算總和
sum1 = a1 + b1

# 格式化輸出結果
print(f"{a1}+{b1}={sum1}")
