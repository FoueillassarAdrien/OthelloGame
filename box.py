class Box(object):
    def __init__(self, x, y):
        self.row = x
        self.column = y
        self.setValue()
    
    def setValue(self, value=' '):
        if value in ['X', 'O', ' ']:
            self.__value = value
        else:
            raise ValueError(f'"{value}" not a valid caracter')
    
    def getValue(self):
        return self.__value