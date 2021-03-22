from matplotlib import pyplot as plt 
import cv2
import glob
import random
from collections import deque

moves = list()
orson = 0

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
    # def expand(self, problem):
    #     return [self.child_node(problem, action)
    #         for action in problem.actions(self.state)]
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
        problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node
    def solution(self):
        return [node.action for node in self.path()[1:]]

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
    
    # хөдөлгөх функц
    def move(self, state, position):
        bside = 3   # мөр баганы тоо        # 0 1 2
        blen = 9    # нийт урт              # 3 4 5
        shine_state = state[:]              # 6 7 8
        index = shine_state.index(0)
        # төлвийг хуулан хоосон нүдийн index-ийг авав
        global orson
        orson += 1
        if position == 1: # deeshee 
            # хэрэв index 0, 1, 2 байвал дээшээ явж болохгүй
            if index not in range(0, bside): 
                # swap хийх үйлдэл
                temp = shine_state[index - bside] # одоогийн index нь 
                shine_state[index - bside] = shine_state[index]
                shine_state[index] = temp
                return shine_state
            # y x x       0 x x
            # 0 x x   →   y x x
            # x x x       x x x
            else:
                return None # тулчихсан тул None-ийг буцаав
        if position == 2: #dooshoo
            if index not in range(blen - bside, blen): # 6 7 8 байвал
                temp = shine_state[index + bside]
                shine_state[index + bside] = shine_state[index]
                shine_state[index] = temp
                return shine_state
            else:
                return None
        if position == 3: #zuun
            if index not in range(0, blen, bside): # 0 3 6
                temp = shine_state[index - 1]
                shine_state[index - 1] = shine_state[index]
                shine_state[index] = temp
                return shine_state
            else:
                return None
        if position == 4: # baruun
            if index not in range(bside - 1, blen, bside): # 2 5 8
                temp = shine_state[index + 1]
                shine_state[index + 1] = shine_state[index]
                shine_state[index] = temp
                return shine_state
            else:
                return None
    # дээш, доош, зүүн, баруун 4-н үйлдлээр тэлэх функц
    def expand(self, node):
        hursh = list()
        # Гаргаж болох 4-н хүү зангилаа
        hursh.append(Node(self.move(node.state, 1), node, 1, node.depth + 1, node.path_cost + 1, 0))
        hursh.append(Node(self.move(node.state, 2), node, 2, node.depth + 1, node.path_cost + 1, 0))
        hursh.append(Node(self.move(node.state, 3), node, 3, node.depth + 1, node.path_cost + 1, 0))
        hursh.append(Node(self.move(node.state, 4), node, 4, node.depth + 1, node.path_cost + 1, 0))
        
        # аль нэг тийшээ явах гээд тулаад явж чадаагүй node-үүдээс бусдыг нь буцаана
        nodes = [temp for temp in hursh if temp.state != None]
        return nodes
    
class MyProblem(Problem):
    def __init__(self, state):
        self.goal_state = [1,2,3,4,5,6,7,8,0] # zorilgo
        self.state = state # анхны төлөв
        self.test = 0
        super().__init__(self.state, self.goal_state)
    def goal_test(self, state):
        return state == self.goal_state
    
    # goal дээр ирсэн үед буцаад анхны төлөв хүртэл нь давтаад
    # хийсэн үйлдлүүдийг state хэлбэрээр авах функц
    def backtrace(self, node):
        current_node = node.parent
        states = [] # үйлдэл хийсний дараах node бүрийн state-ийг авах лист
        # зураг эвлэсэн төлвөөс эвлээгүй төлөв хүртэлх давталт
        while self.state != current_node.state:
            states.insert(0,current_node.state)
            current_node = current_node.parent # эцэг рүү нь очих
        return states
    
    # дээрх функцтэй ижил гэхдээ үйлдэл хэлбэрээр авах функц
    def backtraceMove(self, node):
        moves = [] # хийсэн үйлдлүүдээ хадгалах лист
        current_node = node.parent
        # зураг эвлэсэн төлвөөс эвлээгүй төлөв хүртэлх давталт
        while self.state != current_node.state:
            if current_node.action == 1:
                movement = 'дээш'
            elif current_node.action == 2:
                movement = 'доош'
            elif current_node.action == 3:
                movement = 'зүүн'
            else:
                movement = 'баруун'
            moves.insert(0, movement)
            current_node = current_node.parent # эцэг рүү нь очих
        return moves
        
