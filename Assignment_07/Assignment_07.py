# ======================
# file: Assignment_07.py
# author: KNE-code2023@github
# date: 2023-12-04
# ======================
from PIL import Image, ImageOps
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def adjust(input_path: str, output_path: str) -> Image:
    input_img = Image.open(input_path)

    gray_img = ImageOps.grayscale(input_img)
    equalized_img = ImageOps.equalize(gray_img)
    equalized_img.save(output_path)

    return equalized_img


def show_histogram(input_img: Image, output_img: Image) -> None:
    input_arr = np.array(input_img)
    input_gray = cv2.cvtColor(input_arr, cv2.COLOR_RGB2GRAY)

    output_arr = np.array(output_img)
    output_gray = cv2.cvtColor(output_arr, cv2.COLOR_GRAY2RGB)

    plt.figure(figsize=(15, 6))
    plt.hist(input_gray.ravel(), bins=256, color="blue", label="input img")
    plt.hist(output_gray.ravel(), bins=256, color="orange", alpha=0.7, label="output img")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    input_folder = "."
    input_file = ".\\image\\Q10.jpg"
    input_path = os.path.join(input_folder, input_file)

    output_file = ".\\image\\Q10_ans.jpg"
    output_path = os.path.join(input_folder, output_file)

    adjusted_img = adjust(input_path, output_path)
    show_histogram(Image.open(input_path), adjusted_img)
