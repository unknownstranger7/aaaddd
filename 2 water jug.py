class node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.parent = data

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


def printPath(solutionNode):
    path = []
    while solutionNode is not None:
        path.insert(0, solutionNode)
        solutionNode = solutionNode.parent

    for node in path:
        print(node, end=" -> ")


def isGoalNode(cnode, gnode):
    return cnode.x == gnode.x and cnode.y == gnode.y


def operation(cnode, rule):
    x = cnode.x
    y = cnode.y

    if rule == 1:
        # Fill Jug 1
        if x < maxjug1:
            x = maxjug1
        else:
            return None
    elif rule == 2:
        # Fill Jug 2
        if y < maxjug2:
            y = maxjug2
        else:
            return None
    elif rule == 3:
        # Empty Jug 1
        if x > 0:
            x = 0
        else:
            return None
    elif rule == 4:
        # Empty Jug 2
        if y > 0:
            y = 0
        else:
            return None
    elif rule == 5:
        # Pour Jug 2 to Jug 1
        if x + y >= maxjug1:
            y = y - (maxjug1 - x)
            x = maxjug1
        else:
            return None
    elif rule == 6:
        # Pour Jug 1 to Jug 2
        if x + y >= maxjug2:
            x = x - (maxjug2 - y)
            y = maxjug2
        else:
            return None
    elif rule == 7:
        # Pour all water from Jug 2 to Jug 1
        if x + y < maxjug1:
            x = x + y
            y = 0
        else:
            return None
    elif rule == 8:
        # Pour all water from Jug 1 to Jug 2
        if x + y < maxjug2:
            y = x + y
            x = 0
        else:
            return None

    if (x == cnode.x and y == cnode.y):
        return None

    nextnode = node(cnode)
    nextnode.x = x
    nextnode.y = y
    nextnode.parent = cnode

    return nextnode


class BfsAlgo:
    def __init__(self):
        self.bfsq = []

    def is_empty(self, l):
        return len(l) == 0

    def pushlist(self, list1):
        self.bfsq.extend(list1)

    def popnode(self):
        if self.is_empty(self.bfsq):
            return None
        else:
            return self.bfsq.pop(0)

    def generateAllSuccessors(self, cnode):
        list1 = []

        for rule in range(1, 9):
            nextnode = operation(cnode, rule)

            if nextnode is not None:
                list1.append(nextnode)

        return list1

    def bfsMain(self, initialNode, GoalNode):
        self.bfsq.append(initialNode)

        while not self.is_empty(self.bfsq):
            visited_node = self.popnode()
            # print("visited Node : " + str(visited_node))

            if isGoalNode(visited_node, GoalNode):
                return visited_node

            successor_nodes = self.generateAllSuccessors(visited_node)
            self.pushlist(successor_nodes)
            # print("successors : " + str(successor_nodes))

        return None


if __name__ == '__main__':
    list2 = []

    maxjug1 = int(input("Enter the value of jug1: "))
    maxjug2 = int(input("Enter the value of jug2: "))

    initialNode = node(None)

    initialNode.x = 0
    initialNode.y = 0
    initialNode.parent = None

    GoalNode = node(None)

    GoalNode.x = int(input("Enter value of Goal in Jug 1: "))
    GoalNode.y = 0
    GoalNode.parent = None

    solutionNode = BfsAlgo().bfsMain(initialNode, GoalNode)

    if solutionNode is not None:
        printPath(solutionNode)
    else:
        print("Solution Not Found!!!")

    print("Done")
