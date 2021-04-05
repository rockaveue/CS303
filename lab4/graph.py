from collections import deque
from english_words import english_words_lower_alpha_set
import string
import enchant
# natural language toolkit сан
# from nltk.corpus import wordnet
import time
class Problem:
    def __init__(self, initial, goal_state=None):
        self.initial = initial
        self.goal_state = goal_state
    def actions(self, state):   
        raise NotImplementedError
    def result(self, state, action):
        raise NotImplementedError
    def goal_test(self, state):
        # state == self.goal_state
        if isinstance(self.goal_state, list):
            # return is_in(state, self.goal)
            return 0
        else:
            return state == self.goal_state
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
    def __repr__(self):
        return "<Node {}>".format(self.state)
    def __lt__(self, node):
        return self.state < node.state
    def expand(self, problem):
        return [self.child_node(problem, action)
            for action in problem.actions(self.state)]

    # graph-аа үүсгэх функц
    def myexpand(self, problem):
        # mygraph дээр өмнөх графаа аваад mysearch2 функцийг дуудна
        mygraph = problem.graph.graph_dict
        # frontier-с авсан үг болон ерөнхий графаар дуудна
        mygraph = self.mysearch2(self.state, mygraph)
        # print(mygraph)
        return mygraph
        
    # Тухайн үгийн үсгүүдийг сольж үг мөн бол тухайн үгийн value-д хийх функц
    # initialState - тухайн хайх үг
    # graph - өмнөх графаа авах утга
    def mysearch2(self, initialState, graph):
        d = enchant.Dict("en_US")
        # англи 26 үсэг
        # үгийн урт * 26-н давталт хийнэ
        letters = string.ascii_lowercase
        # ugiin urt
        wordLen = len(initialState)
        # тухайн үгээр хайгаагүй бол хайлтуудыг хадгалах dict үүсгэв
        if not initialState in graph:
            graph[initialState] = dict()
        # дээр үүсгэсэн dict-г хувьсагчид хадгалав
        state_dict = graph[initialState]
        for i in range(wordLen):
            # орж ирсэн үг рүү index-ээр хандахын тулд list болгов
            initial_state_in_list = list(initialState)
            # тухайн үгийн анх байсан үсгийн хадгалав
            baisan_letter = initial_state_in_list[i]
            for j in letters:
                # Анх байснаас бусад 25 тохиолдолд үгийн уртын тоогоор давтаж
                # англи үг мөн бол dict-д хадгална
                if j != baisan_letter:
                    initial_state_in_list[i] = j
                    new_state = ''.join(initial_state_in_list)
                    # Англи үгийн санд байгаа эсэхийг шалгах хэсэг
                    # if new_state in english_words_lower_alpha_set: # english_words сангийх
                    if d.check(new_state): # enchant сангийх
                    # if wordnet.synsets(new_state): # nltk.corpus.wordnet сангийх
                       state_dict[new_state] = 1
        # үүссэн шинэ граф-ийг буцаана
        return graph
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node
    def solution(self):
        # return [node.action for node in self.path_cost[1:]]
        return [node.action for node in self.path()[1:]]
        # return 0

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    def __eq__(self, other):
        # return isinstance(other, Node) and self.map == other.map
        return isinstance(other, Node) and self.state == other.state
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
        self.graph_dict = graph_dict or {} # graph
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
        # print(node.state)
        # дээр үүсгэсэн функцээр тухайн үгийг үгнүүдэд хуваан задлах үйлдэл
        graph = node.myexpand(problem)
        for child in node.expand(problem):
            # print(child)
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    print("Граф")
                    # Хамгийн сүүлд үүссэн графаа recursive функц ашиглан задлав
                    for key, value in recursive_items(problem.graph.graph_dict):
                        # түлхүүр болон утгын түлхүүрүүдийг л хэвлэв
                        print(key, {k for k in value.keys()})
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
            print("Граф")
            # print(problem.graph.graph_dict)
            # Хамгийн сүүлд үүссэн графаа recursive функц ашиглан задлав
            for key, value in recursive_items(problem.graph.graph_dict):
                # түлхүүр болон утгын түлхүүрүүдийг л хэвлэв
                print(key, {k for k in value.keys()})
            return node
        explored.add(node.state)
        graph = node.myexpand(problem)
        frontier.extend(child for child in node.expand(problem)
        if child.state not in explored and child not in frontier)
    return None
# nested dictionary задлах функц
def recursive_items(dictionary):
    for key, value in dictionary.items():
        # хэрэв value нь dict бол функцийг дахин дуудна
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        # else:
            # yield (key, value)
# хугацаа миллисекундээр авах функц
def current_milli_time():
    return round(time.time() * 1000)
import numpy as np
def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)

# Жишээ граф
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
# Лабораторийн ажлын жишээ граф
my_map = UndirectedGraph(dict(
    fool = dict(foul=1, foil=1, cool=1, pool=1),
    fail = dict(fall=1, foil=1),
    pall = dict(pale=1, poll=1, fall=1),
    poll = dict(pool=1, pole=1),
    pope = dict(pole=1),
    pale = dict(pole=1, sale=1, page=1),
    sage = dict(sale=1, page=1)
))
# Тухайн үг үгийн санд байдаг эсэхийг шалгах функц
def checkWord(word):
    if word in english_words_lower_alpha_set:
        return True
    else:
        return False
def GraphSearch():
    first = input("Эхний үгийг оруулна уу.")
    while not checkWord(first):
        first = input("Боломжгүй үг байна. Дахин оруулна уу.")
    last = input("Хувиргах үгийг оруулна уу.")
    while not checkWord(last):
        last = input("Боломжгүй үг байна. Дахин оруулна уу.")
    # problem = GraphProblem('fool', 'sage', my_map)
    # Хоосон dict утгатай граф-тай, анхны болон зорилгын төлөвтэй асуудал үүсгэв
    problem = GraphProblem(first, last, UndirectedGraph(dict()))
    searcher = breadth_first_graph_search # depth_first_graph_search
    def do(searcher, problem):
        t = current_milli_time() # Хайлт хийхээс өмнөх цагийг авав
        goal_node = searcher(problem)
        t = current_milli_time() - t # Хайлт дууссаны дараах цагийг аван хасав
        print(f"Хайлт хийсэн хугацаа {t}ms")
        if goal_node != None: # Хайлтаас хариу олдвол
            print('Хайлтын алгоритм ', searcher.__name__)
            print('Орсон node-үүд :', Node.solution(goal_node),
            ' path cost:', goal_node.path_cost)
        else: # хариу олдоогүй бол
            print("Граф")
            # Хамгийн сүүлд үүссэн графаа recursive функц ашиглан задлав
            for key, value in recursive_items(problem.graph.graph_dict):
                # түлхүүр болон утгын түлхүүрүүдийг л хэвлэв
                print(key, {k for k in value.keys()})
            print('үгийг холбох боломжгүй')
    
    do(searcher, problem)

def main():
    GraphSearch()
    

if __name__ == "__main__":
    main()