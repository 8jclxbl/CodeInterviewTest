def printMatrix(matrix):
    if matrix == []: return []
    if type(matrix[0]) != type([]): return matrix
    
    rn = len(matrix)
    cn = len(matrix[0])
    rmin = 0
    cmin = 0
    rmax = rn
    cmax = cn

    temp = []

    while rmin < rmax and cmin < cmax:
        for i in range(cmin,cmax):
            temp.append(matrix[rmin][i])
        rmin += 1
        if rmax - rmin < 1:break
        for i in range(rmin,rmax):
            temp.append(matrix[i][cmax-1])
        cmax -= 1
        if cmax - cmin < 1:break
        for i in range(cmax-1,cmin-1,-1):
            temp.append(matrix[rmax-1][i])
        rmax -= 1
        if rmax - rmin < 1:break
        for i in range(rmax-1,rmin-1,-1):
            temp.append(matrix[i][cmin])
        cmin += 1
        
    return temp 

print(printMatrix([1]))

def printMatrix(self, matrix):
        # write code here
        result = []
        while(matrix):
            result+=matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat