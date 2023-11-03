import time

# Define the time frame in minutes
time_frame_minutes = 10  # Change this to the desired time frame

# Get the first input from the user
input1 = input("Enter the first input: ")

# Added some change by Balu
# Record the time when the first input was entered
start_time = time.time()

# Get the second input from the user
input2 = input("Enter the second input: ")

# Calculate the time elapsed in seconds
time_elapsed = time.time() - start_time
#time_elapsed_minutes = time_elapsed / 60  # Convert seconds to minutes

# Check if the inputs match and if they were entered within the time frame
if input1 == input2 :
    if time_elapsed <= time_frame_minutes:
        print("Inputs match and were entered within the time frame. Access granted.")
    else :
        print("Inputs match but time exceeds. Hence pin has expired")
else:
    print("Inputs do not match. Access denied.")
