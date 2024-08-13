#!/usr/bin/env python3
from PIL import Image
from typing import List, Tuple

with Image.open("./ascii-pineapple.jpg") as img:
    img.load()

MAX_INTENSITY = 255
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_ASCII_CHAR_POSITION = len(ASCII_CHARS) - 1

def get_pixel_matrix(img, width: int, height: int) -> List[List[Tuple[int]]]:
    """Returns a 2D pixel Matrix"""
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = img.getpixel((x, y))
            row.append(pixel)
        matrix.append(list(reversed(row)))
    return matrix


def get_intensity_matrix(pixel_matrix: List[List[Tuple[int]]]) -> List[List[int]]:
    """RETURNS a 2D Intensity matrix
    Represents a brightness or Luminosity of a RGB tuple
    """
    intensity: List[List] = []
    for pixel_row in pixel_matrix:
        row = []
        for rgb in pixel_row:
        # using the average brightness method
            average = int(sum(rgb) / 3)
            row.append(average)
        intensity.append(row)
    return intensity


def get_ascii_letter(intensity: int) -> str:
    """Returns a letter representing a intensity"""
    char_position = int ((intensity * MAX_ASCII_CHAR_POSITION) / MAX_INTENSITY)
    return ASCII_CHARS[char_position]



def get_ascii_matrix(intensity_matrix: List[List[int]]) -> List[List[str]]:
    """Returns a 2D Matrix with ascii characters representing
    the image
    """
    ascii_matrix = []
    # MAP THE INTENSITY TO A ASCII CHARACTER
    for intensity_row in intensity_matrix:
        ascii_row = []
        for intensity in intensity_row:
            char = get_ascii_letter(intensity)
            ascii_row.append(char)
        ascii_matrix.append(ascii_row)
    return ascii_matrix


def print_ascii(ascii_matrix: List[List[str]], number_repeats: int = 1) -> None:
    """PRINT THE ASCII ART"""
    for row in ascii_matrix:
        for letter in row:
            print(letter * number_repeats, end="")
        print()


width, height = int(img.width / 2), int(img.height / 2)
img = img.resize((width, height), Image.Resampling.LANCZOS)
print("Successfully loaded image!")
print(f"Image size: {width} x {height}")

# CREATE A 2D MATRIX FOR IMAGE DATA
pixel_matrix = get_pixel_matrix(img, width, height)

# PROCESS RGB tuple turn into single Brightness number
average_bright = get_intensity_matrix(pixel_matrix)

# PRODUCE THE ASCII MATRIX REPRESENTING THE IMAGE
ascii_matrix = get_ascii_matrix(average_bright)

# PRINTS THE ART
print_ascii(ascii_matrix, 2)

