# 檔案名稱： HW6-G.py
# 建立日期： 2025/11/04
# 檔案說明： 使用遞迴計算費伯那希數列第 n 項
# 編輯者： monjeychiang

def fib(n):
  # 使用遞迴計算費伯那希數列第 n 項
  # 基底情況：F0 = 0, F1 = 1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  # 遞迴步驟：Fn = Fn-1 + Fn-2
  else:
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
  # 讀取輸入
  number_input = int(input())
  
  # 呼叫函式並輸出結果
  if 0 <= number_input <= 30:
    result = fib(number_input)
    print(result)
