def measure(d):

    solutions = []
    steps = 0

    m = int(input("Enter the value of m : " ))
    n = int(input("Enter the value of n : " ))

    initial_state = [m,0]
    solutions.append([0,0])
    solutions.append(initial_state)

    while True:
        
        if initial_state[1] < n:
            to_pour = n - initial_state[1]

            if to_pour-initial_state[0] >= 0 and initial_state[0] > 0:
                initial_state = [0,initial_state[1] + initial_state[0]]
                

            elif initial_state[0] == 0:
                initial_state = [m,initial_state[1]]

            else:
                initial_state = [initial_state[0] - to_pour,n]

            solutions.append(initial_state)
            steps +=1

        elif initial_state[1] == n:
            initial_state = [initial_state[0],0]
            solutions.append(initial_state)
            steps+=1
        
        if initial_state[0] == d or initial_state[1] == d:
            step+=1
            return solutions,steps
        
    
    