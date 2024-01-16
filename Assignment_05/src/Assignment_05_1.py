# ======================
# file: Assignment_05_1.py
# author: KONI-code2023@github
# date: 2023-10-23
# ======================
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


def main() -> None:
    while True:
        a = get_positive_integer_input("請輸入正整數 a：")
        b = get_positive_integer_input("請輸入正整數 b (需大於等於 a)：")

        if a <= b:
            break
        else:
            print("請確保 a <= b")

    output = [i for i in range(a, b + 1) if i % 4 == 0 or i % 9 == 0]

    print(f"{output}，共有{len(output)}個，總和為{sum(output)}")


if __name__ == "__main__":
    main()
