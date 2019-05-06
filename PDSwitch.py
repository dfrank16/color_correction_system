#P-Controller
num_iterations = 0
stop = 30
#Values from sensor
r_s = 27
g_s = 50
b_s = 160
print("R:",r_s,"G:",g_s,"B:",b_s)
#Desired values
r_d = 199
g_d = 31
b_d = 203
#Update values
r_u = 0
g_u = 0
b_u = 0
cond = True
#Proportional change variable initialization
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
while cond == True:
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
    #Here is where we would update the color but this hasn't been implemented
    #yet, so I'm using this as a temporary replacement for testing
    r_s=r_u
    g_s=g_u
    b_s=b_u
    #Update the previous error variables
    r_prev = r_error
    g_prev = g_error
    b_prev = b_error
    print("R:",r_s,"G:",g_s,"B:",b_s)
    num_iterations = num_iterations + 1
    #Stop if the proportional values are zero
    # if r_p==0 and g_p==0 and b_p==0:
    #New: stop after you reach final iteration count
    if stop == num_iterations:
        cond = False
print("Iterations:",num_iterations)
