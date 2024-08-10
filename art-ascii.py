#!/usr/bin/env python3
from PIL import Image

im = Image.open("./ascii-pineapple.jpg")
print(im.format, im.size, im.mode)
