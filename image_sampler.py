from PIL import Image
import tkinter as tk
from tkinter import filedialog
import sample_calculator

SAMPLE_SIZE = 3


def parse_input(type):
    while True:
        number = input("Please specify the " +
                       type +
                       " in pixels of each sample: ")
        try:
            val = int(number)
            if val <= 0:
                print("Error: input must be a positive integer.")
                continue
            break
        except ValueError:
            print("Error: input must be a positive integer.")
    return val


def crop_image(image: object,
               sample_width: int,
               sample_height: int,
               x: int,
               y: int):

    # Generates a cropped image.

    left = x
    top = y
    right = x + sample_width
    bottom = y + sample_height
    print(f"Dimensions are: {left},{top},{right},{bottom}")
    return image.crop((left, top, right, bottom))

if __name__ == "__main__":
    sample_width = parse_input("width")
    sample_height = parse_input("height")
    input("A menu will now appear, "
          "from which an image should be selected.\nPress Enter when ready.")
    root = tk.Tk()
    root.withdraw()

    # The image is selected using a file picker menu.
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    width, height = image.size

    # At this point, the sample calculator calculates
    # the set of coordinates for generating each sample.
    image_positions = sample_calculator.run(
        width, height, sample_width, sample_height, SAMPLE_SIZE)
    print(image_positions)
    images = []
    for i in image_positions:
        cropped_image = crop_image(
            image, sample_width, sample_height, i[0], i[1])
        images.append(cropped_image)

        # Each cropped image is displayed
        # using the system's default image viewer.
        cropped_image.show()
