import english_words
import string
import igraph
import matplotlib.pyplot as plt
import plotly.graph_objects as go
def alphabet_position(text):
	return [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
def alphabet_character(text):
	return ''.join([chr(int(x)) for x in text])
myalphabet = string.ascii_lowercase
 # 4n usegtei angli ugnuud
    # print([i for i in list(english_words_lower_alpha_set) if len(i) == 4])
    # first = input("Эхний үгийг оруулна уу.")
    # mylen = len(first)
    # last = input("Хувиргах үгийг оруулна уу.")
    # a = {
    #     'cool': [3.5, 0.7], 'fail': [3.5, 9], 'fall': [6.8, 9], 'foil': [1.2,7.5], 'fool': [1.2, 2], 'foul': [0.5, 5], 'page': [18, 2], 'pale': [16.5, 4], 'pall': [8.5, 7.5], 'pole': [10, 5], 'poll': [8.5, 2], 'pool': [7, 0.7], 'pope': [15, 7], 'sage': [19, 3], 'sale': [18, 5]
    # }
    # edges = [('fool', 'foul'), ('fool', 'foil'), ('fool', 'cool'), ('fool', 'pool'), ('foul', 'foil'),('foil','fail'),('fail','fall'),('fall','pall'),('pall', 'poll'),('poll', 'pool'),('pool','cool'),('poll','pole'),('pole','pope'),('pole','pale'),('pale','sale'),('pale','page'),('sale','sage'),('page','sage')]
    # vertices = set()
    # for line in edges:
    #     vertices.update(line)
    # vertices = sorted(vertices)
    # g = igraph.Graph() # 2 stands for children number
    # g.add_vertices(vertices)
    # g.add_edges(edges)
    # g.es['weight'] = 1
    # plt.figure(figsize=(10,5))
    # plt.plot()
    # plt.ylim([0, 10])
    # plt.xlim([0, 20])
    # plt.show()
print(vertices)
print(g)

def doesntwork():
    
#ajillahgui
    def expandGraph(self, problem):
        # return [self.child_node(problem, action)
        #     for action in problem.actions(self.state)]
        childrens = list()
        # def alphabet_position(text):
        #     return [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
        # def alphabet_character(text):
        #     return ''.join([chr(int(x)) for x in text])
        mystate = list(self.state)
        mylen = len(mystate)
        mygraph = problem.graph.graph_dict
        mygraph = self.mysearch(childrens, mystate, mylen, problem, mygraph )
        print(mygraph)
        return childrens
    # hamgiin hoinoos ni buh usguudiig ni soliod yvna
    # aaa → aab, aac ... aaz, aba, abb, abc geh met
    def mysearch(self, childrens ,state, leng, problem, mygraph, index=0):
        letters = string.ascii_lowercase
        umnuhState = ''.join(state)
        for i in range(index, leng):
            # letters = letters.replace(f'{state[i]}', '')
            for j in letters:
                state[i] = j
                actualstate = ''.join(state)
                if umnuhState and actualstate in english_words_lower_alpha_set:
                    mygraph[umnuhState] = {}
                    a = mygraph[umnuhState]
                    # print(actualstate)
                    # childrens.append(Node(actualstate, self, actualstate, problem.path_cost(self.path_cost, self.state, actualstate, actualstate)))
                    self.state = actualstate
                    a[actualstate] = 1
                if i < leng:
                    mygraph = self.mysearch(childrens, state, leng, problem, mygraph, i+1)
        # self.state = childrens[-1]
        return mygraph
