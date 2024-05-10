from src.Operator import *

def isEndNode (s) : 
    sz = s.N 
    data = s.data 
    for i in range (sz) : 
        if data[i*sz] != 0 and data[i*sz + 0] == data[i*sz + 1] == data[i * sz + 2]  :
            return True 
        if  data[sz + i] != 0 and data[0 * sz + i] == data[1 * sz + i] == data[2 * sz + i] : 
            return True
    # đường chéo chính   
    if data [0] != 0 and data [0] == data[4] == data[8] : 
        return True 
    # đường chéo phụ 
    if data [2] != 0 and data[2] == data[4] == data[6] : 
        return True 
    # nếu còn node chưa đánh -> chưa kết thúc game 
    for value in data : 
        if value == 0 : return False
    return True # đã kết thúc game 

def Win (s) :
    if s.data == None : 
        return False 
    sz = s.N 
    data = s.data 
    for i in range (sz) : 
        if data[i*sz] != 0 and (data[i*sz + 0] == data[i*sz + 1] == data[i * sz + 2])  :
            return True 
        if  data[sz + i] != 0 and (data[0 * sz + i] == data[1 * sz + i] == data[2 * sz + i]) : 
            return True
    # đường chéo chính   
    if data [0] != 0 and data [0] == data[4] == data[8] : 
        return True 
    # đường chéo phụ 
    if data [2] != 0 and data[2] == data[4] == data[6] : 
        return True  
    return False # các trường hợp còn lại  


def CheckMyTurn (s) : 
    res = 0 
    for x in s.data : 
        if x == 0 : res += 1 
    if res % 2 == 0 :  return True # lượt chẵn thì AI đi  
    return False 

def Value (s) : 
    if Win (s) : 
        if CheckMyTurn (s) : 
            return 1 # nếu là lượt mình mà thằng -> 1 
        return -1 # lượt người khác thì -> -1
    return 0 

def AlphaBeta (s, d, a, b, mp) : 
    if isEndNode (s) or d == 0 : 
        return Value (s) 
    sz = s.N 
    if mp == True : # maximum layer 
        for i in range (sz) : 
            for j in range (sz) : 
                child = Operator(i,j).Move(s) 
                if child == None : continue # i,j không đánh được 
                tmp = AlphaBeta (child, d - 1 , a , b , False) 
                a = max (a, tmp) 
                if a >= b : break 
        return a 
    else : # minimum player 
        for i in range (sz) : 
            for j in range (sz) : 
                child = Operator(i,j).Move(s) 
                if child == None : continue # i,j không đánh được 
                tmp = AlphaBeta (child, d - 1 , a , b , True) 
                b = min (b, tmp) 
                if a >= b : break 
        return b 

def MiniMax (s, d, mp) : 
    return AlphaBeta (s, d, -2, 2, mp)