# zurah uildeltei class
class Environment:
    def __init__(self):
        self.fig = plt.figure(figsize=(6,6), num = "Laboratory 3") 
        # 3-3 харьцаатай хүснэгтийн мөр багана
        self.rows = 3
        self.columns = 3
        self.mur = 0
        self.bagana = 0
        # хоосон нүд байгаа index
        self.index = 5
        j = 1
        # нийт зураг болон түүний дугаар байх dict
        self.imgs = {}
        # 0 гэсэн утгыг хоосон гэж бодов
        self.imgs[0] = '0'
        # imgs dict-д 1-9 хүртэл бүх зургаа хийж байна
        for i in range(3):
            for k in range(3):
                self.imgs[j] = glob.glob(f"images/logoo_0{i+1}_0{k+1}.png")[0]
                j += 1
        del self.imgs[9] # хамгийн сүүлийн зургийг хасах
        
        # хийсэн зургуудаа temp-д хийн хольж байна(зургуудын номероор)
        temp = list(self.imgs.keys())[:]
        random.shuffle(temp)
        # zurgiin dugaar boloh state iig hiihed zurgiig gargana
        self.index = temp.index(0) + 1
        # анхны төлвийг зурах үйлдэл
        # self.readImage(self, temp)
        self.state = temp
        # санамсаргүйгээр гарсан төлөв
        print(f"Анхны төлөв = {self.state}\n")
        
    def get_value(self, val):
        for key, value in self.imgs.items():
            if val == key:
                return value
    
        return "value doesn't exist"
    # value-гаар түлхүүр олох функц
    def get_key(self, val):
        for key, value in self.imgs.items():
            if val == value:
                return key
    
        return "value doesn't exist"
    
    # зургийн дугаар авч зураг үзүүлэх функц
    def displayImage(self, image, i):
        ax = self.fig.add_subplot(self.rows, self.columns, i)
        # deer bichsen tulhuur oloh funktseer zurgiin dugaariig olon tavij baina
        ax.annotate(self.get_key(image), xy = (50,350), fontsize = 20)
        # cv2 нь зургийг RGB биш BGR байдлаар ашигладаг ту cv2.cvtColor функцийг ашиглан RGB болгоно.
        plt.imshow(cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)) 
        plt.axis('off') 
    
    def readImage(self, state):
        imgPaths = [self.get_value(key) for key in state]
        # 0 буюу хоосон нүд байгаа index
        index = state.index(0) + 1
        j = 1
        for imgPath in imgPaths:
            # хоосон нүд байвал зураг биш өнгө хийнэ
            if j == index:
                ax = self.fig.add_subplot(self.rows, self.columns, j) # 3-3 харьцаатай зүйлийн хэддэх дээр нь байрлуулахийг тогтооно
                plt.imshow([[(0.5,0.5,0.5)]]) # 0.5 0.5 0.5 өнгөтэй плот үзүүлж байна
                ax.annotate(self.get_key('0'), xy = (-0.4,0.35), fontsize = 20) # тоо гаргаж ирж буй функц
                plt.scatter(0, 0, s = 100, marker = 'D') # тэмдэг гаргаж ирж буй үйлдэл
                plt.axis("off")
            else: # хоосон нүд биш бол зургийн path-ийг хайж зураг болгон дүрслэнэ
                self.displayImage(imgPath, j)
                # print(file)
            j += 1
        plt.show(block=False) # block-ийг false болгосноор responsive figure-тэй болгоно
        plt.pause(0.3) # 0.3 секундийн pause аван дараагийн figure-ийг дүрслэхэд бэлдэнэ
        plt.clf()
        
    # хамгийн сүүлийн дүрсийг дуудахад ашиглана
    # clf хийхгүй учир фигүр устахгүй
    def readImageWithoutClf(self, state):
        imgPaths = [self.get_value(key) for key in state]
        index = state.index(0) + 1
        j = 1
        for imgPath in imgPaths:
            if j == index:
                ax = self.fig.add_subplot(self.rows, self.columns, j)
                plt.imshow([[(0.5,0.5,0.5)]])
                ax.annotate(self.get_key('0'), xy = (-0.4,0.35), fontsize = 20)
                plt.scatter(0, 0, s = 100, marker = 'D')
                plt.axis("off")
            else:
                self.displayImage(imgPath, j)
            j += 1
        plt.show()
        plt.pause(0.3)
        

