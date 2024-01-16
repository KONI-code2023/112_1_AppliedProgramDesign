# ======================
# file: Assignment_05_3.py
# author: KONI-code2023@github
# date: 2023-10-23
# ======================
import matplotlib.pyplot as plt
from collections import Counter
import os


def read_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # 全部轉成小寫
            text = file.read().lower()
        return text
    except FileNotFoundError:
        print(f"檔案 '{file_path}' 不存在。")
        return ""
    except Exception as e:
        print(f"讀取檔案時發生錯誤：{e}")
        return ""


def filter_text(text: str) -> str:
    # 只留a~z
    return "".join(filter(str.isalpha, text))


def count_characters(text: str) -> Counter:
    return Counter(text)


def plot_bar_chart(character_counts: Counter) -> None:
    sorted_counts = dict(sorted(character_counts.items()))
    plt.bar(sorted_counts.keys(), sorted_counts.values())
    plt.show()


def main() -> None:
    file_path = "..\\data\\snow-white.txt"

    text = read_file(file_path)
    if text:
        filtered_text = filter_text(text)
        character_counts = count_characters(filtered_text)
        print(character_counts)
        plot_bar_chart(character_counts)


if __name__ == "__main__":
    main()
