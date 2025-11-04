# 檔案名稱： HW6-C.py
# 建立日期： 2025/11/04
# 檔案說明： 計算字串中母音的總數
# 編輯者： monjeychiang

def count_vowels(s):
  # 計算字串中母音的總數（不分大小寫）
  vowels = "aeiou"
  count = 0
  for char in s.lower():
    if char in vowels:
      count += 1
  return count

if __name__ == "__main__":
  input_string = input()
  vowel_count = count_vowels(input_string)
  print(vowel_count)
