import random, copy
import matplotlib.pyplot as plt

# matrix-d    1 = хана, 0 = цэвэрхэн, 2 = бохир
# matrix = [
#     [1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1]
# ]
# matrixAction-d  0 = дээшээ, 1 = доошоо, 3 = баруун, 4 = цэвэрлэх, 5 = дуусах
# matrixAction = [
#     [9, 9, 9, 9, 9, 9],
#     [9, 1, 3, 1, 5, 9],
#     [9, 1, 0, 1, 0, 9], 
#     [9, 1, 0, 1, 0, 9], 
#     [9, 3, 0, 3, 0, 9],
#     [9, 9, 9, 9, 9, 9]
# ]
# matrix = []
# matrixAction = []



bagana = 1
mur = 1
n = 0
class Object:
    alive = True
    #Энэ нь хүрээлэн буй орчинд гарч болох аливаа биет объектыг илэрхийлнэ.
    #Хүссэн обьектуудаа авахын тулд та Object-ийн дэд ангиллыг үүсгэж ашиглана.
    #Объект бүр нь __ name__slot (зөвхөн гаралтанд ашигладаг)-тай байж болно .
    def __repr__(self):
        return '<%s>' % getattr(self, '__name__', self.__class__.__name__)
    def is_alive(self):
    #Амьд объектууд үнэн утгыг буцаана
        return hasattr(self, 'alive') and self.alive
    def display(self, matrix):
    #Объектын дүрслэлийг харуулах
        plt.imshow(matrix, 'terrain')
        plt.show(block=False)
        plt.plot(bagana, mur, 'D', 'Өрөө')
        plt.pause(0.4)
        plt.clf()

class Agent(Object):
    def __init__(self):
        def program(percept):
            return input('Percept=%s; action? ' % percept)
        self.prog = program
        self.alive = True
    def TraceAgent(self, agent):
        #Агентын програмыг оролт, гаралтыг багцалж хэвлэнэ. Энэ нь агент тухайн
        #орчинд юу хийж байгааг харуулна.
        old_program = agent.program
        def new_program(self, percept):
            action = old_program(percept)
            print('%s perceives %s and does %s' % (agent, percept, action))
            return action
        agent.program = new_program
        return agent

class SimpleReflexAgent(Agent):
    
    def __init__(self, m):
        # matrix-ийн бүх index-д санамсаргүйгээр утга онооно
        for mI in range(1, int(n) - 1):
            for aI in range(1, int(n) - 1):
                # 0 ,1, 2, 3 гэсэн тоонуудаас санамсаргүйгээр 1 тоо аван (25%)
                # тухайн тоо нь 1 бол тэр хэсгийн утгыг 2 буюу бохир болгоно
                number = random.randint(0, 3)
                m[mI][aI] = 2 if number == 1 else 0
        # эцэг классын дүрслэх функцыг дуудаж анхны төлвийг харуулна
        super(SimpleReflexAgent, self).display(matrix)
        # drawMatrix(matrix)
        self.program()
    
    def drawMatrix(self, matrix):
        super(SimpleReflexAgent, self).display(matrix)
        
    def simpleAgentRobot(self, x, y):
        if (matrix[x][y] == 2): 
            # matrix-ийн block бохир бол 4-ийг явуулж цэвэрлэнэ
            return 4
        else:
            print("NoOp")
        # цэвэрхэн бол дараа нь хаашаа явах вэ гэдгээ matrixAction-с авна
        return matrixAction[x][y]
    
    def program(self):
        global mur
        global bagana
        while True:
            # мөр, баганыг шалгаж үзэн цэвэрлэж эсвэл 1 тийш явах үйлдлүүдийг хийнэ
            action = self.simpleAgentRobot(mur, bagana)
            if (action == 0): # дээшээ явах бол
                print("Up")
                mur = mur - 1 # мөрөөс 1-ийг хасна
                self.drawMatrix(matrix)
            elif (action == 1): # доошоо явах бол
                print("Down")
                mur = mur + 1 # мөр дээр 1-ийг нэмнэ
                self.drawMatrix(matrix)
            elif (action == 2): # зүүн явах бол
                print("Left")
                bagana = bagana - 1 # баганаас 1-ийг хасна
                self.drawMatrix(matrix)
            elif (action == 3): # баруун явах бол
                print("Right")
                bagana = bagana + 1 # багана дээр 1-ийг нэмнэ 
                self.drawMatrix(matrix)
            elif (action == 4): # цэвэрлэх матрикс блокийн утгыг 0 болгоно
                print("Suck")
                matrix[mur][bagana] = 0
                self.drawMatrix(matrix)
            else:
                print("end")
                # drawMatrix(matrix)
                break

