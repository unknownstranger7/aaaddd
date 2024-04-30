def measure_d(d):
    """
    This function finds the minimum number of steps required to measure a given volume 'd' using two jugs of different capacities.

    Args:
        d (int): The target volume to be measured.

    Returns:
        tuple: A tuple containing the list of states of the jugs after each step, and the minimum number of steps required.
    """
    solution = []  # List to store the states of the jugs after each step


    steps = 0   # Counter for the number of steps

    # Prompt the user to enter the capacities of the two jugs
    m = int(input("Enter a value for m: "))
    n = int(input("Enter a value for n: "))

    initial_state = [m , 0]
    solution.append([0,0])
    solution.append(initial_state)

    while True:
       # Check if the current volume in the second jug is less than the target volume
        if initial_state[1] < n:
            # Calculate the amount of water needed to fill the second jug to the target volume
            to_pour = n - initial_state[1]
            # Check if the first jug has enough water to fill the second jug to the target volume
            if to_pour - initial_state[0] >= 0 and initial_state[0] > 0:
                initial_state = [0,initial_state[1] + initial_state[0]]
                solution.append(initial_state)
                steps += 1
            
            # If the first jug is empty, refill it and add the state to the solution list
            elif initial_state[0] == 0:
                initial_state = [m,initial_state[1]]
                solution.append(initial_state)
                steps += 1
           # Otherwise, pour the remaining water from the first jug into the second jug
            else:
                initial_state = [initial_state[0] - to_pour,n]
                solution.append(initial_state)
                steps += 1
            
        # If the volume in the second jug is equal to the target volume, empty the second jug
        elif initial_state[1] == n:
            initial_state = [initial_state[0],0]
            solution.append(initial_state)
            steps += 1

        # If the volume in either of the jugs is equal to the target volume, return the solution and the number of steps
        if initial_state[0] == d or initial_state[1] == d:
            steps += 1
            return solution, steps

        
    
d = int(input("Enter a value for d: "))
if(d<0):
    print("Invalid Input")
    exit()
solved , min_steps = measure_d(d)
print(f'Number of Steps                   : {min_steps}')
print(f'State of the Jugs after each Step : {solved}')