def dfs(myEnv, problem):
    # explored - орсон state-үүдээ тэмдэглэх хувьсагч
    # frontier - мод
    explored , frontier = set(), list([Node(problem.initial)])
    global orson
    while frontier:
        # shineer orsnoos ni ehleed gargaad yvna LIFO
        node = frontier.pop()
        explored.add(node.map)
        # print(node.map)
        if problem.goal_test(node.state):
            # дэндүү их тоо гарч байсан тул comment болгосон
            # states = problem.backtrace(node)
            print("Depth first search")
            print(f"last state =  {node.state}\ndepth = {node.depth}\norson node-iin = {orson}")
            # for move in states[:]:
                # myEnv.readImage(move)
            # myEnv.readImageWithoutClf(node.state)
            # moves = problem.backtraceMove(node)
            # return moves
            return 0
        # expand buyu teleh funktsiig ashiglan huu zangilaanuudiig olno
        possiblePaths = reversed(node.expand(node)) 
        for path in possiblePaths:
            # huu zangilaanuudaas orj baigaagui zangilaanuudiig modond hiine
            if path.map not in explored:
                frontier.append(path)
                explored.add(path.map)
    return "Илэрц олдсонгүй"
def bfs(myEnv, problem):
    global orson
    explored , frontier = set(), deque([Node(problem.initial)])
    while frontier:
        # ehelj orsnoos ni ehleed gargaad yvna FIFO
        node = frontier.popleft()
        explored.add(node.map)
        # print(node.map)
        if problem.goal_test(node.state):
            print("\n\nBreadth first search")
            # state helbereer anhnii node-oos goal node hurtelh nuudluudiig avav
            states = problem.backtrace(node)
            print(f"last state =  {node.state}\ndepth = {node.depth}\norson node-iin too = {node.path_cost}")
            for move in states[:]:
                myEnv.readImage(move)
            myEnv.readImageWithoutClf(node.state)
            # nuudel helbereer anhnii node-oos goal node hurtelh nuudluudiig avav
            move = problem.backtraceMove(node)
            return move
        # expand buyu teleh funktsiig ashiglan huu zangilaanuudiig olno
        possiblePaths = node.expand(node)
        for path in possiblePaths:
            # huu zangilaanuudaas orj baigaagui zangilaanuudiig modond hiine
            if path.map not in explored:
                frontier.append(path)
                explored.add(path.map)
    return "Илэрц олдсонгүй"

def getInvCountMine(arr):
    count = 0
    # бүх утгууд руу орох давталт
    for i in arr: 
        # тухайн утгаас хойших утгууд руу орох давталт
        for j in range(arr.index(i) , len(arr)):
            # tuhain utgaas hoino baigaa utguud ni tuunees baga bol count deer nemne
            if i > 0 and arr[j] and i > arr[j]:
                count += 1
    # niit count tegsh bol evluuleh bolomjtoi sondgoi bol bolomjgui
    return count

def isSolvable(puzzle) : 
    # Count inversions in given 8 puzzle 
    invCount = getInvCountMine(puzzle)
    # return true if inversion count is even. 
    return (invCount % 2 == 0)
     
def main():
    myEnv = Environment()
    # reshaped = np.array(myEnv.state).reshape(3,3)
    if not isSolvable(myEnv.state):
        print(f"inversion = {getInvCountMine(myEnv.state)} учир эвлүүлэх боломжгүй")
    else:
        print(f"inversion = {getInvCountMine(myEnv.state)} учир эвлүүлэх боломжтой")
        print(dfs(myEnv, MyProblem(myEnv.state)))
        print(bfs(myEnv, MyProblem(myEnv.state)))
    
if __name__ == "__main__":
    main()
