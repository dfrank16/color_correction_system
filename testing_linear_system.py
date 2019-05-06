import matplotlib.pyplot as plt
import numpy as np
import time
import sys

def update_graph(red, green, blue):
    red_dec = (red/255)
    green_dec = (green/255)
    blue_dec = (blue/255)
    color_desiredec = (red_dec, green_dec, blue_dec)
    graph.fill(x, y, c=color_desiredec)

if __name__ == '__main__':
    print("\nDesired RGB Value: (", sys.argv[1], sys.argv[2], sys.argv[3], ")\n")
    
    plt.ion()
    fig, graph = plt.subplots()
    x = [0, 0, 1, 1]
    y = [0, 1, 1, 0]
    color_match = False
    num_cycles = 0
    
    r_sensor = 128
    g_sensor = 128
    b_sensor = 128
    
    r_desired = int(sys.argv[1])
    g_desired = int(sys.argv[2])
    b_desired = int(sys.argv[3])
    
    r_new = 0
    g_new = 0
    b_new = 0
    
    try: 
        while not color_match:
            num_cycles = num_cycles + 1
            update_graph(r_sensor, g_sensor, b_sensor)
            plt.pause(0.01)
            plt.draw()
            
            # Red
            if r_sensor < r_desired:
                r_new = r_sensor+1
            elif r_sensor > r_desired:
                r_new = r_sensor-1
            else:
                r_new = r_desired
            
            # Green
            if g_sensor < g_desired:
                g_new = g_sensor+1
            elif g_sensor > g_desired:
                g_new = g_sensor-1
            else:
                g_new = g_desired
            
            # Blue
            if b_sensor < b_desired:
                b_new = b_sensor+1
            elif b_sensor > b_desired:
                b_new = b_sensor-1
            else:
                b_new = b_desired
            
            if r_sensor == r_desired and g_sensor == g_desired and b_sensor == b_desired:
                color_match = True

            print("R: ", r_sensor, "G: ", g_sensor, "B: ", b_sensor)

            r_sensor = r_new
            g_sensor = g_new
            b_sensor = b_new
            
    except KeyboardInterrupt:
        sys.exit()

    print("\nComplete!\n")
    print("Cycles: ", num_cycles)
    plt.pause(3)
    







