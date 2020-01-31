class Matrix():
    
    
    def __init__(self, rows, cols):
        self.m = rows
        self.n = cols
    
    def user_fill(self):
        self.content = []
        
        for i in range(self.m):
            elements = []
            
            for j in range(self.n):
                element = float(input("[{},{}] element = ".format(i + 1, j + 1)))
                elements.append(element)
            
            self.content.append(elements)
            
    def zeros(self):
        self.content = []
        
        for i in range(self.m):
            elements = []
            
            for j in range(self.n):
                element = 0
                elements.append(element)
            
            self.content.append(elements)
            
    def ones(self):
        self.content = []
        
        for i in range(self.m):
            elements = []
            
            for j in range(self.n):
                element = 1
                elements.append(element)
            
            self.content.append(elements)
            
    def unit(self):
        if(self.m == self.n):
            self.content = []
            
            for i in range(self.m):
                elements = []
                
                for j in range(self.n):
                    if (i==j):
                        element = 1
                    else:
                        element = 0
                    elements.append(element)
            
                self.content.append(elements)
        else:
            print("size not equal")
            
    def add(self, other_matrix):
        if(self.n == other_matrix.n and self.m == other_matrix.m and len(self.content) != 0 and len(other_matrix.content) != 0):
            for i in range(self.m):
                for j in range(self.n):
                    self.content[i][j] = self.content[i][j] + other_matrix.content[i][j]
            
        else:
            print("size not equal")
            
    def substr(self, other_matrix):
        if(self.n == other_matrix.n and self.m == other_matrix.m and len(self.content) != 0 and len(other_matrix.content) != 0):
            for i in range(self.m):
                for j in range(self.n):
                    self.content[i][j] = self.content[i][j] - other_matrix.content[i][j]
            
        else:
            print("size not equal")
            
    def multiplyByNum(self, a):
        for i in range(self.m):
            for j in range(self.n):
                self.content[i][j] = a*self.content[i][j]