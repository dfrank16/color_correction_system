from __future__ import print_function
import os
import sys
import argparse
import time
import board
import busio
import adafruit_tcs34725
import matplotlib.pyplot as matplot
import numpy as np
import easygui as gui
from PIL import Image, ImageDraw


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
im = Image.new('RGBA', (300, 300))


def main():


    # Initialize I2C bus and sensor.


    
    #im.getpixel((0, 0))




    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    print('Temperature: {0}K Lux: {1}'.format(temp, lux))

    rgb = sensor.color_rgb_bytes
    print('R: ' + str(rgb[0]))
    print('G: ' + str(rgb[1]))
    print('B: ' + str(rgb[2]))
    print(rgb)

    print("\nRGB Raw: ")
    rgb_raw = sensor.color_raw
    print(rgb_raw)

    print("\nColor: ")
    color_value = sensor.color
    print(color_value)



    for x in range(300):
        for y in range(300):
            im.putpixel((x, y), (rgb_raw[0], rgb_raw[1], rgb_raw[2]))
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



if __name__ == '__main__':
    sys.exit(main())
