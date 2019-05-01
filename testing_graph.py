from __future__ import print_function
import os
import sys
import argparse
import time
#import matplotlib.pyplot as matplot
import numpy as np
import easygui as gui
from PIL import Image, ImageDraw


im = Image.new('RGBA', (300, 300))
r = 0
g = 100
b = 200


def main():

    while True:
        print("\nRGB Raw: ")
        rgb = (r, g, b)
        print(rgb_raw)

        for x in range(300):
            for y in range(300):
                im.putpixel((x, y), (rgb[0], rgb[1], rgb[2]))
        im.save('testimage.png')
        #Image.open('testimage.png').show()

        color = 'testimage.png'
        msg = 'Color'
        choices = ["R", "G", "B"]
        reply = gui.buttonbox(msg, image=color, choices=choices)



        #color = np.array([rgb_raw[0], rgb_raw[1], rgb_raw[2]])
        #color = np.expand_dims(color, axis=0)

        #matplot.imshow(color)
        #matplot.show()

        # Delay for a second and repeat.
        time.sleep(1.0)

        r = r + 1
        g = g + 2
        b = b + 3
        r = r%256
        g = g%256
        b = b%256



if __name__ == '__main__':
    sys.exit(main())
