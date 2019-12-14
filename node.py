from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt


G_dfs = nx.Graph()
G_bfs = nx.Graph()

class Node:
    goal_state = [0,0,1]
    no_of_nodes = 0
    def __init__(self, parent, state):
    
        self.state = state
        self.parent = parent        
    def is_goal_state(self):
        if self.state == self.goal_state:
            return True
        else:
            return False

    def is_valid(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        if missionaries >= 0 and missionaries <= 3 and cannibals >= 0 and cannibals <= 3:
            return True
        return False
    
    def is_killed(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        if missionaries < cannibals and missionaries > 0:
            return True
        elif missionaries > cannibals and missionaries < 3:
            return True
    
    def expand(self):
        children = []
        b = 1 # boat in right shore 
        o = -1
        if self.state[2] == 1: 
            b = 0 #boat in left shore
            o = 1
        for x in range(3):
            for y in range(3):
                new_state = self.state.copy()
                new_state[0], new_state[1], new_state[2] = new_state[0] + o * x, new_state[1] + o * y, b
                new_node = Node(self, new_state)
                if new_node.is_valid() and (x + y >=1 and x + y <= 2):
                    children.append(new_node)

        return children


def bfs(i_state):
    i_node = Node(None, i_state)

    if i_node.is_goal_state():
        return i_node

    q = Queue()
    q.put(i_node)

    visited = []

    while not(q.empty()):
        node = q.get()
        if node.state not in visited:
            visited.append(node.state)

        G_bfs.add_node(str(node.state),color='Killed Node')
    
        if node.parent:
            G_bfs.add_edge(str(node.parent.state), str(node.state))        
        
        if not node.is_killed():
            G_bfs.nodes[str(node.state)]['color'] = 'Traversed Node'
            children = node.expand()
            for child in children:
                if child.state not in visited:
                    if child.is_goal_state():
                        G_bfs.add_node(str(child.state), color='Goal Node')
                        G_bfs.add_edge(str(child.parent.state), str(child.state))
                        return child
                    else:
                        visited.append(child.state)
                        q.put(child)
    return

def dfs(i_state):
    i_node = Node(None, i_state)
    if i_node.is_goal_state():
        return i_node

    visited = []
    s = []
    s.append(i_node)
    while s:
        node = s.pop()
        if node.state not in visited:
            visited.append(node.state)

        G_dfs.add_node(str(node.state), color='Killed Node')

        if node.parent:
            G_dfs.add_edge(str(node.parent.state), str(node.state))

        if not node.is_killed():
            G_dfs.nodes[str(node.state)]['color'] = 'Traversed Node'
            children = node.expand()    
            for child in children:
                if child.state not in visited:
                    if child.is_goal_state():
                        G_dfs.add_node(str(child.state), color='Goal Node')
                        G_dfs.add_edge(str(child.parent.state), str(child.state))  
                        # print("returned")                      
                        return child
                    
                    else:
                        # print(f"{node.state} is not a goal state")
                        visited.append(child.state)
                        s.append(child)
    return  None

def optimize_graph(G):
    e = list(G.edges)
    for i in range(len(e)-1):
        for j in range(i+1, len(e)-1):
            if e[i][1] == e[j][1]:
                if G.has_edge(e[j][0], e[j][1]):
                    G.remove_edge(e[j][0], e[j][1])
    return G

def find_path(solution):
    path = []
    path.append(solution.state)
    parent = solution.parent
    while parent:
        path.append(parent.state)
        parent = parent.parent
    path.reverse()
    return path
i_state = [3,3,0]
bfs(i_state)
dfs(i_state)
# print("bfs = ",b)
# print("dfs= ", d)
G_bfs_optimized = optimize_graph(G_bfs)
G_dfs_optimized = optimize_graph(G_dfs)



