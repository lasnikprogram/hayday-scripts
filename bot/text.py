#!/usr/bin/python3
import pytesseract
from PIL import Image, ImageDraw

startx = 251
starty = 138
sizex = 228
sizey = 33
jumpx = 489 - startx
jumpy = 350 - starty
jumpsidex = 764 - (startx + jumpx)
lastside = False
debug = False

def from_paper(image, lastside=lastside, debug=debug):
    if debug:
        draw = ImageDraw.Draw(image)
    
    for y in range(3):
        for x in range(2 if lastside else 4):
            if x >= 2:
                x_coord = startx + jumpx * (x - 1) + jumpsidex
            else:
                x_coord = startx + jumpx * x
            y_coord = starty + jumpy * y
            shape = [x_coord, y_coord, x_coord + sizex, y_coord + sizey]
            crop = img.crop(shape)
            return pytesseract.image_to_string(crop, config='-c tessedit_char_whitelist='\
                '\'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \' --psm 10').split('\n')

            if debug:
                draw.rectangle(shape, outline ="red")
    if debug:
        img.show()
