import Box, Player

class Board(object):
    size = 8
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    index = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, player1, player2):
        self.status = self.createStatus()
        self.p1 = player1.getName()
        self.p2 = player2.getName()
        self.header = self.createHeader()
    
    def createStatus(self):
        status = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(Box.Box(self.index[i], self.columns[j]))
            status.append(row)
        status[3][3].setValue('O')
        status[3][4].setValue('X')
        status[4][3].setValue('X')
        status[4][4].setValue('O')
        return status
    
    def createHeader(self):
        header = '\n* ------ WELCOME TO OTHELLO ------ *\n\n'
        header += f'        {self.p1} Vs {self.p2}\n\n'
        header += '     A   B   C   D   E   F   G   H\n'
        header += '   +---+---+---+---+---+---+---+---+'
        return header
    
    def displayBoard(self):
        print(self.header)
        for i in range(self.size):
            row = f' {i} |'
            for j in range(self.size):
                row += f' {self.status[i][j].getValue()} |'
            print(row)
            print('   +---+---+---+---+---+---+---+---+')
