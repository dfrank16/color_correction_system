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
    plt.ion()
    fig, graph = plt.subplots()
    x = [0, 0, 1, 1]
    y = [0, 1, 1, 0]
    cond = True
    failure = False
    num_iterations = 0
    stop = 30
    
    r_s = 27
    g_s = 50
    b_s = 160
    print("R:",r_s,"G:",g_s,"B:",b_s)

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
    kp = 0.4
    
    try: 
        r_d = int(sys.argv[1])
        g_d = int(sys.argv[2])
        b_d = int(sys.argv[3])
        print("\nDesired RGB Value: (", sys.argv[1], sys.argv[2], sys.argv[3], ")\n")
    except IndexError:
        cond = False
        failure = True
    
    try: 
        while cond == True:
            update_graph(r_s, g_s, b_s)
            plt.pause(0.01)
            plt.draw()
            
            r_p = int((r_d-r_s)*kp)
            g_p = int((g_d-g_s)*kp)
            b_p = int((b_d-b_s)*kp)
            
            #Now update the screen using the above values
            r_u = r_s+r_p
            g_u = g_s+g_p
            b_u = b_s+b_p
            
            #Here is where we would update the color but this hasn't been implemented
            #yet, so I'm using this as a temporary replacement for testing
            r_s=r_u
            g_s=g_u
            b_s=b_u
            print("R:",r_s,"G:",g_s,"B:",b_s)
            
            num_iterations = num_iterations + 1
            
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
        plt.pause(3)
    







