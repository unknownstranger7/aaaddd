# tree = {'S': [['A', 1], ['B', 5], ['C', 8]],
#         'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
#         'B': [['S', 5], ['G', 4]],
#         'C': [['S', 8], ['G', 5]],
#         'D': [['A', 3]],
#         'E': [['A', 7]]}
# heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}

def AStarSearch(startHeu):
    closed = []             # closed nodes
    opened = [['S', startHeu]]     # opened nodes

    # find the visited nodes
    while True:
        # print(opened)
        fn = [i[1] for i in opened]     # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # current node
        closed.append(opened[chosen_index])
        
        del opened[chosen_index]
        if node == 'G':        # break the loop if node G has been found
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})            # add nodes to cost dictionary
            fn_node = cost[node] + heuristic[item[0]] + item[1]     # calculate f(n) of current node()
            temp = [item[0], fn_node]
            opened.append(temp)                                     # store f(n) of current node in array opened

    # find optimal sequence
    trace_node = 'G'                        # correct optimal tracing node, initialize as node G
    optimal_sequence = ['G']                # optimal node sequence
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]           # current node
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
            change the correct optimal tracing node to current node'''
            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:  # start to check_node + check_node to trace_node = start to trace_node
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()              # reverse the optimal sequence

    return closed, optimal_sequence

from collections import defaultdict

if __name__ == '__main__':
    tree = defaultdict(list)
    cost = {'S': 0}             # total cost for nodes visited (only edge addition from satrt to node is considered without h(n))
    heuristic = {
        'S': 0,
        'A': 5, 
        'B': 10, 
        'C': 7, 
        'D': 0, 
        'E': 9, 
        'G': 0
    }
    
    while True:
        ip = input("if done press 'q'\nEnter graph in this order start(s) adjacent(e) weight(w): ").upper().split(" ")
        if "Q" in ip:
            break
        tree[ip[0]].append([ip[1], int(ip[2])])
    # print(tree)
    visited_nodes, optimal_nodes = AStarSearch(heuristic["S"])
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))