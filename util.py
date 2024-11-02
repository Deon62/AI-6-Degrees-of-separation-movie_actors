class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    #intialize frontier as empty list
    def __init__(self):
        self.frontier = []

#add node to frontier
    def add(self, node):
        self.frontier.append(node)
#check if frontier contains node
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
#check if frontier is empty
    def empty(self):
        return len(self.frontier) == 0
#remove node from frontier
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        #return last node in frontier
        else:
            node = self.frontier[-1]
            #remove last node from frontier
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
