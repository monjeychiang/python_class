# 檔案名稱： HW6-A.py
# 建立日期： 2025/11/04
# 檔案說明： 將攝氏溫度轉換為華氏溫度
# 編輯者： monjeychiang

def c_to_f(celsius):
  # 將攝氏溫度轉換為華氏溫度
  return celsius * 9/5 + 32

if __name__ == "__main__":
  celsius_input = float(input())
  fahrenheit_output = c_to_f(celsius_input)
  print(f"{fahrenheit_output:.2f}")
