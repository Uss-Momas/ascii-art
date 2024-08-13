#!/usr/bin/env python3
from PIL import Image

with Image.open("./ascii-pineapple.jpg") as img:
    img.load()

img = img.transpose(Image.ROTATE_90)
x, y = img.size
x, y = img.width, img.height
x, y = int(x / 2), int(y / 2)
img = img.resize((x, y), Image.Resampling.LANCZOS)
print("Successfully loaded image!")
print(f"Image size: {x} x {y}")


# CREATE A 2D MATRIX FOR IMAGE DATA
pixel_matrix = []

for i in range(x):
    pixel_row = []
    for j in range(y):
        pixel = img.getpixel([i, j])
        pixel_row.append(pixel)
    pixel_matrix.append(list(reversed(pixel_row)))

# print(pixel_matrix[0])
# print("===================================================================================================")
# print(list(reversed(pixel_matrix[0])))



# for x in range(len(pixel_matrix)):
    # for y in range(len(pixel_matrix[x])):
        # pixel = pixel_matrix[x][y]
        # print(pixel)
        # break
        # Now do something with the pixel... 

# PROCESS RGB tuple turn into single Brightness number
average_bright = []
for pixel_row in pixel_matrix:
    avg_bright_row = []
    for rgb in pixel_row:
        # compute the average number of rgb tuple
        average = int(sum(rgb) / 3) # METHOD 1
        # average = 0.21 * rgb[0] + 0.72 * rgb[1] + 0.07 * rgb[2] # Method 2
        avg_bright_row.append(average)
    average_bright.append(avg_bright_row)

print("Iterating through pixel brightnesses:")
for brightness in average_bright:
    print(brightness)
    break

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

max_bright = 255
max_char_pos = len(ascii_chars) - 1
bright = 255
char_position = int((bright * max_char_pos) / max_bright) # formula to map BRIGHTNESS TO ASCII CHARACTER
print(ascii_chars[char_position])

ascii_matrix = []
for avg_bright_row in average_bright:
    ascii_row = []
    for bright in avg_bright_row:
        char_position = int((bright * max_char_pos) / max_bright)
        ascii_row.append(ascii_chars[char_position])
    ascii_matrix.append(ascii_row)
print("Successfully constructed ASCII matrix!")
print(f"ASCII matrix size: {len(ascii_matrix)} x {len(ascii_matrix[0])}")
print("Iterating through pixel ASCII characters:")
for row in ascii_matrix:
    for ascii in row:
        print(ascii * 3, end="")
    print()
