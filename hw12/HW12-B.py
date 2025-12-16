# 檔案名稱：HW12-B.py
# 建立日期：2025/12/16
# 檔案說明：班級通訊錄檢查（@staticmethod、Dict 操作）
# 編寫者：monjeychiang


class ContactValidator:
    @staticmethod
    def validate_phone(phone):
        # 手機號碼需為 10 碼數字
        return len(phone) == 10 and phone.isdigit()


def main():
    count = int(input())
    contacts = {}

    for _ in range(count):
        student_id, name, phone = input().split()
        if ContactValidator.validate_phone(phone):
            contacts[student_id] = name
            print(f"{name} added")
        else:
            print("Invalid Phone")

    for student_id in sorted(contacts):
        print(f"{student_id}: {contacts[student_id]}")


if __name__ == "__main__":
    main()
