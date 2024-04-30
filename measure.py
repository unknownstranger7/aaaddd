def measure_d(d):
    solution = []
    steps = 0

    m = int(input("Enter a value for m: "))
    n = int(input("Enter a value for n: "))

    initial_state = [m , 0]
    solution.append([0,0])
    solution.append(initial_state)


    while True:
        
        if initial_state[1] < n:
            to_pour = n - initial_state[1]
            if to_pour - initial_state[0] >= 0 and initial_state[0] > 0:
                initial_state = [0,initial_state[1] + initial_state[0]]
                solution.append(initial_state)
                steps += 1

            elif initial_state[0] == 0:
                initial_state = [m,initial_state[1]]
                solution.append(initial_state)
                steps += 1
            
            else:
                initial_state = [initial_state[0] - to_pour,n]
                solution.append(initial_state)
                steps += 1
            

        elif initial_state[1] == n:
            initial_state = [initial_state[0],0]
            solution.append(initial_state)
            steps += 1

        

        if initial_state[0] == d or initial_state[1] == d:
            steps += 1
            return solution, steps

        
    
d = int(input("Enter the amount you want to measure: "))
solved , min_steps = measure_d(d)
print(f'Number of Steps                   : {min_steps}')
print(f'State of the Jugs after each Step : {solved}')
