 # 4 buyu tuunees ih too oruulah
n = input('n = ')
rows = int(n)
# matrixay
matrix = [[0 for i in range(int(n))] for j in range(int(n))]
matrixAction = [[0 for i in range(int(n))] for j in range(int(n))]
# matrix = [[0] * rows] * rows
# print(matrix)
for i in range(int(n)):     
    # hamgiin ehnii bolon suuliin muriig uurchluh
    matrix[0][i] = 1
    matrix[int(n) - 1][i] = 1
    matrixAction[0][i] = 8
    matrixAction[int(n) - 1][i] = 8
    if i != 0 or i != int(n) - 1:
        # ehnii bolon suuliin muruus busad muriin
        # ehnii bolon suuliin elementiig uurchluh
        matrix[i][0] = 1
        matrix[i][-1] = 1
        matrixAction[i][0] = 8
        matrixAction[i][-1] = 8
# print(matrix)



if int(n) < 5: # 5-aas baga buyu 4 bol
    # 1 5 
    # 3 0 helbertei bolgono
    matrixAction[1][1] = 1
    matrixAction[1][2] = 5
    matrixAction[2][1] = 3
    matrixAction[2][2] = 0
else :
#goliin muruudiig uurchluh
    for i in range(int(n) - 2):
        for j in range(int(n) - 2):
            # 8 1 0 1 0 .... 8 helbertei bolgono
            if j % 2 == 0:
                matrixAction[i + 1][j + 1] = 1
            else :
                matrixAction[i + 1][j + 1] = 0
    # 2 dah muriig uurchluh
    for i in range(int(n) - 2):
        if i % 2 == 1:
            # 8 1 3 1 3 ...... 5 8 helbertei(2 dah moriig)
            matrixAction[1][i + 1] = 3
        else : 
            # 8 3 0 3 0 ...... 0 8 helbertei(suuleesee 2dah)
            matrixAction[-2][i + 1] = 3
    # herev n tegsh bol 2 dah muriin hamgiin suuliihiig 5 bolgoj 
    # duusgah sondgoi bol suuleesee 2 dah muriig
    if int(n) % 2 == 0 :
        matrixAction[1][-2] = 5
    else :
        matrixAction[-2][-2] = 5    
print(matrixAction)