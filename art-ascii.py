#!/usr/bin/env python3
from PIL import Image

with Image.open("./ascii-pineapple.jpg") as img:
    img.load()

x, y = img.size
print("Successfully loaded image!")
print(f"Image size: {x} x {y}")


# CREATE A 2D MATRIX FOR IMAGE DATA
pixel_matrix = []

for i in range(x):
    pixel_row = []
    for j in range(y):
        pixel = img.getpixel([i, j])
        pixel_row.append(pixel)
    pixel_matrix.append(pixel_row)

# for x in range(len(pixel_matrix)):
    # for y in range(len(pixel_matrix[x])):
        # pixel = pixel_matrix[x][y]
        # print(pixel)
        # break
        # Now do something with the pixel... 

# PROCESS RGB tuple turn into single Brightness number
average_bright = []
for pixel_row in pixel_matrix:
    for rgb in pixel_row:
        # compute the average number of rgb tuple
        average = int(sum(rgb) / 3)
        average_bright.append(average)

print("Iterating through pixel brightnesses:")
for brightness in average_bright:
    print(brightness)
    break

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

