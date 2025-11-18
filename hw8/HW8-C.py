# 檔案名稱： HW8-C.py
# 建立日期： 2025/11/18
# 檔案說明： 建立一個不重複且維持原始順序的播放清單。
# 編輯者： monjeychiang

# 讀取歌曲總數 N
n = int(input())

# 建立一個空列表來儲存不重複且有序的播放清單
unique_playlist = []
# 建立一個空集合來快速檢查歌曲是否已存在
seen_songs = set()

# 迴圈讀取 N 首歌曲
for _ in range(n):
    # 讀取歌名並移除前後多餘的空白/換行符
    song = input().strip()
    # 檢查這首歌是否已經在 seen_songs 集合中
    if song not in seen_songs:
        # 如果是新歌，將它加入不重複播放清單
        unique_playlist.append(song)
        # 同時也將它加入 seen_songs 集合，標記為已處理
        seen_songs.add(song)

# 輸出最終的播放清單
print(unique_playlist)
