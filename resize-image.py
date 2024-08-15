#!/usr/bin/env python3
from PIL import Image
from sys import argv

def resize_by_percentage(image, outfile, percentage):
    with Image.open(image) as im:
        width, height = im.size
        resized_dimensions = (int(width * percentage), int(height * percentage))
        resized = im.resize(resized_dimensions)
        resized.save(outfile, 'jpeg')

if len(argv) != 2:
    print("Usage: ./resize-image.py image-path")
    exit(1)

image_path = argv[1]

resize_by_percentage(image_path, 'deadpool-percentage.png', 0.5)
