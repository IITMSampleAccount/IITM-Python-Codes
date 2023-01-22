dic = {}
dic[8] = [[0, 59, 38, 33, 30, 17, 8, 63], [37, 34, 31, 60, 9, 62, 29, 16], [58, 1, 36, 39, 32, 27, 18, 7], [35, 48, 41, 26, 61, 10, 15, 28], [42, 57, 2, 49, 40, 23, 6, 19], [47, 50, 45, 54, 25, 20, 11, 14], [56, 43, 52, 3, 22, 13, 24, 5], [51, 46, 55, 44, 53, 4, 21, 12]]
dic[7] = [[0, 37, 30, 7, 18, 35, 14],[31, 28, 19, 36, 15, 6, 17],[38, 1, 32, 29, 8, 13, 34],[27, 24, 39, 20, 33, 16, 5],[40, 21, 2, 25, 44, 9, 12],[23, 26, 47, 42, 11, 4, 45],[48, 41, 22, 3, 46, 43, 10]]
dic[6] = [[0, 15, 6, 25, 10, 13], [33, 24, 11, 14, 5, 26], [16, 1, 32, 7, 12, 9], [31, 34, 23, 20, 27, 4], [22, 17, 2, 29, 8, 19], [35, 30, 21, 18, 3, 28]]
dic[5] = [[0, 5, 14, 9, 20], [13, 8, 19, 4, 15], [18, 1, 6, 21, 10], [7, 12, 23, 16, 3], [24, 17, 2, 11, 22]]
N=int(input())
def is_valid(i, j, sol):
    if(i>=0 and i<N and j>=0 and j<N):
        if(sol[i][j]==-1):
            return True
    return False

def knight_tour(sol, i, j, step_count, x_move, y_move):
    if(step_count==N*N):
        return True
    for k in range(0, len(x_move)):
        next_i=i+x_move[k]
        next_j=j+y_move[k]
        if(is_valid(next_i, next_j, sol)):
            sol[next_i][next_j]=step_count
            if(knight_tour(sol, next_i, next_j, step_count+1, x_move, y_move)):
                return True
            sol[next_i][next_j]=-1;
    return False
    
def start_knight_tour():
    sol=[]
    for i in range(0, N):
        a=([-1]*N)
        sol.append(a)
    x_move=[2, 1, -1, -2, -2, -1, 1, 2]
    y_move=[1, 2, 2, 1, -1, -2, -2, -1]
    sol[0][0]=0
    if(knight_tour(sol, 0, 0, 1, x_move, y_move)):
        for i in range(0, N):
            sol[i] = [x + 1 for x in sol[i]]
        for i in range(0, N):
            for j in range(0, N):
                print(sol[i][j], end = " ")
            print()
        return True
    return False
    
if(__name__=="__main__"):
    if dic.get(N) != None: 
        sol = dic[N]
        for i in range(0, N):
            for j in range(0, N):
                print(sol[i][j] + 1, end = " ")
            print()
    else:
        start_knight_tour()