class MyHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def insert(self, val):
        if  self.size != 0 and self.find(val) != -1: 
            print('val has in the heap')
            return -1
        self.heap.append(val)
        self.size += 1
        cur = self.size - 1
        return self.upflow(cur)
    
    def delete(self):
        if self.size == 0:
            print('the heap is empty')
            return -1
        else:
            self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
            res = self.heap.pop()
            self.size -= 1
            self.downflow(0)
            return res
            
    def downflow(self,cur):
        childl = cur * 2 + 1
        childr = cur * 2 + 2
        if childl < self.size and childr == self.size:
            if self.heap[cur] < self.heap[childl]: 
                self.heap[cur],self.heap[childl] = self.heap[childl],self.heap[cur]
            return cur
        elif childr < self.size:
            if self.heap[cur] < self.heap[childl] and self.heap[childl] > self.heap[childr]:
                self.heap[cur],self.heap[childl] = self.heap[childl],self.heap[cur]
                return self.downflow(childl)
            elif self.heap[cur] < self.heap[childr] and self.heap[childr] > self.heap[childl]:
                self.heap[cur],self.heap[childr] = self.heap[childr],self.heap[cur]
                return self.downflow(childr)
        else:
            return cur
            
            
    
    def find(self,val,cur = 0):
        if self.heap[cur] == val:return cur
        else:
            if self.heap[cur] < val: return -1
            else:
                child = cur * 2 + 1
                if child < self.size:
                    return self.find(val,child)
                if child + 1 < self.size:
                    return self.find(val,child + 1)
                
    def upflow(self,cur):
        if cur % 2 != 0:
            parent = cur//2
        else:
            parent = cur//2 - 1
        if parent >= 0:
            if self.heap[parent] < self.heap[cur]:
                self.heap[parent],self.heap[cur] = self.heap[cur],self.heap[parent]
                return self.upflow(parent)
        return cur         

def heap_sort(array,reverse = False):
        h = MyHeap()
        res = []
        for i in array:
            h.insert(i)
        while h.size:
            res.append(h.delete())
        if reverse: return res[::-1]
        return res