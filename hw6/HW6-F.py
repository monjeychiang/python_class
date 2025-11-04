# 檔案名稱： HW6-F.py
# 建立日期： 2025/11/04
# 檔案說明： 使用遞迴計算 N 的階乘
# 編輯者： monjeychiang

def factorial(n):
  # 使用遞迴計算 n 的階乘
  # 基底情況：0! = 1
  if n == 0:
    return 1
  # 遞迴步驟：n! = n * (n-1)!
  else:
    return n * factorial(n - 1)

if __name__ == "__main__":
  # 讀取輸入
  number_input = int(input())
  
  # 呼叫函式並輸出結果
  if 0 <= number_input <= 12:
    result = factorial(number_input)
    print(result)
