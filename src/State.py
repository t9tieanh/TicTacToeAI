
import copy

class State : 
    def __init__(self, data = None, N = 3) :
        self.data = data 
        self.N = N 
    def Clone (self) : 
        sn = copy.deepcopy (self)
        return sn 
    def Print (self) : 
        sz = self.N 
        for i in range (sz) : 
            for j in range (sz) : 
                tmp = self.data[i*sz + j]
                if tmp == 0 : 
                    print ('_',end='')
                elif tmp == 1: 
                    print ('o',end = '')
                else : 
                    print ('x',end='')
            print()
        print ("------------------")