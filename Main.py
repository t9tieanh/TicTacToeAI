from src.gui import TicTacToe
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    game = TicTacToe(root)
    root.mainloop()