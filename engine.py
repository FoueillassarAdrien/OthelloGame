import Player, Board, Box

class Engine(object):
    invert = {'X':'O', 'O':'X'}
    def launchGame(self):
        self.round = 0
        self.p1 = Player.Player()
        self.p2 = Player.Player()
        self.board = Board.Board(self.p1, self.p2)

        while self.testEnd()==False:
            self.round += 1
            newPawn = self.playPawn(self.p1, self.board)
            if newPawn:
                newPawn.set_color(self.p1.getColor())
                self.changeColor(self, newPawn)

            newPawn = self.playPawn(self.p2, self.board)
            if newPawn:
                newPawn.set_color(self.p2.getColor())
                self.changeColor(self, newPawn)

    def playPawn(self, player):
        self.board.displayBoard()
        print(f"Player: {player.name} - Round: {self.round}")
        b = self.askMove(self.board)

        validBoxes = self.playableBoxes(self.board, player)
        if len(validBoxes) > 0:
            while b not in validBoxes:
                print('Déso frère, joue autre chose...')
                b = self.askMove(self.board)
        else:
            print('Dommage plus de case à jouer...')
            return None
        return b

    def askMove(self):
        r = input("Line coordinate (1-8):")
        while r not in self.board.index:
            print('Not a valid line number (1-8)')
            r = input("Line coordinate (1-8):")
        c = input("Columne coordinate (A-H):")
        while c not in self.board.columns:
            print('Not a valid columns letter (A-H)')
            c = input("Columns coordinate (A-H):")
        return Box.Box(r, c)
    
    def playableBoxes(self, player):
        listOfList = self.board.status
        validBoxes = [item for sub in listOfList for item in sub]
        for b in validBoxes:
            if b.getValue() != ' ':
                validBoxes.remove(b)
        for b in validBoxes:
            nb = 0
            for direction in ['N', 'W', 'S', 'E']:
                nb += self.testInBetween(self, b, direction, player.getColor())
            if nb == 0:
                validBoxes.remove(b)
        return validBoxes
    
    def testInBetween(self, box, direction, color):
        i = self.board.index.index(box.row)
        j = self.board.index.index(box.column)
        v = color
        nb = 0

        if (direction=='N') and (1 < i):
            if self.board.status[i-1][j].getValue() == self.invert[v]:
                nb = 1
                valid = False
                for l in range(i-2, -1, -1):
                    if self.board.status[l][j].getValue() == v:
                        valid = True
                        break
                    elif self.board.status[l][j].getValue() == self.invert[v]:
                        nb += 1
                    else:
                        break
    
        if (direction=='W') and (1 < j):
            if self.board.status[i][j-1].getValue() == self.invert[v]:
                nb = 1
                valid = False
                for l in range(j-2, -1, -1):
                    if self.board.status[i][l].getValue() == v:
                        valid = True
                        break
                    elif self.board.status[i][l].getValue() == self.invert[v]:
                        nb += 1
                    else:
                        break

        if (direction=='S') and (i < self.board.size-3):
            if self.board.status[i+1][j].getValue() == self.invert[v]:
                nb = 1
                valid = False
                for l in range(i+2, self.board.size):
                    if self.board.status[l][j].getValue() == v:
                        valid = True
                        break
                    elif self.board.status[l][j].getValue() == self.invert[v]:
                        nb += 1
                    else:
                        break

        if (direction=='E') and (j < self.board.size-3):
            if self.board.status[i][j+1].getValue() == self.invert[v]:
                nb = 1
                valid = False
                for l in range(j+2, self.board.size):
                    if self.board.status[l][j].getValue() == v:
                        valid = True
                        break
                    elif self.board.status[l][j].getValue() == self.invert[v]:
                        nb += 1
                    else:
                        break
        return nb

    def changeColor(self, newPawn):
        i = self.board.index.index(newPawn.row)
        j = self.board.index.index(newPawn.column)
        c = newPawn.getValue()

        for direction in ['N', 'W', 'S', 'E']:
            nb = self.testInBetween(self, newPawn, direction, c)
            if direction == ['N']:
                for l in range(i, i-nb-1, -1):
                    self.board.status[l][j].setValue(c)
            if direction == ['W']:
                for l in range(j, j-nb-1, -1):
                    self.board.status[i][l].setValue(c)
            if direction == ['S']:
                for l in range(i, i+nb+1):
                    self.board.status[l][j].setValue(c)
            if direction == ['E']:
                for l in range(j, j+nb+1):
                    self.board.status[i][l].setValue(c)
    
    def testEnd(self):
        vBP1 = self.playableBoxes(self.p1)
        vBP2 = self.playableBoxes(self.p2)
        return True if vBP1+vBP2 == 0 else False


if __name__ == '__main__':
    engine = Engine()
    engine.launchGame()
        