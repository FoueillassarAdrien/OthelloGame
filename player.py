import Board, Box

class Player:
    def __init__(self,count=2):
        self.setColor()
        self.count = count
        self.setName()

    def setName(self):
        name=""
        while name=="":
            name=str(input("Entrez votre pseudo : "))
        self.__name = name

    def getName(self):
        return self.__name

    def setColor(self):
        color=""
        color=str(input("Choix de la couleur X ou O : "))
        while color!="X" and color!="O":
            color=str(input("Choix invalide, entrez X ou O : "))
    
    def getColor(self):
        return self.__color

    def pawnCount(self,board):
        
        for i in range(board.size):
            for j in range(board.size):
                if self.color==board.status[i][j].getValue:
                    self.score+=1
