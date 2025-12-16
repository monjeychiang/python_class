# 檔案名稱：HW12-G.py
# 建立日期：2025/12/16
# 檔案說明：銀行轉帳與防詐騙（Static Method 驗證、Class Method 全行凍結、Instance Method 轉帳）
# 編寫者：monjeychiang


class Account:
    # 類別屬性：全行凍結狀態
    is_frozen = False

    def __init__(self, acc_id, balance):
        self.acc_id = acc_id
        self.balance = balance

    @staticmethod
    def validate_account_id(acc_id):
        """帳號格式：A 開頭 + 5 碼數字"""
        return acc_id.startswith("A") and len(acc_id) == 6 and acc_id[1:].isdigit()

    @classmethod
    def freeze(cls):
        cls.is_frozen = True

    @classmethod
    def unfreeze(cls):
        cls.is_frozen = False

    def transfer_to(self, target, amount):
        # 1) 全行凍結
        if Account.is_frozen:
            print("Frozen")
            return

        # 2) 帳號格式
        # 呼叫 Static Method 進行驗證
        if not (Account.validate_account_id(self.acc_id) and Account.validate_account_id(target.acc_id)):
            print("Invalid Account")
            return

        # 3) 餘額是否足夠
        if self.balance < amount:
            print("Insufficient Funds")
            return

        # 4) 執行轉帳
        self.balance -= amount
        target.balance += amount
        print("Success")


def main():
    try:
        # 處理可能沒有輸入的情況
        line = input().strip()
        if not line:
            return
        cmd_count = int(line)
    except (EOFError, ValueError):
        return

    accounts = {}

    for _ in range(cmd_count):
        try:
            line = input().strip()
            # 若遇到空行則跳過，防止 split 後 parts 為空導致 IndexError
            if not line:
                continue
                
            parts = line.split()
            cmd = parts[0]

            if cmd == "create":
                # 確保參數足夠：create <id> <balance>
                if len(parts) >= 3:
                    acc_id = parts[1]
                    balance = float(parts[2])
                    accounts[acc_id] = Account(acc_id, balance)

            elif cmd == "transfer":
                # 確保參數足夠：transfer <from> <to> <amount>
                if len(parts) >= 4:
                    from_id, to_id, amount = parts[1], parts[2], float(parts[3])
                    sender = accounts.get(from_id)
                    receiver = accounts.get(to_id)

                    # 帳戶不存在視為帳號無效
                    if sender is None or receiver is None:
                        print("Invalid Account")
                        continue

                    sender.transfer_to(receiver, amount)

            elif cmd == "freeze":
                Account.freeze()
                
            elif cmd == "unfreeze":
                Account.unfreeze()
        
        except (EOFError, IndexError, ValueError):
            # 遇到意外的輸入錯誤或檔案結束，跳出迴圈或忽略該行
            break

if __name__ == "__main__":
    main()