# 檔案名稱： HW6-D.py
# 建立日期： 2025/11/04
# 檔案說明： 判斷一個字串是否為迴文
# 編輯者： monjeychiang

def is_palindrome(s):
  # 判斷字串是否為迴文
  # s[::-1] 透過字串切片將字串反轉
  # s == s[::-1] 這個比較運算式會直接返回一個布林值 (True 或 False)
  return s == s[::-1]

if __name__ == "__main__":
  input_string = input()
  if is_palindrome(input_string):
    print("Yes")
  else:
    print("No")