class Environment:
# Environment-д хэрэглэгчээс 'n' утгыг аван n-ийн квадрат matrix-уудыг үүсгэн
# үүсгэсэн matrix-д санамсаргүйгээр бохир утгыг оруулан цааш ажиллуулна
    def __init__(self):
        self.objects = []; self.agents = []
        # object_classes = [] ## Орчинд нэвтрэх боломжтой хичээлүүдийн жагсаалт
        global n
        global matrix
        global matrixAction
        n = input('2 буюу түүнээс их өрөөний мөр баганы тоо болох n-ийг оруулна уу.\nn = ')
        n = int(n) + 2
        # n урттай квадрат matrix үүсгэх
        matrix = [[0 for i in range(int(n))] for j in range(int(n))]
        matrixAction = [[0 for i in range(int(n))] for j in range(int(n))]
        # matrix = [[0] * rows] * rows
        # print(matrix)
        for i in range(int(n)):     
            # хамгийн эхний болон сүүлийн мөрийг өөрчлөх
            matrix[0][i] = 1
            matrix[int(n) - 1][i] = 1
            matrixAction[0][i] = 8
            matrixAction[int(n) - 1][i] = 8
            if i != 0 or i != int(n) - 1:
                # эхний болон сүүлийн мөрөөс бусад мөрийн
                # эхний болон сүүлийн элементийг өөрчлөх
                matrix[i][0] = 1
                matrix[i][-1] = 1
                matrixAction[i][0] = 8
                matrixAction[i][-1] = 8
        # print(matrix)

        if int(n) < 5: # 5-аас бага буюу 4 бол
            # 1 5 
            # 3 0 хэлбэртэй болгоно
            matrixAction[1][1] = 1
            matrixAction[1][2] = 5
            matrixAction[2][1] = 3
            matrixAction[2][2] = 0
        else :
        # голын мөрүүдийг өөрчлөх
            for i in range(int(n) - 2):
                for j in range(int(n) - 2):
                    # 8 1 0 1 0 .... 8 хэлбэртэй болгоно
                    if j % 2 == 0:
                        matrixAction[i + 1][j + 1] = 1
                    else :
                        matrixAction[i + 1][j + 1] = 0
            # 2 дахь мөрийг өөрчлөх
            for i in range(int(n) - 2):
                if i % 2 == 1:
                    # 8 1 3 1 3 ...... 5 8 хэлбэртэй(2 дахь мөрийг)
                    matrixAction[1][i + 1] = 3
                else : 
                    # 8 3 0 3 0 ...... 0 8 хэлбэртэй(сүүлээсээ 2 дахь)
                    matrixAction[-2][i + 1] = 3
            # хэрэв n тэгш бол 2 дахь мөрийн хамгийн сүүлийхийг 5 болгож
            # дуусгах сондгой бол сүүлээсээ 2 дахь мөрийг
            if int(n) % 2 == 0 :
                matrixAction[1][-2] = 5
            else :
                matrixAction[-2][-2] = 5    
        # print(matrixAction)
    def percept(self, agent):
        #Агентын харж буй ойлголтыг буцаана. Засварлаж утга оруулна
        # abstract
        pass


def main():
    Environment()
    SimpleReflexAgent(matrix)
    print(f"Цэвэрлэгдлээ!")
    

if __name__ == "__main__":
    main()