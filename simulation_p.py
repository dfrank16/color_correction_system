from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import os
import argparse
import random

# Update the control graph to dipslay the current colors
def update_graph(red, green, blue):
    # Turn the input values into decimals
    red_dec = (red/255)
    green_dec = (green/255)
    blue_dec = (blue/255)

    # Fix irroneous values that may pop up
    if red_dec > 1:
        red_dec = 1
    if green_dec > 1:
        green_dec = 1
    if blue_dec > 1:
        blue_dec = 1

    # Display the new color
    color_desired = (red_dec, green_dec, blue_dec)
    graph.fill(x, y, c=color_desired)

if __name__ == '__main__':
    # Initialize the graphs
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
    
    # These are the the sensor values that we are using for simulation
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
    
    #Change this value around until you find something that works!
    kp = 0.6
    
    try: 
        # Grabs the input arguments when started the program
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
            
        color_desired2 = (red_dec2, green_dec2, blue_dec2)
        graph3.fill(x, y, c=color_desired2)
    
    except IndexError:
        # If there is an error with the input arguments, stop the program
        cond = False
        failure = True
    
    update_graph(r_u, g_u, b_u)
    input("Press Enter to begin...")

    try: 
        while cond == True:
            # Add the updated colors to the graph
            y_scatter.append(r_s)
            y_scatter.append(g_s)
            y_scatter.append(b_s)
            
            # Add the respective colors to display the points
            colors.append("red")
            colors.append("green")
            colors.append("blue")
            
            # Update the P values
            r_p = int((r_d-r_s)*kp)
            g_p = int((g_d-g_s)*kp)
            b_p = int((b_d-b_s)*kp)
            print("P R:",r_p,"G:",g_p,"B:",b_p)
            
            #Now update the screen using the above values
            r_u = r_s+r_p
            g_u = g_s+g_p
            b_u = b_s+b_p
            print("Update color R:",r_u,"G:",g_u,"B:",b_u)
            
            # Update the graph with the new values
            update_graph(r_u, g_u, b_u)
            plt.pause(1)
            plt.draw()
            
            # Update sensor values for simulation
            r_s = r_u
            g_s = g_u
            b_s = b_u
            print("Sensor R:",r_s,"G:",g_s,"B:",b_s)
            
            num_iterations = num_iterations + 1

            # Add three values to properly set up the x axis for the new points
            x_scatter.append(num_iterations)
            x_scatter.append(num_iterations)
            x_scatter.append(num_iterations)
            
            print("\n")
                
            # Update the scatter plot with the new values
            scatter = graph2.scatter(x_scatter, y_scatter, color=colors)

            if num_iterations == 15:
                r_s = random.randint(0, 255)
                g_s = random.randint(0, 255)
                b_s = random.randint(0, 255)
            
            #Stop after you reach final iteration count
            if stop == num_iterations:
                cond = False
            
    except KeyboardInterrupt:
        # Exit if ctrl-C is detected
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
    







