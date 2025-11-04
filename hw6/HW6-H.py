# 檔案名稱： HW6-H.py
# 建立日期： 2025/11/04
# 檔案說明： 使用遞迴計算兩個非負整數的最大公因數 (GCD)
# 編輯者： monjeychiang

def gcd(a, b):
  # 使用輾轉相除法的遞迴實作
  # 基底情況：當 b 為 0 時，a 即為最大公因數
  if b == 0:
    return a
  # 遞迴步驟：gcd(a, b) = gcd(b, a % b)
  else:
    return gcd(b, a % b)

if __name__ == "__main__":
  # 讀取並處理輸入
  a, b = map(int, input().split())
  
  # 呼叫函式並輸出結果
  result = gcd(a, b)
  print(result)
