from PIL import Image, ImageOps
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def adjust_image(input_path, output_path):
    input_image = Image.open(input_path)

    grayscale_image = ImageOps.grayscale(input_image)
    equalized_image = ImageOps.equalize(grayscale_image)
    equalized_image.save(output_path)

    return equalized_image

def display_histogram(input_image, output_image):
    input_array = np.array(input_image)
    input_gray = cv2.cvtColor(input_array, cv2.COLOR_RGB2GRAY)

    output_array = np.array(output_image)
    output_gray = cv2.cvtColor(output_array, cv2.COLOR_GRAY2RGB)

    plt.figure(dpi=150)
    plt.hist(input_gray.ravel(), bins=256, color='blue', label='input image')
    plt.hist(output_gray.ravel(), bins=256, color='orange', alpha=0.7, label='output image')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_folder = "." 
    input_file = "Q10.jpg"
    input_path = os.path.join(input_folder, input_file)

    output_file = "Q10_ans.jpg"
    output_path = os.path.join(input_folder, output_file)

    adjusted_image = adjust_image(input_path, output_path)
    display_histogram(Image.open(input_path), adjusted_image)
