from PIL import Image # pip install pillow
import tkinter as tk # sudo apt-get install python3-tk
from tkinter import filedialog
import sample_calculator

SAMPLE_WIDTH = 100
SAMPLE_HEIGHT = 20
SAMPLE_SIZE = 3

def crop_image(image: object, 
               width: int,
               height: int,
               x: int, 
               y: int):
    left = x
    top = y
    right = x + SAMPLE_WIDTH
    bottom = y + SAMPLE_HEIGHT
    print(f"Dimensions are: {left},{top},{right},{bottom}")
    return image.crop((left, top, right, bottom))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    width, height = image.size
    image_positions = sample_calculator.run(width, height, SAMPLE_WIDTH, SAMPLE_HEIGHT, SAMPLE_SIZE)
    print(image_positions)
    images = []
    for i in image_positions:
        cropped_image = crop_image(image, width, height, i[0], i[1])
        images.append(cropped_image)
        cropped_image.show()
