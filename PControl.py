#P-Controller
#There is a reason why Kp is less than one, stored in my notes
#Change the input RGB values based on difference from their desired values

#To count how long this takes
num_iterations = 0

#This is if we want to go for a set number of iterations instead of going till
#we get to a certain RGB value/range
stop = 30 #Change this value as you see fit

#Here is where we obtain values from the sensor
r_s = 27
g_s = 50
b_s = 160
#Print the initial sensor readings
print("R:",r_s,"G:",g_s,"B:",b_s)

#These are our desired values
r_d = 199
g_d = 31
b_d = 203

# These are what we will update to the computer to change the color
r_u = 0
g_u = 0
b_u = 0

cond = True

#These will be the proportional change that we add to sensor values to get update values
r_p = 0
g_p = 0
b_p = 0
#Also, here is the Kp value to be multiplied to the error.
#Change this value around until you find something that works!
kp = 0.4
#Note: When I did ZN Tuning Rules for this prototype (without the sensor
#actually running), I found Kc=2, but let's just say Kc=1.9 to make it look more
#legit.  Tc = 2 iterations.  So, ZN says we use Kp=0.5Kc for P-Control
#Decided not to use the ZN value for now
#These values will likely be different when we do the real thing

while cond == True:
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
    #Stop if the proportional values are zero
    # if r_p==0 and g_p==0 and b_p==0:
    #New: stop after you reach final iteration count
    if stop == num_iterations:
        cond = False
print("Iterations:",num_iterations)
