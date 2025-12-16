# 檔案名稱：HW12-F.py
# 建立日期：2025/12/16
# 檔案說明：圖書館借閱系統（Tuple 日期、Set 借閱中書籍、Dict 會員資料）
# 編寫者：monjeychiang


class Member:
    def __init__(self, name):
        self.name = name
        self.history = []  # List of (ISBN, Date)

    def add_history(self, isbn, date):
        self.history.append((isbn, date))


class Library:
    def __init__(self):
        self.borrowed_books = set()
        self.members = {}

    def get_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)
        return self.members[name]

    def borrow(self, user, isbn, date):
        if isbn in self.borrowed_books:
            print("Unavailable")
            return
        member = self.get_member(user)
        self.borrowed_books.add(isbn)
        member.add_history(isbn, date)
        print("Borrowed")

    def return_book(self, isbn):
        self.borrowed_books.discard(isbn)

    def print_history(self, user):
        member = self.get_member(user)
        for isbn, date in member.history:
            print(f"{date}: {isbn}")


def main():
    library = Library()
    command_count = int(input())

    for _ in range(command_count):
        parts = input().split()
        cmd = parts[0]

        if cmd == "borrow":
            user, isbn, date = parts[1], parts[2], parts[3]
            library.borrow(user, isbn, date)
        elif cmd == "return":
            isbn = parts[1]
            library.return_book(isbn)
        elif cmd == "history":
            user = parts[1]
            library.print_history(user)


if __name__ == "__main__":
    main()
