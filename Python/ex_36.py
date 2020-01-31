class Prostokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def obwod(self):
        return 2*self.a+2*self.b

    def pole(self):
        return self.a*self.b

class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a)