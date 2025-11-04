# 檔案名稱： HW6-B.py
# 建立日期： 2025/11/04
# 檔案說明： 使用遞迴計算 1 到 n 的總和
# 編輯者： monjeychiang

def sum_to_n(n):
  # 使用遞迴計算從 1 到 n 的總和
  if n == 0:
    return 0
  else:
    return n + sum_to_n(n - 1)

if __name__ == "__main__":
  try:
    number_input = int(input())
    if 0 <= number_input <= 1000:
      result = sum_to_n(number_input)
      print(result)
    else:
      print("Input must be between 0 and 1000.")
  except ValueError:
    print("Invalid input. Please enter an integer.")
