# 檔案名稱： HW6-E.py
# 建立日期： 2025/11/04
# 檔案說明： 篩選出串列中大於指定閾值的數字
# 編輯者： monjeychiang

def filter_by_threshold(numbers, limit):
  # 返回一個新的串列，其中只包含大於 limit 的數字
  return [num for num in numbers if num > limit]

if __name__ == "__main__":
  # 讀取並處理第一行輸入：由空格分隔的整數
  numbers_list = list(map(int, input().split()))
  
  # 讀取第二行輸入：limit
  limit_value = int(input())
  
  # 呼叫函式並取得篩選後的結果
  filtered_list = filter_by_threshold(numbers_list, limit_value)
  
  # 輸出結果
  print(filtered_list)
