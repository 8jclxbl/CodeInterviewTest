"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""
import numpy as np
class Solution:
    def __init__(self):
        self.mask = None
        self.matrix = None
        self.path = None

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.path = path
        self.path_length = len(path)
        

        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols + j] == path[0]:
                    self.mask = [0 for k in range(rows * cols)]
                    if self._hasPath(i,j,0): return True
        return False

    def _hasPath(self,x,y,cur):
        temp = x * self.cols + y
        if     x >= self.rows \
            or x < 0 \
            or y >= self.cols \
            or y < 0 \
            or self.matrix[temp] != self.path[cur] \
            or self.mask[temp] == 1: 
            return False
        #print(np.array(self.mask).reshape(5,8),x,y,self.path[cur],self.matrix[temp])

        if cur == self.path_length - 1: return True
        self.mask[temp] = 1

        if self._hasPath(x+1,y,cur + 1) or self._hasPath(x-1,y,cur + 1) or self._hasPath(x,y+1,cur + 1) or self._hasPath(x,y-1,cur + 1):
            return True
        self.mask[temp] = 0
        return False


"""
test = [['a', 'b', 'c', 'e'], 
        ['s', 'f', 'c', 's'], 
        ['a', 'd', 'e', 'e']]
path1 = 'bcced'
path2 = 'abcd'
"""

"""
ABCEHJIG
SFCSLOPQ
ADEEMNOE
ADIDEJFM
VCEIFGGS
"""

s = Solution()
"""
print(s.hasPath(test,3,4,path1))
print(s.mask)

print(s.hasPath(test,3,4,path2))
print(s.mask)
"""
print(s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SLHECCEIDEJFGGFIE"))
print(s.mask)
