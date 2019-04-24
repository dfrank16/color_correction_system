import time
import board
import busio
import adafruit_tcs34725
import matplotlib.pyplot as matplot
import numpy as np


# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

# Main loop reading color and printing it every second.
while True:
    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    print('Temperature: {0}K Lux: {1}'.format(temp, lux))

    rgb = sensor.color_rgb_bytes
    print('R: ' + rgb[0])
    print('G: ' + rgb[1])
    print('B: ' + rgb[2])

    color = np.array([rgb[0], rgb[1], rgb[2]], dtype=np.uint8)

    matplot.imshow(color[0])
    matplot.show()

    # Delay for a second and repeat.
    time.sleep(1.0)

