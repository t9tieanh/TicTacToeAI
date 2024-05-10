from tkinter import * 
from src.State import * 
from src.Operator import *  
from src.Algorithm import * 
from PIL import Image, ImageTk

class TicTacToe:
    def __init__(self, root):
        # các trạng thái bàn cờ
        self.state = State ([0,0,0,
                        0,0,0,
                        0,0,0])
        self.btn = [0,0,0,
                    0,0,0,
                    0,0,0] # dùng để lưu button trong frame 
        self.status = 0 # trạng thái của bàn cờ 0 chưa phân thắng bại , 1 : hòa , 2 đã có người thắng
        #
        self.root = root
        self.root.geometry("550x720")
        # self.root.configure(bg='#87CEEB')
        self.root.configure(bg='#ffffff')
        self.root.resizable(False, False)
        self.root.title("Game Tic-Tac-Toe, Phạm Tiến Anh")
        logo_path = 'image\\logo.ico'
        self.root.iconbitmap(logo_path)
         # Đặt hình nền
        self.bg_image = Image.open('Image\\background.jpg')
        self.bg_image = self.bg_image.resize((550, 720), Image.Resampling.LANCZOS)  # Thay đổi tại đây
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.background_label = Label(self.root, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.lblPlayer = Label(self.root, bg='#E3CF57', text="It's your turn (o)", font=('consolas', 15))
        self.lblPlayer.place(x=170, y=30)

        self.btnReset = Button(self.root, text="Play Again", bg='#E3CF57', font=("consolas", 15), command = self.RestartGame)
        self.btnReset.place(x=200, y=70)

        self.frame = Frame(self.root) # frame chứa bàn cờ 
        self.frame.place(x=10, y=120)

        # bắt đầu vẽ bàn cờ 
        sz = self.state.N 
        for i in range(sz):
            for j in range(sz):
                self.btn[i * sz + j] = Button(self.frame, text="_", fg = '#00688B', bg='#E3CF57', font=('consolas', 40), width=5, height=2,
                    command=lambda row= i, column = j: self.play(row, column))
                self.btn[i * sz + j].grid(row=i, column=j, padx=10, pady=10)
    

    def Update (self) : 
        sz = self.state.N 
        for i in range(sz):
            for j in range(sz):
                if (self.status == 0) : 
                    self.btn[i*sz+j].config(fg = '#00688B')
                if self.state.data[i*sz+j] == 1 : 
                    self.btn[i*sz+j].config(text="o")
                elif self.state.data[i*3+j] == 2 :
                    self.btn[i*sz+j].config(text="x")
                else : 
                    self.btn[i*sz+j].config(text="_")


    def CheckWin (self) :
        if self.state.data == None : 
            return False 
        sz = self.state.N
        data = self.state.data
        for i in range (sz) : 
            if data[i*sz] != 0 and (data[i*sz + 0] == data[i*sz + 1] == data[i * sz + 2])  :
                for j in range (sz): self.btn[i*sz + j].configure(fg = 'red')
                return True 
            if  data[sz + i] != 0 and (data[0 * sz + i] == data[1 * sz + i] == data[2 * sz + i]) : 
                for j in range (sz): self.btn[j*sz + i].configure(fg = 'red')
                return True
        # đường chéo chính   
        if data [0] != 0 and data [0] == data[4] == data[8] : 
            for j in range (sz): self.btn[j*sz + j].configure(fg = 'red')
            return True 
        # đường chéo phụ 
        if data [2] != 0 and data[2] == data[4] == data[6] : 
            for j in range (sz): self.btn[j*sz + sz-j-1].configure(fg = 'red')
            return True  
        
        for value in data : 
            if value == 0 : return False

        return 'draw' # trường hợp hòa


    def RestartGame (self) : 
        self.status = 0
        self.state = State ([0,0,0,
                        0,0,0,
                        0,0,0])
        self.Update()
        self.lblPlayer.config (text="It's your turn (o)")

    # đánh 
    def play (self, x , y) : 
        if (self.status != 0) : return 

        child = Operator(x,y).Move(self.state)
        if child == None : return # đánh sai  
        self.state = child
        self.Update()

        if self.CheckWin () == 'draw' : 
            self.lblPlayer.config (text="Draw, Restart ?")
            self.status = 1
            return 

        if self.CheckWin () :  
            self.lblPlayer.config (text="Player won, Restart ?")  
            self.status = 2
            return 

        # đến lượt AI 
        mn = 2 
        minChild = None 
        sz = self.state.N 
        for i in range (sz) : 
            for j in range (sz) : 
                child = Operator (i,j).Move(self.state)
                if child == None : 
                    continue 
                tmp = MiniMax (child , 1 , True)
                print (i,j,tmp) 
                if mn > tmp : 
                    mn = tmp 
                    minChild = child 
        self.state = minChild
        self.Update() 

        if self.CheckWin() :  # ai win
            self.lblPlayer.config (text="AI won, Restart ?")  
            self.status = 2
            return 

