import matplotlib.pyplot as plt
from collections import Counter
import os

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # 全部轉成小寫
        return text
    except FileNotFoundError:
        print(f"檔案 '{file_path}' 不存在。")
        return None
    except Exception as e:
        print(f"讀取檔案時發生錯誤：{e}")
        return None

def filter_text(text):
    return "".join(filter(str.isalpha, text))  # 只留a~z

def count_characters(text):
    return Counter(text)

def plot_bar_chart(character_counts):
    sorted_counts = dict(sorted(character_counts.items()))
    plt.bar(sorted_counts.keys(), sorted_counts.values())
    plt.show()

def main():
    file_path = '..\\data\\snow-white.txt'
    
    text = read_file(file_path)
    if text is not None:
        filtered_text = filter_text(text)
        character_counts = count_characters(filtered_text)
        print(character_counts)
        plot_bar_chart(character_counts)

if __name__ == "__main__":
    main()
