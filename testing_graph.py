import matplotlib.pyplot as plt
import numpy as np
import time

def update_graph(red, green, blue):
    red_dec = (red/255)
    green_dec = (green/255)
    blue_dec = (blue/255)
    color_dec = (red_dec, green_dec, blue_dec)
    graph.fill(x, y, c=color_dec)

if __name__ == '__main__':
    plt.ion()
    fig, graph = plt.subplots()
    x = [0, 0, 1, 1]
    y = [0, 1, 1, 0]
    
    r = 0
    g = 100
    b = 200
    
    while True:
        update_graph(r, g, b)
        plt.pause(0.25)
        plt.draw()
        
        r = r + 10
        g = g + 20
        b = b + 30
        r = r%255
        g = g%255
        b = b%255










