#!/usr/bin/env python3
import colorama
from colorama import Fore
from os import path
from PIL import Image
from sys import argv
from typing import List, Tuple

colorama.init()

if len(argv) != 2:
    print("Usage: ./art-ascii.py image-source.jpeg")
    exit(1)
img_path = argv[1]

if not path.exists(img_path):
    print(f"Path {img_path}: Doesn't exists!")
    exit(1)

if not path.isfile(img_path):
    print(f"Path {img_path}: Is Not a File!")
    exit(1)


def is_image(img_path: str) -> bool:
    try:
        with Image.open(img_path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError):
        return False

if not is_image(img_path):
    print(f"Path {img_path}: Is not an Image!")
    exit(1)


with Image.open(img_path) as img:
    img.load()

MAX_INTENSITY = 255
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_ASCII_CHAR_POSITION = len(ASCII_CHARS) - 1


def invert_brightness_number(rgb):
    """Function to invert an RGB matrix brightness
    Witch means:
        - dark becomes light (255 -> 0) and light becomes dark (0 -> 255)
        formula:
            - value = m - n
            where:
                - m: 255
                - n: 0, 1, 2...
    Returns:
        - mapped value on the scale to 0-255
    """
    NEW_MIN = 255
    r, g, b = NEW_MIN - rgb[0], NEW_MIN - rgb[1], NEW_MIN - rgb[2]
    return r, g, b

          
def get_pixel_matrix(img, width: int, height: int, invert: bool = False) -> List[List[Tuple[int, int, int]]]:
    """Returns a 2D pixel Matrix"""
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = img.getpixel((x, y))
            if not invert:
                row.append(pixel)
            else:
                row.append(invert_brightness_number(pixel))
        matrix.append(row)
    return matrix


def intensity_algorithm(algorithm: str, rgb: Tuple[int, int , int]) -> int:
    """Calculates the proper intensity algorithm
    Possible values:
        - "brightness"
        - "min/max"
        - "luminosity"
    """
    if algorithm == 'average':
        return int(sum(rgb) / 3)
    if algorithm == 'min/max':
        return int((max(rgb) + min(rgb)) / 2)
    # otherwise is luminosity
    R = rgb[0]
    G = rgb[1]
    B = rgb[2]
    return int((0.21 * R) + (0.72 * G) + (0.07 * B))

def get_intensity_matrix(pixel_matrix: List[List[Tuple[int, int, int]]], intensity_algo: str ="average") -> List[List[int]]:
    """RETURNS a 2D Intensity matrix
    Represents a brightness or Luminosity of a RGB tuple
    """
    intensity: List[List] = []
    for pixel_row in pixel_matrix:
        row = []
        for rgb in pixel_row:
        # using the average brightness method
            average = intensity_algorithm(intensity_algo, rgb)
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
pixel_matrix = get_pixel_matrix(img, width, height, invert=False)

# PROCESS RGB tuple turn into single Brightness number
average_bright = get_intensity_matrix(pixel_matrix, intensity_algo="average")

# PRODUCE THE ASCII MATRIX REPRESENTING THE IMAGE
ascii_matrix = get_ascii_matrix(average_bright)

# PRINTS THE ART
print_ascii(ascii_matrix, 2)

