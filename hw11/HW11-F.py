# 檔案名稱：HW11-F.py
# 建立日期：2025/12/09
# 檔案說明：航空訂位系統（類別屬性＋靜態方法＋實體方法）
# 編寫者：monjeychiang


class AirlineBooking:
    # 類別屬性：航班總座位數與剩餘座位數
    total_seats = 0
    remaining_seats = 0

    def __init__(self):
        # 本作業中實體本身不需要額外狀態
        pass

    @classmethod
    def config_capacity(cls, num):
        # 類別方法：設定／更新航班總座位數，並重置剩餘座位
        cls.total_seats = num
        cls.remaining_seats = num

    @staticmethod
    def is_valid_passport(passport):
        # 靜態方法：檢查護照是否為 9 碼英數字
        return len(passport) == 9 and passport.isalnum()

    def book(self, passport):
        # 實體方法：處理個人訂位流程
        if not AirlineBooking.is_valid_passport(passport):
            return "Invalid Passport"

        if AirlineBooking.remaining_seats <= 0:
            return "Flight Full"

        # 有座位且護照合法，完成訂位並扣除剩餘座位
        AirlineBooking.remaining_seats -= 1
        return "Booking Confirmed"


# 讀取初始座位數並設定航班容量
initial_seats = int(input())
AirlineBooking.config_capacity(initial_seats)

# 建立訂位系統實體
system = AirlineBooking()

# 讀取指令數 N
n = int(input())

# 依序處理 N 筆指令
for _ in range(n):
    parts = input().strip().split()

    # config [num]：更換機型座位數
    if parts[0] == "config":
        num = int(parts[1])
        AirlineBooking.config_capacity(num)
        print("Capacity Updated")

    # book [passport]：訂位
    elif parts[0] == "book":
        passport = parts[1]
        result = system.book(passport)
        print(result)

