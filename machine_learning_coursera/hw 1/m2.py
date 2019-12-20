def matadd(x,y):
    res = [[x[i][j] + y[i][j]  for j in range(len(x[0]))] for i in range(len(x))] 
    return res
def trans(x):
    t_matrix = zip(*x) 
    return t_matrix

    
x = [[1,2,3,4],[4,5,6,5],[7,8,9,3]] 
y = [[9,8,7,6],[6,5,4,3],[3,2,1,3]]
result = matadd(x,y)
x = trans(x)
for i in result:
    print(i)