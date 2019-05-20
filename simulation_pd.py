from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import os
import argparse

def update_graph(red, green, blue):
    red_dec = (red/255)
    green_dec = (green/255)
    blue_dec = (blue/255)
    
    if red_dec > 1:
        red_dec = 1
    if green_dec > 1:
        green_dec = 1
    if blue_dec > 1:
        blue_dec = 1
        
    color_desired = (red_dec, green_dec, blue_dec)
    graph.fill(x, y, c=color_desired)

if __name__ == '__main__':
    plt.ion()
    fig3, graph3 = plt.subplots()
    fig2, graph2 = plt.subplots()
    fig, graph = plt.subplots()
    x = [0, 0, 1, 1]
    y = [0, 1, 1, 0]
    x_scatter = []
    y_scatter = []
    colors = []
    graph2.grid()
    
    cond = True
    failure = False
    num_iterations = 0
    stop = 30
    
    r_s = 27
    g_s = 150
    b_s = 160
    print("\nInitial RGB Value: (",r_s, g_s, b_s, ")")

    #These are our desired values
    r_d = 0
    g_d = 0
    b_d = 0

    # These are what we will update to the computer to change the color
    r_u = 0
    g_u = 0
    b_u = 0

    #These will be the proportional change that we add to sensor values to get update values
    r_p = 0
    g_p = 0
    b_p = 0
    
    #Derivative change variable initialization
    r_deriv = 0
    g_deriv = 0
    b_deriv = 0
    
    #Value of previous sensor values for derivatve stuff
    #We start with these errors so derivative has an initial starting point (of 0)
    r_prev = r_d-r_s
    g_prev = g_d-g_s
    b_prev = b_d-b_s
    
    kp = 0.6
    kd = 0.2
    
    try: 
        r_d = int(sys.argv[1])
        g_d = int(sys.argv[2])
        b_d = int(sys.argv[3])
        print("\nDesired RGB Value: (", sys.argv[1], sys.argv[2], sys.argv[3], ")\n")

        red_dec2 = (r_d/255)
        green_dec2 = (g_d/255)
        blue_dec2 = (b_d/255)
        
        if red_dec2 > 1:
            red_dec2 = 1
        if green_dec2 > 1:
            green_dec2 = 1
        if blue_dec2 > 1:
            blue_dec2 = 1
            
        color_desired3 = (red_dec2, green_dec2, blue_dec2)
        graph3.fill(x, y, c=color_desired3)
    
    except IndexError:
        cond = False
        failure = True
    
    update_graph(r_u, g_u, b_u)
    input("Press Enter to begin...")
    
    try: 
        while cond == True:
            y_scatter.append(r_s)
            y_scatter.append(g_s)
            y_scatter.append(b_s)
            
            colors.append("red")
            colors.append("green")
            colors.append("blue")
            
            #Errors
            r_error = r_d - r_s
            g_error = g_d - g_s
            b_error = b_d - b_s
            
            #Red
            if abs(r_error)>=5:
                r_p = int(r_error*kp)
                r_deriv = int((r_error-r_prev)*kd)
                r_u = r_s+r_p+r_deriv
            else:
                if r_s < r_d:
                    r_u = r_s+1
                elif r_s > r_d:
                    r_u = r_s-1
                else:
                    r_u = r_d
            
            #Green
            if abs(g_error)>=5:
                g_p = int(g_error*kp)
                g_deriv = int((g_error-g_prev)*kd)
                g_u = g_s+g_p+g_deriv
            else:
                if g_s < g_d:
                    g_u = g_s+1
                elif g_s > g_d:
                    g_u = g_s-1
                else:
                    g_u = g_d
            
            #Blue
            if abs(b_error)>=5:
                b_p = int(b_error*kp)
                b_deriv = int((b_error-b_prev)*kd)
                b_u = b_s+b_p+b_deriv
            else:
                if b_s < b_d:
                    b_u = b_s+1
                elif b_s > b_d:
                    b_u = b_s-1
                else:
                    b_u = b_d
            
            print("Update color R:",r_u,"G:",g_u,"B:",b_u)
            
            update_graph(r_u, g_u, b_u)
            plt.pause(1)
            plt.draw()
            
            r_s = r_u
            g_s = g_u
            b_s = b_u
            print("Sensor R:",r_s,"G:",g_s,"B:",b_s)
            
            #Update the previous error variables
            r_prev = r_error
            g_prev = g_error
            b_prev = b_error
            
            num_iterations = num_iterations + 1

            x_scatter.append(num_iterations)
            x_scatter.append(num_iterations)
            x_scatter.append(num_iterations)

            print("\n")
                
            scatter = graph2.scatter(x_scatter, y_scatter, color=colors)
            
            #Stop after you reach final iteration count
            if stop == num_iterations:
                cond = False
            
    except KeyboardInterrupt:
        sys.exit()

    if failure == True:
        print("\nFailure Occured. Please Try Again")
    else:
        print("\nComplete!\n")
        print("Iterations:",num_iterations)
        scatter = graph2.scatter(x_scatter, y_scatter, color=colors)
        try:
            plt.pause(100)
        except KeyboardInterrupt:
            sys.exit()
    







