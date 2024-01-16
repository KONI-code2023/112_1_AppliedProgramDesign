# ======================
# file: Assignment_02.py
# author: KONI-code2023@github
# date: 2023-10-02
# ======================
import numpy as np


def get_positive_number() -> None:
    while True:
        try:
            num = float(input("請輸入正整數或正浮點數: "))
            if num < 0:
                return None
            elif num.is_integer() and num > 0:
                return int(num)
            elif num > 0:
                return num
            else:
                print("請輸入正整數或正浮點數")
        except ValueError:
            print("請輸入有效數字")


def main() -> None:
    n = []

    while True:
        num = get_positive_number()
        if num is None:
            break
        n.append(num)

    if not n:
        print("未輸入任何數字")
        return

    print(f"平均值 = {round(np.mean(n), 2)}，中位數 = {round(np.median(n), 2)}，"
          f"變異數 = {round(np.var(n), 2)}，標準差 = {round(np.std(n), 2)}")


if __name__ == "__main__":
    main()
