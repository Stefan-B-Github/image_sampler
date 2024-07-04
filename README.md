# Image Sampler
A small Python tool that generates random, non-overlapping samples from an image file.

## Requirements:

- **Pillow** (`pip install pillow`)
- **tkinter** (`apt-get install python3-tk` or similar).

## Usage:

```
python image_sampler.py
```
The user will be prompted to enter the width and height of each sample generated. Thereafter, a menu will appear in which to select the image to be sampled.
The tool will generate three samples of the required size, so long as it is possible to do so without any samples overlapping.
These samples will be saved to temporary storage, and opened in the system's default image viewer.

## Example:

**User input:**

![image](https://i.imgur.com/fqWb2dc.png)

**Image selected:**

![image](https://i.imgur.com/M3Epf7r.png)

**Output:**

![image](https://i.imgur.com/n8JomaZ.png)

![image](https://i.imgur.com/5eTJEWX.png)

![image](https://i.imgur.com/kTAQog4.png)

Three non-overlapping samples of 300x200 pixels have been generated.

## Extending functionality

The main method of `image_sampler.py` produces an array named `images` containing the image samples stored in-memory. This array can be used for further transformations.
