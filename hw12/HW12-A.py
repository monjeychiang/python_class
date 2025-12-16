# 檔案名稱：HW12-A.py
# 建立日期：2025/12/16
# 檔案說明：飲料店訂單系統（類別定義、實體屬性、List 操作、__str__）
# 編寫者：monjeychiang


class Drink:
    def __init__(self, name, price, sweetness):
        self.name = name
        self.price = price
        self.sweetness = sweetness

    def __str__(self):
        return f"{self.name} ({self.sweetness}) - ${self.price}"


def main():
    order_count = int(input())
    orders = []

    for _ in range(order_count):
        name, price, sweetness = input().split()
        orders.append(Drink(name, int(price), sweetness))

    total = 0
    for drink in orders:
        print(drink)
        total += drink.price

    print(f"Total: ${total}")


if __name__ == "__main__":
    main()
