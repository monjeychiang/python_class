# 檔案名稱： HW8-G.py
# 建立日期： 2025/11/18
# 檔案說明： 統計文章中單字的出現次數。
# 編輯者： monjeychiang

# 讀取行數 N
n = int(input())

# 將所有句子合併成一個長字串
full_text = ""
for _ in range(n):
    full_text += input() + " "

# 1. 將所有字母轉為小寫
full_text = full_text.lower()

# 2. 忽略所有指定的標點符號
punctuation_to_remove = ['.', ',', '!', '?']
for punc in punctuation_to_remove:
    full_text = full_text.replace(punc, '')

# 3. 以空格切割單字
words = full_text.split()

# 4. 使用字典統計每個單字出現的次數
word_counts = {}
for word in words:
    if word: # 確保不是空字串
        word_counts[word] = word_counts.get(word, 0) + 1

# 取得所有單字並按字母順序排序
sorted_words = sorted(word_counts.keys())

# 按照排序後的順序印出結果
for word in sorted_words:
    print(f"{word}: {word_counts[word]}")
