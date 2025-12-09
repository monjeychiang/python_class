# 檔案名稱：HW11-D.py
# 建立日期：2025/12/09
# 檔案說明：圖書館書籍編目（靜態驗證＋類別屬性計數）
# 編寫者：monjeychiang


class Book:
    # 類別屬性：圖書館總藏書量
    total_books = 0

    def __init__(self, name, isbn):
        # 實體屬性：書名與 ISBN
        self.name = name
        self.isbn = isbn
        # 每成功建立一本書，總藏書量加 1
        Book.total_books += 1

    @staticmethod
    def is_valid_isbn(isbn):
        """
        驗證 ISBN 是否為 10 位或 13 位的「純數字」字串。
        """
        return isbn.isdigit() and len(isbn) in (10, 13)


# 讀取指令數量 N
n = int(input())

# 依序處理 N 筆指令
for _ in range(n):
    parts = input().strip().split()

    # 指令格式：add [BookName] [ISBN]
    if parts[0] == "add":
        name = parts[1]
        isbn = parts[2]

        # 靜態方法先驗證 ISBN
        if Book.is_valid_isbn(isbn):
            # 合法才建立書籍物件並更新總藏書量
            book = Book(name, isbn)
            print(f"Added {book.name}, Total Books: {Book.total_books}")
        else:
            print("Invalid ISBN")

