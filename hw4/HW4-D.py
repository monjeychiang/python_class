# 檔案名稱： HW4-D.py
# 建立日期： 2025/10/14
# 檔案說明： 找出並印出在給定區間 [A, B] 內的所有質數。
# 編輯者： monjeychiang

def is_prime(num):
    """
    檢查一個數字是否為質數。
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        A_str, B_str = input().split()
        A = int(A_str)
        B = int(B_str)

        if A <= 0 or B <= 0:
            print()
        else:
            prime_numbers = []
            for num in range(A, B + 1):
                if is_prime(num):
                    prime_numbers.append(num)
            
            if prime_numbers:
                print(*(prime_numbers))
            else:
                print() # 輸出一個空行
    except ValueError:
        print()
    except IndexError:
        print()
