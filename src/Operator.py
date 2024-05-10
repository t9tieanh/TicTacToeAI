import src.State

class Operator : 
    def __init__(self,x = 0, y = 0) :
        self.x = x 
        self.y = y 
    # hàm đánh 
    def Move (self, s) : 
        sz = s.N # lấy size của state 
        x = self.x 
        y = self.y
        if x >= sz or x < 0 : 
            return None 
        if y >= sz or y < 0 : 
            return None 
        if s.data[x * sz + y] != 0 : 
            return None 
        # xác định lượt đánh để đánh 
        res = 0 
        for value in s.data : 
            if value != 0 : res += 1 
        sn = s.Clone() 
        if res % 2 == 0 : sn.data[x * sz + y] = 1 
        else : sn.data[x * sz + y] = 2
        return sn 
