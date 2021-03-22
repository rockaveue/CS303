from collections import deque
class Problem:
    def __init__(self, initial, goal_state=None):
        self.initial = initial
        self.goal_state = goal_state
    def actions(self, state):   
        raise NotImplementedError
    def result(self, state, action):
        raise NotImplementedError
    def goal_test(self, state):
        state == self.goal_state
        # if isinstance(self.goal, list):
        #     # return is_in(state, self.goal)
        #     return 0
        # else:
        #     return 
    def path_cost(self, c, state1, action, state2):
        return c + 1
    def value(self, state):
        raise NotImplementedError
    
class Node:
    def __init__(self, state, parent = None, action = None, path_cost = 0, depth = 0, key = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = depth
        self.key = key
        if parent:
            self.depth = parent.depth + 1
        if self.state:
            self.map = ''.join(str(e) + ', ' for e in self.state)
    def __repr__(self):
        return "<Node {}>".format(self.state)
    def __lt__(self, node):
        return self.map < node.map
    def expand(self, problem):
        return [self.child_node(problem, action)
            for action in problem.actions(self.state)]
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
        problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node
    def solution(self):
        return [node.action for node in self.path_cost[1:]]
        # return 0

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    def __eq__(self, other):
        return isinstance(other, Node) and self.map == other.map
    def __hash__(self):
        return hash(self.state)
    
class GraphProblem(Problem):
    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph
        self.goal = goal
    def actions(self, A):
        return list(self.graph.get(A).keys())
    def result(self, state, action):
        return action
    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or np.inf)
    def find_min_edge(self):
        m = np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)
        return m
    def h(self, node):
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(self.distance(locs[node], locs[self.goal]))
            return int(self.distance(locs[node.state],
                    locs[self.goal]))
        else:
            return np.inf
    def distance(self, a, b):
        return a
class GraphProblemStochastic(GraphProblem):
    def result(self, state, action):
        return self.graph.get(state, action)
    def path_cost(self):
        raise NotImplementedError
class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)
    def connect(self, A, B, distance=1):
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)
    def connect1(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2
                    in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
    
def breadth_first_graph_search(problem):
#Эхлээд хайлтын модны хамгийн гүехэн зангилааг хайх
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None
def depth_first_graph_search(problem):
 #Эхлээд хайлтын модны хамгийн гүнзгий зангилааг хайх
    frontier = [(Node(problem.initial))] # Stack
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
        if child.state not in explored and child not in frontier)
    return None
import numpy as np
def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90,
    Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))
def GraphSearch():
    problem = GraphProblem('Arad', 'Bucharest', romania_map)
    searcher = breadth_first_graph_search
    def do(searcher, problem):
        goal_node = searcher(problem)
        print('Search algorithm ', 'breadth_first_graph_search')
        print('List of nodes visited:', Node.solution(goal_node),
        ' path cost:', goal_node.path_cost)
        do(searcher, problem)
        GraphSearch()
    
    do(searcher, problem)

def main():
    GraphSearch()

if __name__ == "__main__":
    main()