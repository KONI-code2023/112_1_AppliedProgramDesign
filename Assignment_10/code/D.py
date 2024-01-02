# ======================
# file: Assignment_04.py
# author: KNE-code2023@github
# date: 2023-10-16
# ======================
import sys


def get_positive_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("請輸入大於 0 的正整數。")
        except ValueError:
            print("請輸入有效的數字。")


def fib(k: int) -> [list, str]:
    if k == 0:
        return [0]
    if k == 1:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, k + 1):
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > sys.maxsize:
            return "overflow"
        fibs.append(next_fib)
    return fibs


def main() -> None:
    k = get_positive_integer_input("請輸入正整數 k：")
    print(f"F({k}) = {fib(k)}")


if __name__ == "__main__":
    main()
