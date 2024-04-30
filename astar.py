import heapq

def astar(start,goal,graph,heuristic):
    open_list = [(0,start)]
    close_list = set()
    parents = {start:None}
    g_scores = {start:0}

    while open_list:
        f_score,current = heapq.heappop(open_list)

        if current==goal:
            print("Goal reached !")
            path =[]
            while current:
                path.append(current)
                current = parents[current]
            print(path)
            return path
        else:
            close_list.add(current)

            for neighbour in graph[current]:
                if neighbour in close_list:
                    continue
                else:
                    temp_g_score = g_scores[current] + graph[current][neighbour]
                    if neighbour not in [n[1] for n in open_list]:
                        f_score = heuristic(neighbour,goal) + temp_g_score
                        heapq.heappush(open_list,(f_score,neighbour))
                    elif temp_g_score < g_scores[neighbour]:
                        index = [n[1] for n in open_list].index(neighbour)
                        f_score = heuristic(neighbour,goal) + temp_g_score
                        open_list[index] = (f_score,neighbour) 
                    parents[neighbour] = current
                    g_scores[neighbour] = temp_g_score            
graph = {
    "A": {"B": 6, "F": 3},
    "B": {"D": 2, "C": 3, "A": 6},
    "C": {"E": 5, "D": 1, "B": 3},
    "D": {"E": 8, "B": 2, "C": 1},
    "E": {"I": 5, "J": 5, "C": 5, "D": 8},
    "J": {"I": 3, "E": 5},
    "I": {"G": 3, "H": 2, "J": 3, "E": 5},
    "G": {"F": 1, "I": 3},
    "H": {"F": 7, "I": 2},
    "F": {"A": 3, "G": 1, "H": 7},
}


# Heuristic function.
def heuristic(node, goal):
    h_scores = {
        "A": 10,  # Estimated distance from A to J
        "B": 8,  # Estimated distance from B to J
        "C": 5,  # Estimated distance from C to J
        "D": 7,  # Estimated distance from D to J
        "E": 3,  # Estimated distance from E to J
        "F": 6,  # Estimated distance from F to J
        "G": 5,  # Estimated distance from G to J
        "H": 3,  # Estimated distance from H to J
        "I": 1,  # Estimated distance from I to J
        "J": 0,  # Estimated distance from J to J (goal)
    }
    return h_scores[node]


# Find path from A to J.
path = astar("A", "J", graph, heuristic)
if path:
    print("Path found:", path)
else:
    print("No path found.")